#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
extensions = [ 'html', 'py', 'js' ]
for e in extensions:
    command = 'find -name "*.%s" | xargs git add' % e
    os.system( command )
