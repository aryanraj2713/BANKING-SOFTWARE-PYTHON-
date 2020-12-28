"""
Created on Sat Nov 21 10:17:15 2020

@author: Aryan Raj
"""
import mysql.connector
print("WELCOME TO OUR BANK-ARYAN RAJ, HARSH KUMAR & NIKHIL RAJ")
a=str(input("enter  mysql password of"))

mydb=mysql.connector.connect(host="localhost",user="root",passwd=a)
mycursor=mydb.cursor()
mycursor.execute("create database if not exists bank")
mycursor.execute("use bank")
 
mycursor.execute("create table if not exists bank_master(acno char(4) primary key,name varchar(30),city char(20),mobileno char(10),balance int(6))")
mycursor.execute("create table if not exists banktrans(acno char (4),amount int(6),dot date,ttype char(1),foreign key (acno) references bank_master(acno))")
mydb.commit()
while(True):
     
    print("1=Create account")
    print("2=Deposit money")
    print("3=Withdraw money")
    print("4=Display account")
    print("5=Exit")
    k=int(input("Enter your choice:"))
    
    if(k==1):
        print("All information prompted are mandatory to be filled")
        acno=str(input("Enter account number(4 digits allowed):"))
        name=input("Enter name(limit 35 characters):")
        city=str(input("Enter city name:"))
        mn=str(input("Enter mobile no.:"))
        balance=0
        mycursor.execute("insert into bank_master values('"+acno+"','"+name+"','"+city+"','"+mn+"','"+str(balance)+"')")
        mydb.commit()
        print("Account is successfully created")
    elif(k==2):
        acno=str(input("Enter account number:"))
        dp=int(input("Enter amount to be deposited:"))
        dot=str(input("Enter date of Transaction: YYYY-MM-DD "))
        ttype="d"
        mycursor.execute("insert into banktrans values('"+acno+"','"+str(dp)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update bank_master set balance=balance+'"+str(dp)+"' where acno='"+acno+"'")
        mydb.commit()
        print("money has been deposited successully!!!")
    elif(k==3):
        acno=str(input("Enter account number:"))
        wd=int(input("Enter amount to be withdrawn:"))
        dot=str(input("enter date of transaction: YYYY-MM-DD "))
        ttype="w"
        mycursor.execute("insert into banktrans values('"+acno+"','"+str(wd)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update bank_master set balance=balance-'"+str(wd)+"' where acno='"+acno+"'")
        mydb.commit()
    elif(k==4):
        acno=str(input("Enter account number:"))
        mycursor.execute("select * from bank_master where acno='"+acno+"'")
        for i in mycursor:
            print(i)
    else:
        break



