from argparse import ArgumentParser
import os, sys, re

class CurlParser(ArgumentParser):
    """ArgumentParser-based parser for curl options"""
    def __init__(self): 
        ArgumentParser.__init__(self)
        self.add_argument('command')
        self.add_argument('url', nargs='?')
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

def sub_env_vars(command):
    pattern = r'\$\{[A-Za-z0-9]+\}'
    env_vars = re.findall(pattern, command)
    if len(env_vars) > 0:
        command_split = re.split(pattern, command)
        for idx, ev in enumerate(map(lambda x: x.strip('${}'), env_vars)):
            command_split.insert(idx+1, os.environ[ev])

        return ''.join(command_split) # reassemble
    else:
        return command
