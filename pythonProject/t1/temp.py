'''
generationlist = {'Peter_I':('Alexei','Anna','Elizabeth'),
                      'Alexei':('Peter_II',),
                      'Anna':('Peter_III',),
                      'Peter_III':('Paul_I',),
                      'Paul_I':('Alexander_I','Nicholaus_I')}
curr = {'Peter_I': 0}'''


generationlist ={}
n=int(input('Depth'))
depth=1
x, y = input('Введите родоначальника'), tuple(input('Введите потовком '))
generationlist.update({x: y})
curr={x: y}

while depth<n:
    x , y = input('Введите родителя'), tuple(input('Введите потовком '))
    generationlist.update({x:y})
    depth+=1
depth=0
for k, v in generationlist.items():
    depth=curr[k]
    for it in v:
        curr.update({it : depth+1})

print(curr)
