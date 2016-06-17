import os, sys, re
import shlex
from .parser import CurlParser
import yaml

def main(fname):
    sys.stdout.write(convert_from_file(fname) + '\n')

def read_config(infile):
    """
    Given a path to a .curlrc file, generates and returns
    a command-line curl statement.
    """
    full_cmd = 'curl '
    
    for line in infile.readlines():
        if len(line.strip()) > 0:
            if line.strip()[0] != '#': # if not comment line
                line = line.strip()
                opt_val = map(lambda x: x.strip(), re.split(r' = ', line))
                if len(opt_val) > 1:
                    opt, val = opt_val
                    val = val.strip('\"')
                else:
                    opt, val = opt_val[0], None
                if opt[0] != '-': # if not shortcut, prefix --
                    opt = '--' + opt
                # append to full command
                full_cmd += '{} '.format(opt)
                full_cmd += '{} '.format(val) if val else ''

    full_cmd = full_cmd.rstrip() # strip right side whitespace

    return full_cmd

def write_config(curl_str):
    parser = CurlParser()
    tokens = shlex.split(curl_str)
    parsed_args = parser.parse_args(tokens)

    result = '# This file was generated by curlio.py\n'

    d = vars(parsed_args)
    empty_vals = [False, None, []]
    no_write = ['command']
    for opt in vars(parsed_args):
        if opt not in no_write and d[opt] not in empty_vals:
            if d[opt]:
                result += '{} = \"{}\"\n'.format(opt, d[opt])
            else:
                result += '{}\n'.format(opt)

    return result

def read_config_yaml(infile):
    """
    Given a path to a configuration YAML file, generates and returns
    a command-line curl statement.
    """
    args_dict = yaml.load(infile.read())

    full_cmd = 'curl'
    for opt, val in args_dict.iteritems():
        if val == True:
            full_cmd += '--{}'.format(opt)
        else:
            full_cmd += ' --{} {}'.format(opt, val)

    return full_cmd

def write_config_yaml(curl_str):
    """
    Given a command-line curl statement, generates a YAML file
    containing a list of all the options and their values.
    """
    parser = CurlParser()
    tokens = shlex.split(curl_str)
    parsed_args = parser.parse_args(tokens)

    d = vars(parsed_args)
    # remove keys with False, None, Empty
    d_clean = {opt: val for opt, val in d.iteritems() if opt != 'command' and val}
    return yaml.dump(d_clean, default_flow_style=False)


if __name__ == '__main__':
    main(sys.argv[1])
