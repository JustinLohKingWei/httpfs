import argparse
import sys
from .printDebug import printDebug
from .server import server

def main():
    parser=argparse.ArgumentParser(description='httpfs is a simple file server')
    parser.add_argument('-v', action="store_true", help="prints debug messages")
    parser.add_argument('-p', action="store", help="specifies the port number the server will listen and serve at.\n\ndefault is 8080.",type=int)
    parser.add_argument('-d', action="store", help="Specifies the directory that the server will use to read/write requested files. Default is the current directory when launching the application.")
    args = parser.parse_args()
    if args.v:
        printDebug()
    print(args.p)
    print(args.d)
    # parser.add_argument('--input', action='store', type=int, required=True)
    # input = sys.argv[1:]
    # inputString = " ".join(input)
    # print(">"+inputString+"<")
    # if("-v" in inputString):
    #     printDebug()
    # if("-p" in inputString):
    #     server()
    # if("--help" in inputString):
    #     printHelp()


    

if __name__ == '__main__':
    main()