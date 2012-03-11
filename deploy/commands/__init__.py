#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Deploy for Humans
    _________________
    
    Mkdir command.
    
    :copyright: (c) 2012 by Jair Gaxiola 
    :license: GPLv3
"""

import os
import requests

from deploy.env import globals

class Mkdir():
    
    def __init__(self, path):
        
        if not os.path.exists(path):
            os.makedirs(path)

class Tar():

    def untar(self, info):
        fullname = "%(name)s-%(version)s" % info
        name = "%(name)s" % info
        version = "%(version)s" % info
        path = globals['store'] + name
        Mkdir(path)
        filename = fullname + '.tar.gz'
        os.system("cd " + path + "; tar -zxvf " + globals['src'] + filename + "; mv " + fullname + " " + version)
		
class Wget():

    def download(self, resource, fullname):

		filename = globals['src'] + "/" + fullname + ".tar.gz"
		source = requests.get(resource)
		Mkdir(globals['src'])
		filesource = open(filename, 'w')
		filesource.write(source.content)
		filesource.close()