from django.shortcuts import render
import mysql.connector as Mysql

un = ''
pwd = ''
# Create your views here.
def Login(request):
    global un, pwd
    if request.method=="POST":
        sql_connection=Mysql.connect(host="localhost",user='root',password='',database='MovieXone')
        cursor = sql_connection.cursor()
        d=request.POST
        for key,value, in d.items():
            if key == "username":
                un = value
            if key == "password":
                pwd = value
        sql_command = "select * from signup where name ='{}' and passcode = '{}'".format(un,pwd)
        cursor.execute(sql_command)
        tup = tuple(cursor.fetchall())
        if tup != ():
            return render(request, 'Main.html')
        if tup == ():
            return render(request, 'WrongPass.html')
    return render(request,'Login.html')