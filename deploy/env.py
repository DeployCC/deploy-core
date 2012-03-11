# -*- coding: utf-8 -*-
import os

global globals

globals = {}
store = '/usr/local/Store/'

if not os.path.exists(store):
    os.makedirs(store)

globals['store'] = store
globals['src'] = store + "src/"
globals['source'] = ''
globals['prefix'] = store