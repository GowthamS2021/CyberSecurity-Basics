#!/usr/bin/python3


## flag{b1n42y_s3r2ch_f7w}

import subprocess

def func(st):
       
        string= './script.sh'
        string = string + ' ' + st 
        
        p = subprocess.run(string,capture_output=True,shell=True)
        p1 = subprocess.run("./bruteforcer",input=p.stdout,capture_output=True)
        p2 = subprocess.run("grep high",input=p1.stdout,capture_output=True,shell=True)
        p3 = subprocess.run("grep low",input=p1.stdout,capture_output=True,shell=True)
        
        if p2.stdout != b'' :
            return 'high'
        elif p3.stdout != b'' :
            return 'low'
        else :
            return 'correct'

f = open('wordlist.txt','r')
lower=''
upper='}'
password=''
for x in f :
    if x > lower and x < upper:
        
        if func(x) == 'high' :
            upper = x
            
        elif func(x) == 'low' :
            lower = x
             
        if func(x) == 'correct':
            password = x          
            break

string= './script.sh'
string = string + ' ' + password
p = subprocess.run(string,capture_output=True,shell=True)

p1 = subprocess.run("./bruteforcer",input=p.stdout,capture_output=True )

print(p1.stdout)  

''' contents of script.sh :

#!/bin/bash

echo $1

'''  
