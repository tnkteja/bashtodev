#!/usr/bin/python
# coding:utf8

from os import environ, system

system("cd /tmp/;\
        git clone https://github.com/tnkteja/bashtodev;cd bashtodev;\
        pip install -r requirements.txt;\
        mkdir -p "+environ["HOME")+"/.bashtodev/")

system("cp /tmp/bashtodev/tools/* $HOME/.bashtodev/;\
        cd $HOME/.bashtodev/;\
        chmod 755 *
       ")
       
bashrcfile=environ("HOME")+"/.bashrc"
bashrccontent=None
with open(bashrcfile,"r") as f:
       bashrccontent=f.read()
with open(bashrcfile,"w") as f:
       f.write(bashrccontent+"\nsource $HOME/.bashtodev/.mybashrc")
       
system("rm -rf /tmp/bashtodev/")
