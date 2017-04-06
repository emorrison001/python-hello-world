import sys

def hello(argv=None):
    if argv is None:
        argv = sys.argv

    print "Hello, world"

    return 0
