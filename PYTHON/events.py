import datetime
a=datetime.date.today()
b=a.strftime('%dth %B %Y')
c=slice(0,11)
d=b[c]
print('the '.capitalize(),'date today is',b)
if d=='06th August':
    print('happy birthday Tanu didi'.capitalize())
elif d=='12th August':
    print('happy birthday Utkarsh'.capitalize())
elif d=='24th August':
    print('happy birthday Shaan bhaiya'.capitalize())
elif d=='15th August':
    print('happy independence day'.capitalize())
elif d=='26th January':
    print('happy republic day'.capitalize())
elif d=='12th May 20':
    print('happy birthday mama'.capitalize())
elif d=='25th March ':
    print('happy birthday vatsal'.capitalize())
elif d=='10th June 2':
    print('happy birthday gaurangi'.capitalize())
elif d=='21th June 2':
    print('happy wedding aniversary papa mummi'.capitalize())
elif d=='01th April ':
    print('happy april fool'.capitalize())
elif d=='11th August':
    print('happy birthday Utkarsh mama'.capitalize())
    print('happy wedding aniversary Utkarsh mama (court marrige)'.capitalize())
elif d=='19th Septem':
    print('happy birthday aditi'.capitalize())
elif d=='05th Septem':
    print("happy teacher's day".capitalize())
elif d=='19th Novem':
    print('happy birthday Parnika'.capitalize())
elif d=='14th Novem':
    print("happy Children's day".capitalize())
elif d=='13th Decem':
    print('happy birthday mummi'.capitalize())
elif d=='25th Decem':
    print('merry christmas'.capitalize())
elif d=='31th Decem':
    print('happy new year eve'.capitalize())
elif d=='01th Januar':
    print('happy new year'.capitalize())
elif d=='20th May':
    print('happy birthday rudraksh'.capitalize())
else :
    print('no new events have been added for this day')   
    
    
    
    