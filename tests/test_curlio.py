import sure
import context
import decurl.curlio as curlio

def test_write_config():
    to_write = curlio.write_config('curl --url http://httpbin.org/get')
    pass

def test_read_config(): 
    pass
