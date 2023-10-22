import pickle
file1=open(r"D:\vs code\Student.txt","wb")
b="cxcvcx "
for i in range(1):
    b=pickle.dump(b,file1)
    print(b)