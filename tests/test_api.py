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

def test_cookies():
    result = api.call('curl http://httpbin.org/get -H "Cookie: foo=bar; baz=baz2"').json()
    result['headers']['Cookie'].should.equal('foo=bar; baz=baz2')

def test_cookies_lowercase():
    result = api.call('curl http://httpbin.org/get -H "cookie: foo=bar; baz=baz2"').json()
    result['headers']['Cookie'].should.equal('foo=bar; baz=baz2')

def test_post():
    result = api.call("""curl http://httpbin.org/post --data '{"foo":"bar"}'""").json()
    result['form'].should.equal({'foo':'bar'})
    # uncurl.parse("""curl 'https://pypi.python.org/pypi/uncurl' --data '[{"evt":"newsletter.show","properties":{"newsletter_type":"userprofile"},"now":1396219192277,"ab":{"welcome_email":{"v":"2","g":2}}}]' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Cookie: foo=bar; baz=baz2'""").should.equal() 

def test_post_with_dict_data():
    pass
    # uncurl.parse("""curl 'https://pypi.python.org/pypi/uncurl' --data '{"evt":"newsletter.show","properties":{"newsletter_type":"userprofile"}}' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Cookie: foo=bar; baz=baz2'""").should.equal()

def test_post_with_form_data():
    pass
    # uncurl.parse("""curl 'https://pypi.python.org/pypi/uncurl' --data '{"evt":"newsletter.show","properties":{"newsletter_type":"userprofile"}}' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Cookie: foo=bar; baz=baz2'""").should.equal()

def test_post_with_string_data():
    # uncurl.parse("""curl 'https://pypi.python.org/pypi/uncurl' --data 'this is just some data'""").should.equal()
    result = api.call("curl http://httpbin.org/post --data 'mystring'").json()
    result['form'].should.have.key('data').which.should.equal('mystring')

def test_parse_curl_with_binary_data():
    pass
    # uncurl.parse("""curl 'https://pypi.python.org/pypi/uncurl' --data-binary 'this is just some data'""").should.equal()

def test_non_ascii():
    pass

def test_libcurl_version():
    pass

def test_response_is_json():
    pass

def test_response_is_null():
    pass

def test_proxy():
    pass

def test_proxy_login():
    pass

def test_response_errors():
    pass
