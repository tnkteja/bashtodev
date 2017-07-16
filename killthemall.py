#!/usr/bin/python
# coding:utf8

from commands import getoutput
from distutils.util import strtobool
from prompter import yesno

psAEFdump="ps -aef | grep "+raw_input("Enter search string"
print psAEFdump
if yesno("Kill them all ?"):
    for line in commands.getoutput(psAEFdump)).split('\n'):
        getoutput("kill -9 "+line.split()[1])
