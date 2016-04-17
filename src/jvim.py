'''
The MIT License (MIT)

Copyright (c) 2016 Noe De La Cruz, Jr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Created on Apr 16, 2016

@author: Noe

'''
import re
from git import Repo
import sys
from os import path

vimrep = 'https://github.com/vim/vim.git'
msgcontinue = 'To Continue, Enter [Y/y]: '
msgexit = 'Exited at user request!'

def getconf():
    # grab the env from jvim.conf
    cfile = open('jvim.conf')
    # print('this is the file: ' + cfile)
    envars = {}

    for line in cfile:

        marker = '#'

        crline = line.partition(marker)[0]

        if not crline:
            continue

        # check to see if the line has a comment. using regular experssions
        
        line = crline.rstrip()
        line = line.replace(' = ','=')
        cdata = line.split('=')
        
        
        envars[str(cdata[0].lower())] = re.sub('\[|\]|\'', '' , str(cdata[1].lstrip().split(',')))


    return envars

def clonevrep():
    # check to see if clone dir exists if not, clone it


    if path.exists(str(envars['sclone'])):
        ycontinue = raw_input('clone dir:\"%s\", already exists ' %  envars['sclone'] + msgcontinue)
        if ycontinue.lower() == 'y':
            return
        sys.exit(msgexit)
                           
            

    print('cloning to:' + str(envars['sclone']))
    
    Repo.clone_from(vimrep, str(envars['sclone']))


envars = getconf()
clonevrep()


# for key in envars:
#     print key

        

