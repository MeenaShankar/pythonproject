lst1=[1,4,6,7,4]
lst2=[1,4,6,4,7,4]
len_lst1=len(lst1)
len_lst2=len(lst2)
c1=0
c2=0
for i in range(0,len_lst1):
    if(lst1[i]==4):
        c1+=1
print("Number of 4 in list1 is:",c1)
for i in range(0,len_lst2):
    if(lst2[i]==4):
        c2+=1
print("Number of 4 in list2 is:",c2)

