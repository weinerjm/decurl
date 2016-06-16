from argparse import ArgumentParser

class CurlParser(ArgumentParser):
    def __init__(self): 
        ArgumentParser.__init__(self)
        self.add_argument('command')
        self.add_argument('url')
        self.add_argument('-d', '--data')
        self.add_argument('--data-binary', default=None) # new from uncurl
        self.add_argument('-H', '--header', action='append', default=[])
        self.add_argument('--compressed', action='store_true')
        self.add_argument('-k', '--insecure', action='store_true') # new
        self.add_argument('-b', '--cookie', default=None) # new
        self.add_argument('-c', '--cookie-jar', default=None) # new
        self.add_argument('-L', '--location', action='store_true') # new
        self.add_argument('-x', '--proxy', default=None)
        self.add_argument('-o', '--output', default=None)
        self.add_argument('-K', '--config', nargs='?',
                          const='.curlrc') # new
        self.add_argument('-O','--remote-name', action='store_true') # new
        self.add_argument('--url')
