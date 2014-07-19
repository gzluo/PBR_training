import sys

def read_print_file(filename):
    for line in open(filename):
        print line,
#------END read_print_file--------------------------

def main():
    if len(sys.argv) < 2:
        print >>sys.stderr, "Usage: python %s filename" % sys.argv[0]
        sys.exit(0)
    file = sys.argv[1]
    read_print_file(file)
#--------END main------------------
main()