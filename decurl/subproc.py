import subprocess as sp 
import sys, shlex
import .curlio as cc

def main(curl_cmd):
    curl_twice(curl_cmd)

def curl_twice(curl_cmd):
    print curl_cmd
    try:
        sp.check_call(shlex.split(curl_cmd))
    except sp.CalledProcessError as e:
        print "command {} exited with status {}".format(curl_cmd,
                                                        e.returncode)

    CONFIG_FILE = 'config_file.txt'
    # write a config file
    with open(CONFIG_FILE,'w') as outf:
        outf.write(cc.write_config(curl_cmd))

    # read back in
    try:
        curl_read_cmd = cc.read_config(CONFIG_FILE)
        sp.check_call(shlex.split(curl_read_cmd))
    except sp.CalledProcessError as e:
        print "command {} exited with status {}".format(curl_read_cmd,
                                                        e.returncode)

if __name__ == "__main__":
    main(sys.argv[1])
