from .parser import CurlParser, sub_env_vars
from . import curlio
from collections import OrderedDict
import json
from six.moves import http_cookies as Cookie
from cookielib import MozillaCookieJar as CookieJar
import shlex
import os, re
from urlparse import urlparse
import requests

# Create a parser object for the curl statement 
parser = CurlParser()

def call(curl_command, session=requests.Session()):
    """Makes a call with the requests module based on a command-line curl statement.

    Arguments:
    curl_command -- a string containing the curl command
    
    Optional arguments:
    session -- a requests.Session object for storing state. 
               default: a new requests.Session() object

    Returns:
    result -- a requests response
    """
    method = 'get'

    tokens = shlex.split(curl_command)
    parsed_args = parser.parse_args(tokens)

    # read from config file if specified
    # else read from stdin
    if parsed_args.config:
        if parsed_args.config == '-':
            # read from stdin
            curl_command = sys.stdin.read()
        else:
            curl_command = curlio.read_config(parsed_args.config)
        tokens = shlex.split(curl_command)
        parsed_args = parser.parse_args(tokens)

    post_data = parsed_args.data or parsed_args.data_binary
    # parse the environment variables out of the string
    post_data_json = None
    
    if post_data:
        method = 'post'
        post_data = sub_env_vars(post_data)
        try:
            post_data_json = json.loads(post_data)
        except ValueError:
            post_data_json = None
    
    cookie_dict = OrderedDict()
    quoted_headers = OrderedDict()
    
    if parsed_args.cookie_jar: # cookie jar file has been specified
        pass
    if parsed_args.cookie: # cookie file specified
        cookies = CookieJar(parsed_args.cookie)
        cookies.load()
        cookie_dict = cookies
    else:   # original uncurl behavior, parse cookies from -H
        for curl_header in parsed_args.header:
            header_key, header_value = curl_header.split(":", 1)

            if header_key.lower() == 'cookie':
                cookie = Cookie.SimpleCookie(header_value)
                for key in cookie:
                    cookie_dict[key] = cookie[key].value
            else:
                quoted_headers[header_key] = header_value.strip()
    
    # need to figure out behavior of proxies= option 
    # to see if it overwrites environment vars. Otherwise use
    # something like: 
    # if not any(('HTTP_PROXY','HTTPS_PROXY' in os.environ)):
    
    proxy_dict = None # default
    
    if parsed_args.proxy:
        proxy_url = urlparse(parsed_args.proxy)
        proxy_dict = {proxy_url[0] : ''.join(proxy_url[1:])}

    if method == 'get':
        requests_call = session.get
    elif method == 'post':
        requests_call = session.post
    
    # put in `with requests.Session() as s:` here
    # to take care of session cookies upon multiple requests
    result = requests_call(parsed_args.url,
                data=post_data_json if post_data_json else parsed_args.data,
                headers=quoted_headers,
                cookies=(cookie_jar if parsed_args.cookie_jar else cookie_dict),
                allow_redirects=parsed_args.location,
                proxies=proxy_dict,
                verify=parsed_args.insecure
                )
    
    return result
