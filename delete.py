import mysql.connector

username=input('enter your registered emailID or phone number:  ')
passwd=input('enter your password:  ')
home=False


try:
    if username.isdigit():
        #print(username)
        usernumber=int(username)
        x2=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
        xx2=x2.cursor()
        xx2.execute('select phone_no from user_info')
        number=[]
        for i in xx2:
            number.append(i[0])        
        if usernumber in number:
            #print(number)
            x3=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
            xx3=x3.cursor()
            xx3.execute(f'select password,aadhar from user_info where phone_no={usernumber}')
            passward=[]
            for i in xx3:
                passward.append(i[0:2])
            z=str(passward[0][1])
            zz=z[4:8]
            passwordd=passwd+zz
            #print(passwordd)
            #print(passward[0])
            if passward[0][0] == passwordd:
                zzz=0
                x7=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                xx7=x7.cursor()
                xx7.execute(f'update user_info set no_of_attempts={zzz} where phone_no={usernumber}')
                x7.commit()
                xx7.close()
                print('successfully logined')
                home=True
            else:
                #print('password is incorrect')
                x5=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                xx5=x5.cursor()
                xx5.execute(f'select no_of_attempts from user_info where phone_no={usernumber}')
                for i in xx5:
                    zz=i[0]+1
                    #print(zz)
                    x6=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                    xx6=x6.cursor()
                    xx6.execute(f'update user_info set no_of_attempts={zz} where phone_no={usernumber}')
                    x6.commit()
                    xx6.close()
                    print('password is incorrect')
                    

        else:
            print('userid doesnot exist check the userid ')
                
                
         

    else:                       
        x=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
        xx=x.cursor()
        xx.execute('select email from user_info')
        mail=[]
        for i in xx:
            mail.append(i[0])
            #print(mail)
        if username in mail:
            #print(username)
            #print(type(username))
            x4=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
            xx4=x4.cursor()
            xx4.execute(f"select password,aadhar from user_info where email=%s",(username,))
            passward=[]
            for i in xx4:
                #print(i)
                passward.append(i[0:2])
                #print(passward)
            z=str(passward[0][1])
            zz=z[4:8]
            passwordd=passwd+zz
            #print(passwordd)
            #print(passward[0])
            if passward[0][0] == passwordd:
                zzzz=0
                x9=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                xx9=x9.cursor()
                xx9.execute(f"update user_info set no_of_attempts={zzzz} where email=%s",(username,))
                x9.commit()
                xx9.close()
                print('successfully logined')
                x12=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                xx12=x12.cursor()
                xx12.execute(f"select phone_no from user_info where email=%s",(username,))
                for i in xx12:
                    username=i[0]
                    home=True
                    #print(i)
                    #print(username)
                    #print(type(username))
                        
            else:
                print('password is incorrect')
                x10=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                xx10=x10.cursor()
                xx10.execute(f"select no_of_attempts from user_info where email=%s",(username,))
                for i in xx10:
                    zz=i[0]+1
                    print(zz)
                    x11=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                    xx11=x11.cursor()
                    xx11.execute(f"update user_info set no_of_attempts=%s where email=%s",(zz,username))
                    x11.commit()
                    xx11.close()
                print('password is incorrect')
                    
                        
                    
        else:
            print('userid doesnot exist check the userid')
            
                    
                            
                    

except:
    print('userid doesnot exist check the userid and password ')

if home:
    def re():
        while True:
            print('enter 1 to delete your account from the bank')
            print('enter 2 to open main menu')
           # print(username)
            x=int(input('enter the number'))
            # print(username)
            if x==1:
                print('are you sure to delete the account from the bank ')
                print('if yes enter 1 or ')
                print('to exit enter 2')
                
                y= int(input('enter the number'))
                if y==1:

                    d=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                    dd=d.cursor()
                    dd.execute(f'select * from user_info where phone_no={username}')
                    user=[]
                    for i in dd:
                        z=i
                    #print(z)
                    for m in range(10):
                        user.append(z[m])
                    #print(user)

                    d1=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                    dd1=d1.cursor()
                    dd1.execute(f'select max(sno) from user_rem')
                    
                    for j in dd1:
                        z=j[0]+1
                    #print(z)
                #    print(user)
                    user.pop(0)
                    user.pop(6)
                    user.pop(7)
                  #  print(user)
                    user.insert(0,z)
                  #  print(user)
                    user.append('delete')
                  #  print(user)

                    d2=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                    dd2=d2.cursor()
                    insert='insert into user_rem (sno,first_name,last_name,phone_no,date_of_birth,aadhar,password,email,status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    data=(user)
                    dd2.execute(insert,data)
                    d2.commit()
                    dd2.close()
                   # print('sp')

                
                    d=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                    dd=d.cursor()
                    dd.execute(f'delete from user_info where phone_no={username}')
                    d.commit()

                    def ex():
                        import Exit
                    ex()

                elif y==2:
                    re()
            
            elif x==2:
                def x():
                    
                    import main
                x()
            else:
                print('invalid input')
    re()

