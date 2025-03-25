#import main.py
import mysql.connector

d=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
dd=d.cursor()
dd.execute(f'delete from user_rem where sno=2')
d.commit()
#dd.close()

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
            print(number)
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
                if zz<6:    
                    x6=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                    xx6=x6.cursor()
                    xx6.execute(f'update user_info set no_of_attempts={zz} where phone_no={usernumber}')
                    x6.commit()
                    xx6.close()
                    print(f'password is incorrect you have more {6-zz} of attempts')
                else:
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
                    user.append('blocked')
                  #  print(user)

                    d2=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                    dd2=d2.cursor()
                    insert='insert into user_rem (sno,first_name,last_name,phone_no,date_of_birth,aadhar,password,email,status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    data=(user)
                    dd2.execute(insert,data)
                    d2.commit()
                    dd2.close()
                    print('please contact bank to unblock')

                
                    d=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                    dd=d.cursor()
                    dd.execute(f'delete from user_info where phone_no={username}')
                    d.commit()

                    def ex():
                        import Exit
                    ex()

                    
                    

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
                if zz<6:
                    x11=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                    xx11=x11.cursor()
                    xx11.execute(f"update user_info set no_of_attempts=%s where email=%s",(zz,username))
                    x11.commit()
                    xx11.close()
                    print(f'password is incorrect there are {6-zz} of attempts')
                else:
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
                    user.append('blocked')
                  #  print(user)

                    d2=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                    dd2=d2.cursor()
                    insert='insert into user_rem (sno,first_name,last_name,phone_no,date_of_birth,aadhar,password,email,status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    data=(user)
                    dd2.execute(insert,data)
                    d2.commit()
                    dd2.close()
                    print('please contact bank to unblock')

                
                    d=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                    dd=d.cursor()
                    dd.execute(f'delete from user_info where phone_no={username}')
                    d.commit()


                    def ex():
                        import Exit
                    ex()

                    
                    
                        
                    
        else:
            print('userid doesnot exist check the userid')
            
                    
                            
                    

except:
    print('userid doesnot exist check the userid and password ')




if home:
    while True:
        print('enter 1 to display balance')
        print('enter 2 to deposite money')
        print('enter 3 to withdrawl money')
        print('enter 4 to transfer money')
        print('enter 5 to transcation history')
        print('enter 6 to go to main menu')
        print()
        x=int(input('enter the number:  '))


        if x==1:
            def balence():
                usernumber=int(username)
                d1=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                dd1=d1.cursor()
                dd1.execute(f'select available_balence from user_tran where phone_no={usernumber}')
                for i in dd1:
                    print(f"the available balaence in your account is { i[0] }" )
            balence()
                
        elif x==2:
            def deposite(a):
                usernumber=int(username)
                d=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                dd=d.cursor()
                dd.execute(f'update user_tran set available_balence=available_balence+{a} where phone_no={usernumber}')
                d.commit()
                dd.close()
                print('sucessdfully added money to your account')
                d1=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                dd1=d1.cursor()
                dd1.execute(f'select available_balence from user_tran where phone_no={usernumber}')
                for i in dd1:
                    print(f'the available balaence in your account is {i[0]}' )
            a=int(input('enter the amount to deposite'))
            deposite(a)

        elif x==3:
            def withdrawl(a):
                usernumber=int(username)
                d2=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                dd2=d2.cursor()
                dd2.execute(f'select available_balence from user_tran where phone_no={usernumber}')
                for i in dd2:
                    z=i[0]
                    if z<a:
                        print('insufficent balence')
                    else:
                        d3=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                        dd3=d3.cursor()
                        dd3.execute(f'update user_tran set available_balence=available_balence-{a} where phone_no={usernumber}')
                        d3.commit()
                        dd3.close()
                        print('sucessdfully withdrawl money from your account')
                        d4=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                        dd4=d4.cursor()
                        dd4.execute(f'select available_balence from user_tran where phone_no={usernumber}')
                        for i in dd4:
                            print(f'the available balaence in your account is {i[0]}' )
                            

            a=int(input('enter the amount to withdrawl'))
            withdrawl(a)

        elif x==4:
            def transfer(a):
                b=input('enter the another user phone_no or emailid to transfer')
                usernumber=int(username)
                print(usernumber)
                print(b.isdigit())
                if not b.isdigit():
                    print(b)
                    x13=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                    xx13=x13.cursor()
                    xx13.execute(f"select phone_no from user_info where email=%s",(b,))
                    for i in xx13:
                        b=i[0]
                        print(type(b))
                        print(b)

                x15=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                xx15=x15.cursor()
                xx15.execute(f"select phone_no from user_info")
                user_p=[]
                for i in xx15:
                    user_p.append(i[0])
                if b in user_p:
                    #usernumber=int(username)
                    d5=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                    dd5=d5.cursor()
                    dd5.execute(f'select available_balence from user_tran where phone_no={usernumber}')
                    for i in dd5:
                        z=i[0]
                        if z<a:
                            print('insufficent balence')
                        else:
                            d6=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                            dd6=d6.cursor()
                            dd6.execute(f'update user_tran set available_balence=available_balence-{a} where phone_no={usernumber}')
                            d6.commit()
                            dd6.close()
                            
                            user2=int(b)
                            d7=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                            dd7=d7.cursor()
                            dd7.execute(f'update user_tran set available_balence=available_balence+{a} where phone_no={user2}')
                            d7.commit()
                            dd7.close()

                            d8=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                            dd8=d8.cursor()
                            dd8.execute(f'select available_balence from user_tran where phone_no={usernumber}')
                            for i in dd8:
                                print(f"the available balaence in your account is { i[0] }" )

                else:
                    print('the entered user emailid or phoneno donot exist in the database')       

            a=int(input('enter the amount to transfer'))
            transfer(a)

        elif x==6:
            def x():
                    
                    
                print('enter 1 to reset your password')
                print('enter 2 to delete your user')
                print('enter 3 to exit')
                print()
                            
                x= int(input("Enter your choice: "))
                                
                if x==1:
                    import forgot
                    
                                        
                elif x==2:
                    import delete
                    
                elif x==3:
                    import Exit
                    
                                        
                else:
                    print('invalid input try again')
            x()
            break



