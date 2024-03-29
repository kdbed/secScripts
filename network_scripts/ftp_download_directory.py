#!/usr/bin/python3
#
# script to login with ftp, print the directory contents
# and retrieve the files
#
# example: python3 ftp_python.py 8.8.8.8 'user' 'password'

from ftplib import FTP
import sys
import os

ip = str(sys.argv[1])
name = str(sys.argv[2])
pss = str(sys.argv[3])

print('\n')
print('Connecting to '+ip+' through FTP')
print("+++++++++++++++++++++++++++++++")



with FTP(sys.argv[1]) as ftp:
    ftp.login(user=name,passwd=pss)
    print("The current directory is: "+ ftp.pwd())
    ftp.dir()
    filenames = ftp.nlst()
    os.makedirs('./downloads')
    for filename in filenames:
        filedata = open('./downloads/'+filename,'wb')
        ftp.retrbinary('RETR '+filename, filedata.write)
    ftp.close()




