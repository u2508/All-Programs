# program to illustrate all the functionsof lists
def delete() :
        a=[]
        b=input('enter the list objects without puncuation:-')
        a.extend(b)  
        print('the'.capitalize(),'list is', a)
        c=int(input('enter position of object to be deleted:-'))-1
        del a[c]
        print("deleting".capitalize(),"the item to be deleted.")
        print('after'.capitalize(),'deleting the item to be deleted,the output is',a)
def append():
        a=[] 
        print('the'.capitalize(),'initial list is', a)
        b=input('enter a list object:-')
        a.append(b)  
        print('the'.capitalize(),'list after appending',b,'is', a)
def clear():
        a=[]
        b=input('enter the list objects without puncuation:-')
        for c in b:
                a.append(c)  
        print('the'.capitalize(),'list is', a)
        a.clear()
        print('the'.capitalize(),'list after clearing is',a)
def copy():
        a=[]
        b=input('enter the list objects without puncuation:-')
        for c in b:
                a.append(c)  
        print('the'.capitalize(),'list is', a)
        print('the'.capitalize(),'copy of list is',a.copy())
def count():
        a=[]
        b=input('enter the list objects without puncuation:-')
        for c in b:
                a.append(c)  
        print('the'.capitalize(),'list is', a)
        x=input('element to be found count for:-')
        d=a.count(x)
        print('the'.capitalize(),'count for element',x,'is',d)
def extend():
        a=[]
        b=input('enter the list objects without puncuations:-')
        print('the'.capitalize(),'initial list is', a)
        a.extend(b)  
        print('the'.capitalize(),'list after extending the values is', a)
def pop():
        a=[]
        b=input('enter the list objects without puncuations:-')
        a.extend(b)
        print('the'.capitalize(),'initial list is', a)
        c=int(input('enter position of object to be deleted:-'))-1
        d=a.pop(c)
        print('On using pop function on given list and',d,'was returned and removed from list',a)
def remove():
        a=[]
        b=input('enter the list objects without puncuations:-')
        a.extend(b)
        print('the'.capitalize(),'initial list is', a)
        c=int(input('enter position of object to be deleted:-'))-1
        a.remove(a[c])
        print("removing".capitalize(),"the item to be removed.")
        print('after'.capitalize(),'removing the item to be removed,the output is',a)
def insert():
        a=[]
        b=input('enter the list objects without puncuations:-')
        a.extend(b)
        print('the'.capitalize(),'initial list is', a)
        c=int(input('enter position of object to be inserted:-'))-1
        b=input('Now enter the object to be added using insert function:-')
        a.insert(c,b)
        print("adding".capitalize(),"the object to be added.")
        print('after'.capitalize(),'adding the object to be added,the output is',a)
def sort():
        a=[]
        b=input('enter the list objects without puncuations:-')
        a.extend(b)
        print('the'.capitalize(),'initial list is', a)
        a.sort()
        print("sorting".capitalize(),"the given list.")
        print('after'.capitalize(),'sorting the given list,the output is',a)
def index():
        a=[]
        b=input('enter the list objects without puncuations:-')
        a.extend(b)
        print('the'.capitalize(),'initial list is', a)
        c=input('Now enter the object whose index is to be found:-')
        d=a.index(c)+1
        print("finding".capitalize(),"the index of given object.")
        print('after'.capitalize(),'finding the index of given object,the index of',c,'is',d)
def reverse():
        a=[]
        b=input('enter the list objects without puncuations:-')
        a.extend(b)
        print('the'.capitalize(),'initial list is', a)
        a.reverse()
        print("reversing".capitalize(),"the given list.")
        print('after'.capitalize(),'reversing the given list,the output is',a)
def main():
        a=input('which function of list would you like to learn:-')
        if a=='append':
                append()
        elif a=='clear':
                clear()
        elif a=='copy':
                copy()
        elif a=='count':
                count()
        elif a=='delete':
                delete()
        elif a=='extend':
                extend()
        elif a=='index':
                index()
        elif a=='insert':
                insert()
        elif a=='pop':
                pop()
        elif a=='sort':
                sort()
        elif a=='remove':
                remove()
        elif a=='reverse':
                reverse()
        else:
                print('Invalid response')
main()