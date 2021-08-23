#! -*- coding: utf8 -*-

import os

def getDir():
    get_dir = home_dir = os.path.expanduser("~")
    return get_dir

get_dir = getDir()

# messages 
def argumentMessage():
    message = f'''\n┌──[Phynance]─[{get_dir}]
└──╼ $'''
    return message

def header(quiet):
    if not quiet:
        print(f'''╔═╗┬ ┬┬ ┬┌┐┌┌─┐┌┐┌┌─┐┌─┐
╠═╝├─┤└┬┘│││├─┤││││  ├┤ 
╩  ┴ ┴ ┴ ┘└┘┴ ┴┘└┘└─┘└─┘by Shady
  Made with <3 | Tools''')

