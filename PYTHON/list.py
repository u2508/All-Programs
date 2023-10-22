# program to find maximum marks in each semister
l1=[80,95,56]
l2=[85,87,45]
l3=[89,85,96]
l4=[55,77,85]
l5=[98,67,99]
for i in range(0,3):
    s1=[l1[i],l2[i],l3[i],l4[i],l5[i]]
    maximum= max(s1)
    print('highest marks in semester',i+1,'are',maximum)