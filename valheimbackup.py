import py7zr
import os
import datetime

#get username and chage directory into where valheim saves are located.
user = os.getlogin()
cDate = datetime.datetime.today().strftime ('%d-%b-%y-%H-%M-%S')
os.chdir ('C:/Users/')
os.chdir (user)
os.chdir ('AppData/LocalLow/IronGate/Valheim/')

#detection
bn = os.path.isfile('VALworld.7z')
print('Check to prevent losing data, does VALworld.7z exist here?',bn)
print('Location:',os.getcwd())

#archive valheim save
with py7zr.SevenZipFile('VALworld.7z', 'w') as archive:
        archive.writeall("worlds/")
os.rename(r'VALworld.7z', r'VALworld-' + str(cDate) + '.7z')



#failed attempts dont look here, this is misery and suffering for me :(
"""if bn == True:
    with py7zr.SevenZipFile('VALworld.7z', 'w') as archive:
        archive.writeall("worlds\")
else:
    with py7zr.SevenZipFile('VALworld.7z', 'w') as archive:
        archive.writeall("worlds\")
"""

#Extracting backups.
"""
archive = py7zr.SevenZipFile('test.7z', mode='r')
archive.extractall(path="/")
"""
"""
timeandday = date.today()

time = timeandday.strftime("%b-%d-%y")
print(time)
"""
