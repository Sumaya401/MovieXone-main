from django.shortcuts import render
import mysql.connector as Mysql

un = ''
em = ''
db = ''
pwd = ''
# Create your views here.
def SignUp(request):
    global un, em, db, pwd
    if request.method=="POST":
        sql_connection=Mysql.connect(host="localhost",user='root',password='',database='MovieXone')
        cursor = sql_connection.cursor()
        d=request.POST
        for key,value, in d.items():
            if key == "username":
                un = value
            if key == "email":
                em = value
            if key == "dob":
                db = value
            if key == "password":
                pwd = value
        sql_command = "insert into signup values('{}','{}','{}','{}')".format(un,em,db,pwd)           
        cursor.execute(sql_command)
        sql_connection.commit()
    return render(request,'SignUp.html')