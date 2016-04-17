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
import jvim


# Jody needs wants ot have a hand at creating a custom python vim ide. 
# he modify's the included jvim.conf file to include the options and features he wants his vim to have
assert 'git.exe' in jvim.envars['gitexe']

# he runs that app which takes him through every step of compiling the vim for windows

# He sees the instructions for using the finished prduct to include creatng the directory and copying 
# the file over to the appropriate directory, which the app check for the existance of and implements 
# if it does not exist. 

# the app askes the user if he wants to install the addons that he prefers to vim
# the app installs the desired apps frome the vimrc located on githup, the location 
# provided to the app by Jody

# the apps clones and copies over the necessary file to the required location in jody's users directory
# The apps fuctions differently if it detect that it is being run from a linux system
