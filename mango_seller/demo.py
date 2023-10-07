alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=[]
for i in range(26):
    numbers.append(i+1);

dict1={}


for key in alphabets:
    for value in numbers:
        dict1[key]=value
        numbers.remove(value)
        break

    
print(str(dict1))

name=input('name= ')
abc=0
for i in name:
    get_value=dict1[i]
    abc+=get_value
print(abc)
v1=list(str(abc))

final=0
for i in v1:
    final+=int(i)
print(final) 
    
v2=list(str(final))

final3=0
for i in v2:
    final3+=int(i)
print(final3) 





