import os, platform

 

os.system('git pull')

 

import requests

 

bit = platform.architecture()[0]

 

if bit == '64bit':

 

    print("\033[1;32m[•] \033[1;33mCONGRATULATIONS YOUR DEVICE SUPPORT THE  TOOL\033[1;35m ")

 

    from MANI import Main

 

    Main()

 

elif bit == '32bit':

    print("\033[1;32m[•] \033[1;33mSorry Your Device Not Support This Tool\033[1;35m ")

    

    Main()
