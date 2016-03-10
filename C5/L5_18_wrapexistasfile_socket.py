__author__ = 'Hernan Y.Ke'

import os
from socket import socket,AF_INET,SOCK_STREAM

fd = open(os.getcwd()+'\\text2.txt',os.O_WRONLY|os.O_CREAT)
f = open(fd,'wt',closefd=False)