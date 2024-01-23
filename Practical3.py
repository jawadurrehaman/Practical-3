fh = open('practical3.txt','w')
import random 
length=15 
i=1 
char_set= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
Password = " " 
while i<=length: 
    Password = Password + random.choice(char_set) 
    i=i+1 
fh.write('Password:'+ str(Password))
fh.close()