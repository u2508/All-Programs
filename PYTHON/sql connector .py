import mysql.connector as s1
con=s1.connect(host="localhost",user="root",passwd='1900',charset="utf8")
if con.is_connected():
    print("connected....")
else:
    print("oops...")
cur=con.cursor()
#cur.execute("create database ips2;")
cur.execute("use ips2;")
print("you are in database now")
#cur.execute("create table x123 (sno int,name char(20) );")
cur.execute("insert into x123() values(522,'ram'),(20,'bytes') ;")
con.commit( )
x=cur.execute('select sum(sno),name from x123 group by name;')
x=cur.fetchall()
print(x)
