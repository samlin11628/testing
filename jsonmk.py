import json

print(dir(json))

myinfo = {"name":"sam", "age":40}
jsoninfo = json.dumps(myinfo)
print(type(jsoninfo))
print(jsoninfo)

## json->dict
dictinfo = json.loads(jsoninfo)
print("dictinfo\'s type is {} ".format(type(dictinfo)))


print(dir(dict（))

#


