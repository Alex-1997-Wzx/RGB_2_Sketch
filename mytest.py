string=r'C:\Users\Alex\Desktop\Python_Notes\img_recog'
s=string.replace('\\','/')
#print(s)

def fun():
    return 2,3
li=[]
result=fun()
li+=result
li.append(result)
print(result)
print(li)