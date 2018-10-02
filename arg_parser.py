import argparse
import pprint
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='Repo updater')
    parser.add_argument('-a', '--all', help='All spk repo will be refreshed', action='store_true' )
    parser.add_argument('-s','--spk', help='Description for foo argument')
    parser.add_argument('-r','--repo', help='Description for bar argument')
    return vars(parser.parse_args())


def main():
    args = parse_args()
    pprint.pprint(args)
    if args["all"]:
        print "refresh all spk repo"
    elif args["spk"] != None and args["repo"] != None:
        print "Refreshing spk {0} and repo {1} after validation".format(args["spk"], args["repo"])
    elif args["spk"] != None and args["repo"] == None:
        print "Refreshing repos of spk {0} after validation".format(args["spk"])
    else:
        help()


def help():
    print " usage :"
    print "--all : all spk repo"
    print "--spk [spk_in_upper]: Refresh all repo under the spk"
    print "--spk [spk] --repo [repo]: refresh the given spk and repo"
    sys.exit(1)


if __name__ == "__main__":
    main()
