import sure
import context
import decurl.api as api

def test_basic_get():
    result = api.call('curl http://weinerjm.github.io/hello.html')
    result.text.should.equal("Hello, world!\n")

def test_basic_headers():
    result = api.call('curl http://httpbin.org/headers -H "Accept: text/html" -H "Accept-Encoding: gzip,deflate,sdch"').json()
    result['headers']['Accept'].should.equal(u'text/html')
    result['headers']['Accept-Encoding'].should.equal(u'gzip,deflate,sdch')

def test_header_cookies():
    result = api.call('curl http://httpbin.org/get -H "Cookie: foo=bar; baz=baz2"').json()
    result['headers']['Cookie'].should.equal('foo=bar; baz=baz2')

def test_cookie_file():
    pass

def test_header_cookies_lowercase():
    result = api.call('curl http://httpbin.org/get -H "cookie: foo=bar; baz=baz2"').json()
    result['headers']['Cookie'].should.equal('foo=bar; baz=baz2')

def test_post():
    result = api.call("""curl http://httpbin.org/post --data '{"foo":"bar"}'""").json()
    result['form'].should.equal({'foo':'bar'})

def test_post_env_var():
    import os
    os.environ['foo'] = 'bar'
    result = api.call("""curl http://httpbin.org/post --data '{"foo":"${foo}"}'""").json()
    result['form'].should.equal({'foo':'bar'})

def test_post_with_dict_data():
    pass
# uncurl.parse("""curl 'https://pypi.python.org/pypi/uncurl' --data '{"evt":"newsletter.show","properties":{"newsletter_type":"userprofile"}}' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Cookie: foo=bar; baz=baz2'""").should.equal()

def test_post_with_form_data():
    pass
    # uncurl.parse("""curl 'https://pypi.python.org/pypi/uncurl' --data '{"evt":"newsletter.show","properties":{"newsletter_type":"userprofile"}}' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Cookie: foo=bar; baz=baz2'""").should.equal()

def test_post_with_string_data():
    # uncurl.parse("""curl 'https://pypi.python.org/pypi/uncurl' --data 'this is just some data'""").should.equal()
    result = api.call("curl http://httpbin.org/post --data 'mystring'").json()
    result.should.have.key('data').which.should.equal('mystring')

def test_parse_curl_with_binary_data():
    pass
    # uncurl.parse("""curl 'https://pypi.python.org/pypi/uncurl' --data-binary 'this is just some data'""").should.equal()

def test_non_ascii():
    pass

def test_curl_version():
    import subprocess as sp
    ver = sp.check_output(['curl','--version']).split()[1]
    assert map(int, ver.split('.')) >= [7,43,0]

def test_response_is_json():
    pass

def test_response_is_null():
    pass

def test_response_errors():
    pass

def test_many_requests_cookies():
    pass

proxy_ip = '107.151.152.211'
proxy_ip_obs = '107.151.152.210'
proxy_port = '80'

def test_proxy_option():
    curl_cmd = 'curl http://httpbin.org/ip '
    curl_cmd += '--proxy "http://{ip}:{port}"'.format(ip = proxy_ip,
                                                      port = proxy_port)
    result = api.call(curl_cmd).json()
    result['origin'].should.equal(proxy_ip_obs)

def test_http_proxy_envvar():
    import os
    os.environ['HTTP_PROXY'] = \
            "http://{ip}:{port}".format(ip = proxy_ip, port = proxy_port)
    result = api.call('curl http://httpbin.org/ip').json()
    result['origin'].should.equal(proxy_ip_obs)

def test_https_proxy_envvar():
    import os
    os.environ['HTTPS_PROXY'] = \
            "https://{ip}:{port}".format(ip = proxy_ip, port = proxy_port)
    result = api.call('curl http://httpbin.org/ip').json()
    result['origin'].should.equal(proxy_ip_obs)

def test_proxy_login():
    pass
