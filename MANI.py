












import os,platform

os.system('git pull')

MANI=platform.architecture()[0]

if MANI=="32bit":

	

	__import__("MANI32")

elif MANI=="64bit":

	

    __import__("MANI")
