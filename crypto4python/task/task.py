from Crypto.Util.number import *

print('This is your prime:',getPrime(512))
with open('/flag','r') as fp:
    flag=fp.read()
print("flag:",flag)