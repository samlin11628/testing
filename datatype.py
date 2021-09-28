str1 = "Hello World!"
str2 = '''aaa\raa    '''
str3 = r"bbb\?bb"
str4 = r'''   cc
ccccc  '''

name = "  abcdefg abc  123  "
age = 10

str5 = str(age)
print(type(age))
print(type(str5))

print ("name is %s,   age is %d" %(name, age))
print ("name is {0},   age is {1},     name is {2}.".format(name,age,name))

print(str1, str2,str3, str4, age)
print ("str1 = "+str1)
print ("str2 = "+str2)
print ("str3 = "+str3)
print ("str4 = "+str4)

print(name.capitalize())
print(name.encode(encoding="UTF-8"))
print(name.index('''b'''))

print(name.__add__("zz"))


# list--------------
a = []
print(type(a))

numlist = [1,2,3,4,5,6]
strlist = ["a","b","c","d"]

print(numlist, strlist)

print(numlist[3], strlist[2])
print(numlist[:5])
print(strlist[2:])

# Build-in functions

# Tuple ----------
test1 = (1,2,3,4,5,6)
test2 = ("a","b","c")   #
test3 = ([1,2,3],"aa")
test3[0].append(45)

# dict----------------
dict1 = {"name":"Sam", "age":40, "job":"it"}
print(type(dict1))
print(dict1['age'])


students = ["aa", "bb", "cc"]
newstudent = "dd"
students.append(newstudent)
print("students are %s" %(students,))

studenttemp = students
morestudents = ["ee","ff","gg"]
studenttemp.append(morestudents)
print("Appending students are %s" %(studenttemp,))
students.extend(morestudents)
print("Extending students are %s" %(students,))




print("-------------")
print(dir(dict))
print("-------------")
print(dir(list))
print("-------------")
print(dir(tuple))
