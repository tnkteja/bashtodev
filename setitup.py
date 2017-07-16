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
       
system("rm -rf /tmp/bashtodev/")
