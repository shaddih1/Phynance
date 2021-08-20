#!/usr/bin/env python3
# -*- coding: utf8 -*-

import argparse
import sys
import os

pythonVersion = sys.version_info
if not pythonVersion.major == 3 and pythonVersion.minor >= 6:
    sys.exit("\nPhynance supports only pyhton3.6 or higher\n")

# local classes
def usage():
    parser = argparse.ArgumentParser(description="Phynance | Finance toolkit")
    parser.add_argument("-q", "--quiet", help="suppress header ", action="store_true")
    parser.add_argument("-l", "--list-options", help="list Phynance options",action="store_true")
    parser.add_argument("-o", "--option", help="set an option to start", metavar="<option>")
#    if len(sys.argv) < 2:
#        phynance = utils.MainMenu()
#        phynance = phynance.start()
    return parser.parse_args()

def main():
    args = usage()
    if len(sys.argv) == 2:
        if args.quiet:
            print("\n[!] Please add more arguments.\n")
    else:
        header = messages.header(args.quiet)
    phynance = orchestra.Conductor()
    if args.list_options:
        phynance.list_options()
    if args.option:
        option = args.option
        phynance.start(option)
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nThanks for using Phynance\n")