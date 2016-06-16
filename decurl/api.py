from .parser import CurlParser
from collections import OrderedDict
import json
from six.moves import http_cookies as Cookie
from cookielib import MozillaCookieJar as CookieJar
import shlex
import os, re
import requests

# Create a parser object for the curl statement 
parser = CurlParser()

def call(curl_command):
    method = "get"

    tokens = shlex.split(curl_command)
    parsed_args = parser.parse_args(tokens)

    # read from config file if specified
    # else read from stdin
    if parsed_args.config:
        if parsed_args.config == '-':
            # read from stdin
            curl_command = sys.stdin.read()
        else:
            curl_command = curl_config.convert(parsed_args.config)
        tokens = shlex.split(curl_command)
        parsed_args = parser.parse_args(tokens)

    base_indent = " " * 4
    data_token = ''
    post_data = parsed_args.data or parsed_args.data_binary
    post_data_json = None
    if post_data:
        method = 'post'
        try:
            post_data_json = json.loads(post_data)
        except ValueError:
            post_data_json = None

        
        # JMW
        # parse the environment variables out of the string
        """
        env_vars = re.findall(r'\$\{[A-Za-z]+\}', post_data)
        if len(env_vars) > 0:
            post_data_split = re.split(r'\$\{[A-Za-z]+\}', post_data)
            for idx, ev in enumerate(map(lambda x: x.strip('${}'), env_vars)): 
                post_data_split.insert(idx+1, os.environ[ev])

            post_data = ''.join(post_data_split) # reassemble
        """
    cookie_dict = OrderedDict()
    quoted_headers = OrderedDict()
    
    if parsed_args.cookie_jar: # cookie file has been specified
        cookie_jar = CookieJar(parsed_args.cookie_jar)
        cookie_dict = 'cookie_jar'
    else: # original uncurl behavior
        for curl_header in parsed_args.header:
            header_key, header_value = curl_header.split(":", 1)

            if header_key.lower() == 'cookie':
                cookie = Cookie.SimpleCookie(header_value)
                for key in cookie:
                    cookie_dict[key] = cookie[key].value
            else:
                quoted_headers[header_key] = header_value.strip()
    
    proxy_dict = None # default
    if parsed_args.proxy:
        proxy_protocol = parsed_args.proxy.split(':')[0].lower()
        proxy_url = ':'.join(parsed_args.proxy.split(':')[1:])[2:]
        proxy_dict = {proxy_protocol : proxy_url}

    verify = parsed_args.insecure

    if method == 'get':
        requests_call = requests.get
    elif method == 'post':
        requests_call = requests.post

    result = requests_call(parsed_args.url,
                data=post_data_json if post_data_json else parsed_args.data,
                headers=quoted_headers,
                cookies=(cookie_jar if parsed_args.cookie_jar else cookie_dict),
                allow_redirects=parsed_args.location,
                proxies=proxy_dict,
                verify=parsed_args.insecure
                )
    
    return result
