#! /usr/bin/env python3

service_name_prefix = "user_sshd_"
#image_name = "ubuntu:fullsshd"
image_name = "baseimage:adduser"

import sys
import random
import string

#n = int(input())
#print(n)

if len (sys.argv) < 2:
    exit (1)

n = int (sys.argv[1])
if n < 1 or n > 99:
    exit (2)

#print (n)

# generate passwords
passwords = list()
alphabets = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters
# hack
alphabets = alphabets.replace ('1', '0')
alphabets = alphabets.replace ('l', 'L')
alphabets = alphabets.replace ('$', '%')

for i in range (n):
    word = ""
    for k in range (10):
        word += alphabets [random.randint (0, len (alphabets) - 1)]
    passwords.append (str (word))

#### template ###
# version: '3'
#
# services:
#   user_sshd_00:
#     image: ubuntu:fullsshd
#     ports: 
#       - "20022:22"
#       - "20011:4011"
#     environment:
#       - NEWUSERNAME=ksuser00
#       - NEWPASSWORD=partypeople
#
#   user_sshd_01:
#     image: ubuntu:fullsshd
#     ports: 
#       - "20122:22"
#       - "20111:4011"      
#
#   user_sshd_02:
#     image: ubuntu:fullsshd
#     ports: 
#       - "20222:22"
#       - "20211:4011"      

print ("version: '3'")
print ("")
print ("services:")

for i in range (n):
    print ("  {}{:02}:".format (service_name_prefix, i))
    print ("    image: {}".format (image_name))
    print ("    ports:")
    print ("      - \"2{:02}22:22\"".format (i))
    print ("      - \"2{:02}11:4011\"".format (i))
    print ("    environment:")
    print ("      - NEWUSERNAME=ksuser{:02}".format (i))
    print ("      - NEWPASSWORD={}".format (passwords [i]))
    if i < n - 1:
        print ("")
