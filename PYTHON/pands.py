import pandas as pd

a = [1, 7, 2]

myvar = pd.DataFrame({"numbers":a})
myvar["name"]=['Anuskha','Utkarsh',"Anu"]
myvar["relation"]=["love","myself","sister"]
myvar.drop("relation",axis=1,inplace=True)
n=pd.DataFrame({"numbers":[11],"name":"raj"})
myvar=pd.concat([n,myvar]).reset_index(drop=True)
print(myvar,file=open("a.csv","w+"))