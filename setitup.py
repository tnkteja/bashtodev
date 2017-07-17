#!/usr/bin/python
# coding:utf8

from os import environ, system
from platform import system as pSystem

system("cd /tmp/;\
        git clone https://github.com/tnkteja/bashtodev;cd bashtodev;\
        pip install -r requirements.txt;\
        mkdir -p "+environ["HOME")+"/.bashtodev/")

system("cp /tmp/bashtodev/tools/* $HOME/.bashtodev/;\
        cd $HOME/.bashtodev/;\
        chmod 755 *
       ")
platform=pSystem()
if platform == "Darwin":
       system(" cd $HOME;\
                if ! [-f ~/.bash_profile]; then cat 'if [ -f ~/.bashrc ]; then . ~/.bashrc; fi' > .bash_profile ; fi'
bashrcfile=environ("HOME")+"/.bashrc"
bashrccontent=None
with open(bashrcfile,"r") as f:
       bashrccontent=f.read()
with open(bashrcfile,"w") as f:
       f.write(bashrccontent+"\nsource $HOME/.bashtodev/.mybashrc")
       
system("rm -rf /tmp/bashtodev/")
