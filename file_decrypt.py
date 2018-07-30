from Crypto.Cipher import AES
from Crypto import Random
import os
import sys
class Encryption:
    def __init__(self,key):
        self.key=key
    
    def pad(self,s):
        return s + "\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, msg,key,key_size=256):
        msg=self.pad(msg)
        iv=Random.new().read(AES.block_size)
        cipher=AES.new(key,AES.MODE_CBC,iv)
        return iv+cipher.encrypt(msg)
    
    def encrypt_file(self,filename):
        with open(filename,'rb') as fp:
            data=fp.read()
        enc=self.encrypt(data,self.key)
        with open(filename+".enc","wb") as fp:
            fp.write(enc)
    def decrypt(self,cipherText,key):
        iv=cipherText[:AES.block_size]
        cipher=AES.new(key,AES.MODE_CBC,iv)
        data=cipher.decrypt(cipherText[AES.block_size:])
        return data.rstrip(b"\0")
    def decrypt_file(self,filename):
        with  open(filename,"rb") as fp:
            cipherText=fp.read()
        dec=self.decrypt(cipherText,self.key)
        with open(filename[:-4],"wb") as fp:
            fp.write(dec)
    
key=b'\xa4\xe4\xfe\xef7\xfe\xab\xd1\x92\x86\xa7\xfc\x9eM\xbe\xeb'
enc=Encryption(key)

enc.decrypt_file(sys.argv[1])
