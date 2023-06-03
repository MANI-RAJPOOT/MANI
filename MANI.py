import os,platform

os.system('git pull')

MANI=platform.architecture()[0]

if MANI=="32bit":

    print('\033[1;32m [×] \033[1;31mSorry 32Bit Device Not Supported This Tool...!\n\033[1;32m [√] \033[1;33mInshallah Coming Soon...!')

elif MANI=="64bit":

    __import__("MANI")
