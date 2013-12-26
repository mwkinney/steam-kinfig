# steam-kinfig
# This program modifies config files

from sys import exit
from platform import system
from shutil import copy
import os
import xml

# set global constants for directory lookups
# TODO- validate osx installation loc
# TODO- possibly put some variables in the class Directory and inherit them in
        # Configuration
version = ('pre-alpha 13.07')
baseunixdir = os.path.expanduser('~/.steam/steam')
baseosxdir = '/Applications/Steam/Steam.app/Contents/MacOS'
basewindir = r'c:\program files\steam'

class Directory(object):

    # checks the directories looking for the program path
    def look(self):
        if platform.system() == 'Linux' and \
        os.path.isdir(baseunixdir + '/resource/styles'):
            copy
        elif platform.system() == 'Darwin' and \
        os.path.isdir(baseosxdir + '/resource/styles'):
            user_select
        elif platform.system() == 'Windows' and \
        os.path.isdir(basewindir + r'\resource\styles'):
            copywin
        else:
            user_select
   
    # allows for user to point to the program directory manually
    # TODO- feature to implement in v2
    def user_select(self):
        print ('Could not locate your Steam path or identify your OS.\nExiting.')
        exit()

class Configuration(object):

    # this function makes the changes to the file, but doesn't save it
    def modify(self):
        pass

    # copy the files from the path found in look() to the program dir
    # TODO- find a way to use an alter to use this function for all OSs 
    def copy(self):
        shutil.copy(baseunixdir + '/resource/styles/steam.styles', baseunixdir + '/skins')

    # TODO- add code for the ~/Library/Application Support/Steam SkinV4 line in
    # registry.vdf
    def copyosx(self):
        shutil.copy(baseosxdir + r'/resource/styles/steam.styles', baseosxdir + '/skins')

    def copywin(self):
        shutil.copy(basewindir + r'\resource\styles\steam.styles', basewindir + '\skins')

    # reverts the changed file to the original by deleting the skin
    # TODO- windows and osx removal
    def revert(self):
        os.remove(baseunixdir + '/skins/steam.styles')

    # code for the user option selections
    def selections(self):
        print ('steam-kinfig by yenic\n' + version +  '\n\nChoose your selection \
        \n\n1)Popup location\n2)Font-size\n3)Revert any changes\n4)Exit')
        
        tokenDict = {
                '1':popup,
                '2':font,
                '3':revert,
                '4':exit,
                }

        user_input = int(input("> "))
        tokenDict.get(user_input,selections)

    # confirms with user and commits changes to the config
    def commit(self):
        pass

    def popup(self):
        pass

    def font(self):
        pass
