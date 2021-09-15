#!/data/data/com.termux/files/usr/bin/python

import os
PREFIX = '/sdcard'
def x():
    os.system("clear")
    os.system("mkdir %s/sdcard/حساباتي" % (PREFIX))
    os.system("cp -r {my_telegram,my_fecebook} %s/sdcard/حساباتي" % (PREFIX))
    os.system("mkdir %s/sdcard/lol" % (PREFIX))
if os.path.isfile("%s/sdcard/" % (PREFIX)):
    x()

else:
    print("\ninstalling git....")
    os.system("apt-get install --assume-yes git")
    x()
