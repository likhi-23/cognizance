rec=[]

rec.append([1,'Likhith',99])
rec.append([2,'George',27])
rec.append([3,'Agarwal',83])
rec.append([4,'Raj',42])

print("Records in the list:")

for a in range(len(rec)):
    for b in range(len(rec[a])):
        print(rec[a][b],end="\t")
    print()
    print("\nSecond record in the list:")
#Printing the Second Record from the list

for b in range(len(rec[1])):
    print(rec[1][b],end="\t")


