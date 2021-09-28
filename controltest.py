# if ----------
score = 60

students = {"Sam":100, "York":80, "Kevin":60, "Mike":30}

for who in students.keys():
    print(who)
#who = "Kevin"
    if students[who] > score:
        print("passed")
    elif students[who] == score:
        print("just passed")
    else:
        print("failed")


#while----------
a = 11
while a>=10 :
    for i in range(100) :
        print(i)
        if i == 5 :
            a = i
            print(a)


#  break/continue ----------
for i in range(10) :
    if i == 5:
        break
    else:
        print(i)

for i in range(10):
    if i==5:
        continue
    else:
        print(i)


#  iterable ------------

from collections import Iterable
#import Iterable
num = 456
print(isinstance(num, Iterable))

num1=[1,2,3]
print(isinstance(num1, Iterable))


# enumerate -------------
names = ['z', 'aa', 'b']
print ("here--------------")
print(names)
print ("but--------------")
print(enumerate(names).next())
print(type(enumerate(names)))


print("----------------")
for i,value in enumerate(names):
    print(i,value)






#for name,age in [["Sam","40]",["York","39"]]:
  #  print(name,age)

#for name,age in {"Sam":40, "York":39}:
#    print(name,age)



# list derived formula-------
print([x for x in range(5)])

numlist=[]
for x in range(5):
    numlist.append(x)

print(numlist)
