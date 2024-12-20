# import required module
from zipfile import ZipFile
#specify the file name
file_name = "secret.zip"
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()



import itertools
alphabets = ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5']
f = open("dict.txt", "w")
for passlen in [6]:
    combinations = itertools.product(alphabets, repeat = passlen)
    for combination in combinations:
        f.write(''.join(combination)+"\n")


import zipfile
cracked = False
z = zipfile.ZipFile("secret.zip")
with open("dict.txt") as f:
    lines = f.readlines()
for password in lines:
    password = password.replace('\n','')
    try:
        z.extractall(pwd=bytes(password, 'utf-8'))
        correct_password = 'Correct password: %s' % password
        cracked = True
        break
    except:
        pass

if cracked:
    print(correct_password)
else:
    print("Password not found")




import zipfile
z = zipfile.ZipFile("secret.zip")
files = z.namelist()
passw = 'b1c1e5'
z.setpassword(bytes(passw, 'utf-8'))
print(z.namelist())
z.extractall()
z.close()
for extracted_file in files:
    print("File name:"+extracted_file+"\n\nContent:")
    with open(extracted_file) as f:
        content = f.readlines()
        print(''.join(content))
        print('\n\n')
