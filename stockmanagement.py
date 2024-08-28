import mysql.connector
print("""
__________________________________
WELCOME TO STOCK MANAGEMENT SYSTEM
__________________________________
""")
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists sales")
mycursor.execute("use sales")
mycursor.execute("create table if not exists login(username varchar(25) not null,password varchar(25) not null)")
mycursor.execute("create table if not exists purchase(odate date not null,name varchar(25) not null,pcode int not null)")
mycursor.execute("create table if not exists stock(pcode int not null,pname varchar(25) not null,quantity int not null,price int not null)")
mydb.commit()
z=0
mycursor.execute("select * from login")
for i in mycursor:
    z+=1
if z==0:
    mycursor.execute("insert into login values('username','shiv')")
    mydb.commit()
while True:
    print("""
1. Admin
2.Exit
""")
    ch=int(input("Enter your choice from the above options"))
    if ch==1:
        passw=input("Enter password")
        mycursor.execute("select * from login")
        for i in mycursor:
            username,password=i
        if passw==password:
            print("LOGIN SUCESSFUL!!")
            print("""
1. Add New Item
2. Updating price
3. Deleting Item
4. Display All Items
5. To Change the Password
6. Log Out
""")
            ch=int(input("Enter your choice:"))
            if ch==1:
                pcode=int(input("Please enter product code-->"))
                pname=input("Please enter product name-->")
                quantity=int(input("Please enter product quantity-->"))
                price=int(input("Please enter product price-->"))
                st="insert into stock(pcode,pname,quantity,price) values({},'{}',{},{})".format(pcode,pname,quantity,price)
                mycursor.execute(st)
                mydb.commit()
                print("Record Successfully Inserted...!!")
            elif ch==2:
                pcode=int(input("Enter the product code-->"))
                new_price=int(input("Enter new price-->"))
                mycursor.execute("update stock set price={} where pcode={}".format(new_price,pcode))
                mydb.commit()
                print("Sucessfully Updated...!!")
            elif ch==3:
                pcode=int(input("Enter the product code-->"))
                mycursor.execute("delete from stock where pcode={}".format(pcode))
                mydb.commit()
                print("Sucessfully deleted...!!")
            elif ch==4:
                mycursor.execute("select * from stock")
                data=mycursor.fetchall()
                print(data)
            elif ch==5:
                old_password=input("Enter your old password")
                new_password=input("Enter your new password")
                mycursor.execute("select * from login")
                for i in mycursor:
                    username,password=i
                if old_password==password:
                    mycursor.execute("update login set password={}".format(new_password))
                    mydb.commit()
                else:
                    print("You have entered wrong old password")
            elif ch==6:
                break
            
        else:
            print("""
INVALID CREDENTIALS...
PLEASE TRY AGAIN LATER :)
""")
    elif ch==2:
        break
            
