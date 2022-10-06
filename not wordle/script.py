#!/usr/bin/python3

# flag{pr377y_5u23_7h15_15_n07_w0rd13} 
import subprocess
import string 
printstr= string.printable
pw=''
count=1

while count <= 30:
    for x in printstr: 
        can_break=False 
             
        p1=subprocess.run(['echo',pw+x],capture_output=True)
        p= subprocess.run('./notwordle',input=p1.stdout,shell=True,capture_output=True)
        string=str(p.stdout)
        num=len(string)
        if count<=9:
            for y in range(num):
                if string[y]==str(count):                               
                    if string[y+1]==' ':
                       pw=pw+x
                       can_break=True
                       break 
        elif count != 30 :
            countstr=str(count)
            for y in range(num):
                if string[y]==countstr[0]:                
                    if string[y+1]==countstr[1]:
                        if string[y+2]==' ':                    
                           pw=pw+x
                           can_break=True
                           break 
        else :
            countstr=str(count)
            for y in range(num):
                if string[y]==countstr[0]:                
                    if string[y+1]==countstr[1]:
                        if string[y+2]==' ':
                            if string[y+3]=='/' :                   
                               pw=pw+x
                               can_break=True
                               break     
        if can_break:
            
            count=count+1
            break

finalpw=subprocess.run(['echo',pw],capture_output=True)    
final=subprocess.run(['./notwordle'],input=finalpw.stdout,capture_output=True)
print(final.stdout)
