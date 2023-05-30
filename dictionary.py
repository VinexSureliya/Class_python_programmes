dict1 = {'key1':10,'key2':20,'key3':30}
print(type(dict1))
print(dict1)
print(dict1['key1'])
print(dict1['key2'])
print(dict1['key3'])
stud1 = {
            'rno':1,
            'stud_name':"Vinex",
            'class':'B.Sc.I.T',
            'sem':5
        }
print(stud1)
print(stud1['rno'])
print(stud1['stud_name'])
print(stud1['class'])
print(stud1['sem'])
for key in stud1:
    print(key,":",stud1[key])
for v in stud1.values():
    print(v)