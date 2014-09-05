#/bin/env python

import subprocess
import os

def die(msg):
    sys.stderr.write(msg + "\n")
    sys.exit(1)

def p4_build_cmd(cmd):
    """Build a suitable p4 command line.

    This consolidates building and returning a p4 command line into one
    location. It means that hooking into the environment, or other configuration
    can be done more easily.
    """
    real_cmd = ["p4"]

    if isinstance(cmd,basestring):
        real_cmd = ' '.join(real_cmd) + ' ' + cmd
    else:
        real_cmd += cmd
    return real_cmd

def read_pipe_lines(c):
    expand = isinstance(c, basestring)
    p = subprocess.Popen(c, stdout=subprocess.PIPE, shell=expand)
    pipe = p.stdout
    val = pipe.readlines()
    if pipe.close() or p.wait():
        die('Command failed: %s' % str(c))

    return val

def read_pipe(c, ignore_error=False):
    expand = isinstance(c,basestring)
    p = subprocess.Popen(c, stdout=subprocess.PIPE, shell=expand)
    pipe = p.stdout
    val = pipe.read()
    if p.wait() and not ignore_error:
        die('Command failed: %s' % str(c))

    return val

if __name__ == '__main__':
    real_cmd = p4_build_cmd(["describe","-s","101930"])
    #print read_pipe(real_cmd)
    print read_pipe_lines(real_cmd)
