#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
mq=mysql.connector.connect(host="localhost",user="root",passwd="5678")
cursor=mq.cursor()

cursor.execute("create database myportal")
cursor.execute("use myportal")
cursor.execute("create table login_details(username varchar(20) primary key, password char(8), name varchar(20), emailid varchar(35), phoneno bigint)")
    
def signup():
    print("SIGN UP")
    u=input("Create a username: ")
    p=input("Create a password(only 8 characters allowed): ")
    n=input("Enter your name: ")
    e=input("Enter your email id: ")
    m=int(input("Enter your phone no.: "))
    print()
    try:
        cursor.execute("insert into login_details values(%s,%s,%s,%s,%s)",(u,p,n,e,m))
        mq.commit()
    except mysql.connector.IntegrityError:
        print()
        print("Username already exists, please try again")
        u=input("Create another username: ")
        p=input("Create a password(only 8 characters allowed): ")
        n=input("Enter your name: ")
        e=input("Enter your email id: ")
        m=int(input("Enter your phone no.: "))
        print()
        cursor.execute("insert into login_details values(%s,%s,%s,%s,%s)",(u,p,n,e,m))
        mq.commit()
    except mysql.connector.DataError:
        print("Create a password of 8 characters only, please try again")
        u=input("Create a username: ")
        p=input("Create another password(only 8 characters allowed): ")
        n=input("Enter your name: ")
        e=input("Enter your email id: ")
        m=int(input("Enter your phone no.: "))
        print()
        cursor.execute("insert into login_details values(%s,%s,%s,%s,%s)",(u,p,n,e,m))
        mq.commit()
        
    print("Your profile is successfully created.")
    print()
    
def login():
    while True:
        print("LOGIN")
        n=input("Enter your username: ")
        p=input("Enter your password: ")
        cursor.execute("select username from login_details")
        count=0
        c=0
        c1=0
        for x in cursor:
            if n==x[0]:
                count+=1
                
        if count==0:
            print("Incorrect username, please try again")
            print()
            continue

        cursor.execute("select password from login_details ")
        for v in cursor:
            if p==v[0]:
                print("You sucessfully logged in")
                print()
                c+=1
                break
        if c==0:
            print("Incorrect password, please try again")
            f=input("Forgot password y/n: ")
            if f.lower()=="y":
                e=input("Enter your email id: ")
                cursor.execute("select emailid from login_details ")
                for w in cursor:
                    if e==w[0]:
                        c1+=1
                        print("Your Email Id is verified")
                        pa=input("Enter a new password: ")
                if c1==1:
                    cursor.execute("update login_details set password=%s where emailid=%s",(pa,e))
                    mq.commit()
                    print("Password updated")
                    print()
                    break
            else:
                continue
        
def deleteacc():
    print("ACCOUNT DELETION")
    us=input("Enter your username to delete your account permanently: ")
    cursor.execute("delete from login_details where username=%s",(us,))
    mq.commit()
    print("Your account is deleted!! \n")

print("\n")

while True:
    ch=input('''WELCOME TO THE LOGIN PORTAL
---------------------------------
1.Sign up
2.Login
3.Delete a existing account
4.Exit
Enter your choice:''')
    print("\n")
    if(ch=="1"):
        signup()
    elif(ch=="2"):
        login()
    elif(ch=="3"):
        deleteacc()
    elif(ch=="4"):
        print("Exit")
        break
    else:
        print("invalid input")
        print("\n")


# In[ ]:




