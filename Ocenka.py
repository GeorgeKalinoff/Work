ouf = open('ocenka.txt', 'w')
#-------------Forming List------------
with open('dataset_3363_4 (2).txt') as inf:
    mas=[]
    for line in inf:
        line = line.strip().split(';')
        mas.append(line)
#print(mas)
#print(len(mas))

#------Calculates Avg For Students------
sumMiddle=0
middle=[]
for el in mas:
    sumMiddle=(int(el[1])+int(el[2])+int(el[3]))/3
    middle.append(sumMiddle)
    ouf.write(str(sumMiddle)+'\n')
    print(sumMiddle)
#-----Calculates Avg For Disciplines____________
s=0
for j in range (1,3+1):
    sum=0
    for i in range (0,len(mas)):
        sum +=int(mas[i][j])
    avg=sum/len(mas)
    print(avg, end=' ')
    ouf.write(str(avg)+' ')