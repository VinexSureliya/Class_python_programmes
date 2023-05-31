stud1 = {
            'rno':1,
            'stud_name':"Vinex",
            'class':'B.Sc.I.T',
            'sem':5
        }
studants = {
                'stud1': stud1,
                'stud2': {'rno':2,'stud_name':"Vinex",'class':'B.Sc.I.T','sem':5},
                'stud3': {'rno':3,'stud_name':"Vinex",'class':'B.Sc.I.T','sem':5}
           }
print(studants['stud1']['stud_name'])
print(studants['stud2']['rno'])
print(studants['stud3']['class'])