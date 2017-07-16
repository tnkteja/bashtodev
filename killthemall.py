#!/usr/bin/python
# coding:utf8

from commands import getoutput
from distutils.util import strtobool
from prompter import yesno

psAEFdump=getoutput("ps -aef | grep "+raw_input("Enter search string"))
print psAEFdump

if yesno("Kill them all ?"):
    for line in psAEFdump.split('\n'):
        getoutput("kill -9 "+line.split()[1])
