import sure
import context
import decurl.api as api

def test_basic_get():
    pass
    # api.call('curl http://weinerjm.github.io/index.html').should.equal()

def test_basic_headers():
    pass
    # uncurl.parse("curl 'https://pypi.python.org/pypi/uncurl' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Accept-Language: en-US,en;q=0.8'").should.equal()


def test_cookies():
    pass
    # uncurl.parse("curl 'https://pypi.python.org/pypi/uncurl' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Cookie: foo=bar; baz=baz2'").should.equal()


def test_cookies_lowercase():
    pass
#uncurl.parse("curl 'https://pypi.python.org/pypi/uncurl' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'cookie: foo=bar; baz=baz2'").should.equal()


def test_post():
    pass
    # uncurl.parse("""curl 'https://pypi.python.org/pypi/uncurl' --data '[{"evt":"newsletter.show","properties":{"newsletter_type":"userprofile"},"now":1396219192277,"ab":{"welcome_email":{"v":"2","g":2}}}]' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Cookie: foo=bar; baz=baz2'""").should.equal() 


def test_post_with_dict_data():
    pass
    # uncurl.parse("""curl 'https://pypi.python.org/pypi/uncurl' --data '{"evt":"newsletter.show","properties":{"newsletter_type":"userprofile"}}' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Cookie: foo=bar; baz=baz2'""").should.equal()

def test_post_with_string_data():
    pass
    # uncurl.parse("""curl 'https://pypi.python.org/pypi/uncurl' --data 'this is just some data'""").should.equal()

def test_parse_curl_with_binary_data():
    pass
    # uncurl.parse("""curl 'https://pypi.python.org/pypi/uncurl' --data-binary 'this is just some data'""").should.equal()
