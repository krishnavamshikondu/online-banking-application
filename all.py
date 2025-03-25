from pyfiglet import *
import mysql.connector

main=False
try:
    a='KV BANK'
    x=figlet_format(a)
    print(x)

     
    main=True
     

except:
    print('server busy')

if main:
    def t():
        while True:
            print()
            print()
            print('enter 1 to register for new user')
            print('enter 2 to login for existed user')
            print('enter 3 to reset your password')
            print('enter 4 to delete your user')
            print('enter 5 to exit')
            print()
                
            x= int(input("Enter your choice: "))
            
            if x==1:
                print()
                print('enter 1 if you are already register')
                print('enter 2 to register')
                print()
                z=int(input('enter the number'))
                print()

                if z==2:
                
                    data=[]
                    money=[]

                    def mail(a):
                        b=input('reenter your email id:  ')
                        special=False
                        email=False

                        char='!@#$%^&*()~.,/?;:'

                        x=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                        xx=x.cursor()
                        xx.execute("select email from user_info")
                        mails=[]
                        for i in xx:
                            mails.append(i[0])

                        if b in mails:
                            email=True
                            print()
                            print('this mail is already exist')
                            t()
                            mail(input('enter you mail ID:  '))
                                    
                        for x in a:
                            if x in char:
                                special=True

                                    
                        if not email and special and a==b:
                            data.append(a)
                            money.append(a)
                            print()
                            f_name(input('enter your name:  '))
                                        
                        else:
                            print('invalid mail check the mail ')
                            mail(input('enter you mail ID:  '))
                                            
                                
                    def f_name(a):
                        b=input('reenter your first name:  ')
                        if a==b:
                            data.append(b)
                            print()
                            l_name(input('enter your last name:  '))

                        else:
                            print('name doesnot match please reenter your name')
                            print()
                            f_name(input('enter your name:  '))

                    def l_name(a):
                        b=input('reenter your last name:  ')
                        if a==b:
                            data.append(b)
                            print()
                            number(int(input('enter your number:  ')))      
                        else:
                            print('the last name doesnot match please reenter')
                            print()
                            l_name(input('enter your last name:  '))

                                        
                    def number(a):
                        b=int(input('reenter your phone number:  '))
                        if a==b and len(str(a))==10 :
                            data.append(b)
                            money.append(b)
                            print()
                            dob(input('enter your date of birth DD/MM/YYYY:  '))

                        else:
                            print('please check the number ')
                            print()
                            number(int(input('enter your number')))
                                        
                    def dob(a):
                        b=input('reenter your date of birth DD/MM/YYYY:  ')
                        if a==b:
                            data.append(b)
                            print()
                            aadhar(int(input('enter the aadhar number:  ')))

                        else:
                            print('please recheck your date of birth')
                            print()
                            dob(input('enter your date of birth DD/MM/YYYY:  '))
                                        
                    def aadhar(a):
                        b=int(input('reenter the aadhar number:  '))
                        if a==b and len(str(a))==12 :
                            data.append(b)
                            print()
                            print('PASSWORD SHOULD HAVE')
                            print('number,uppercase,lowercase,special charecter and 8 letters')
                            print()
                            password(input('enter the password:  '))
                        else:
                            print('aadhar number doesnt match try again')
                            print()
                            aadhar(int(input('enter the aadhar number:  ')))
                                            
                    def password(a):
                        b=input('reenter the password')
                        print()
                        upper= False
                        lower= False
                        digit= False
                        special= False
                        print()

                        char='!@#$%^&*()~.,/?;:'

                        for ch in b:

                            if ch.isupper():
                                upper=True
                            elif ch.islower():
                                lower=True
                            elif ch.isdigit():
                                digit=True
                            elif ch in char:
                                special=True
                        if upper and lower and digit and special and a==b :
                            x=str(data[5])  #salt ante user ki thelikunda password lo few numbwers
                            #print(x)        add chesam to get morw safty 
                            z=x[4:8]
                            #print(z)       manam user addhar lo unde 5-8 numbers ni salt la pettam
                            y=b+z
                            #print(y)
                            data.append(y)
                            print()
                            sno()
                                        
                        else:
                            print('password doesnt match try again')
                            print()
                            password(input('enter the password:  '))



                    def sno():
                        z=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                        zz=z.cursor()
                        zz.execute('select max(sno) from user_info ')
                        for i in zz:
                            print(i[0])
                            m=i[0]+1
                            data.append(m)
                            money.append(m)
                            deposit()

                    def deposit():
                        dep=int(input('to create account you need to deposit min 1000 rs/-'))
                        if dep>=1000 :
                            money.append(dep)
                            print()
                            print('your successfully registered to kv bank')
                                    
                                    
                            no_of_attempt=0
                            data.append(no_of_attempt)
                            #print(data)
                            xx=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                            xxx=xx.cursor()
                            insert='insert into user_info (email,first_name,last_name,phone_no,date_of_birth,aadhar,password,sno,no_of_attempts) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                            values=(data)
                            xxx.execute(insert,values)
                            xx.commit()
                            xx.close()

                            #print(money)
                            xx2=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                            xxx2=xx2.cursor()
                            insert2='insert into user_tran (email,phone_no,sno,available_balence) values(%s,%s,%s,%s)'
                            values2=(money)
                            xxx2.execute(insert2,values2)
                            xx2.commit()
                            xx2.close()
                            print()
                            print()
                            print()

                        else:
                            print('invalid input try again')
                            print()
                            deposit()
                                    
                    mail(input('enter your email id:  '))
                elif z==1:
                    continue


     
            elif x==2:
                 
                
                d=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                dd=d.cursor()
                dd.execute(f'delete from user_rem where sno=2')
                d.commit()
                #dd.close()

                username=input('enter your registered emailID or phone number:  ')
                passwd=input('enter your password:  ')
                print()
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
                            #--print(number)
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
                                elif zz>=6:
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
                                   #--- print(zz)
                                if zz<6:
                                    x11=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                                    xx11=x11.cursor()
                                    xx11.execute(f"update user_info set no_of_attempts=%s where email=%s",(zz,username))
                                    x11.commit()
                                    xx11.close()
                                    print(f'password is incorrect there are {6-zz} of attempts')
                                #print(zz)
                                else :
                                   #-- print(zz)
                                   #-- print(username)
                                    d=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                                    dd=d.cursor()
                                    dd.execute(f'select * from user_info where email=%s',(username,))
                                    user=[]
                                    for i in dd:
                                        z=i
                                   #-- print(z)
                                    for m in range(10):
                                        user.append(z[m])
                                   #-- print(user)

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
                                   #-- print(user)

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
                                    dd.execute(f'delete from user_info where email=%s',(username,))
                                    d.commit()


                                    
                                    
                                        
                                    
                        else:
                            print('userid doesnot exist check the userid')
                            
                                    
                                            
                                    

                except:
                    print('userid doesnot exist check the userid and password ')




                if home:
                    while True:
                        print()
                        print()
                        print('enter 1 to display balance')
                        print('enter 2 to deposite money')
                        print('enter 3 to withdrawl money')
                        print('enter 4 to transfer money')
                        print('enter 5 to transcation history')
                        print('enter 6 to go to main menu')
                        print()
                        print()
                        x=int(input('enter the number:  '))
                        print()


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
                                    print()
                                    print()
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
                                        print()
                                        print()
                                        print('insufficent balence')
                                    else:
                                        d3=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                                        dd3=d3.cursor()
                                        dd3.execute(f'update user_tran set available_balence=available_balence-{a} where phone_no={usernumber}')
                                        d3.commit()
                                        dd3.close()
                                        print('sucessfully withdrawl money from your account')
                                        d4=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                                        dd4=d4.cursor()
                                        dd4.execute(f'select available_balence from user_tran where phone_no={usernumber}')
                                        for i in dd4:
                                            print(f'the available balaence in your account is {i[0]}' )
                                            print()
                                            print()
                                            

                            a=int(input('enter the amount to withdrawl'))
                            withdrawl(a)

                        elif x==4:
                            def transfer(a):
                                b=input('enter the another user phone_no or emailid to transfer')
                                usernumber=int(username)
                               #-- print(usernumber)
                               #-- print(b.isdigit())
                                if not b.isdigit():
                                   #--  print(b)
                                    x13=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                                    xx13=x13.cursor()
                                    xx13.execute(f"select phone_no from user_info where email=%s",(b,))
                                    for i in xx13:
                                        b=i[0]
                                        #--print(type(b))
                                        #--print(b)

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
                                            print()
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
                                                print()
                                                print()

                                else:
                                    print('the entered user emailid or phoneno donot exist in the database')
                                    print()
                        
                            a=int(input('enter the amount to transfer'))
                            transfer(a)

                        elif x==6:
                            break
                            
            elif x==3:
                
                def forg():
                    global username
                    print()
                    print()
                    username=input('enter your email or phone no')
                    dob= input('enter your date of birth in dd/mm/yyyy')

                        #if not username.isdigit():
                    def user_t():
                        global username
                        x0=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                        xx0=x0.cursor()
                        xx0.execute("select email from user_info")
                        user0=[]
                        for x in xx0:
                            user0.append(x[0])
                        print(user0)
                        if username in user0:
                            x=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                            xx=x.cursor()
                            xx.execute("select phone_no from user_info where email=%s",(username,))
                            
                            for i in xx:
                                username=i[0]
                                #--print(i[0])
                                #--print(username)

                        else:
                            print()
                            print('invalid username try again')
                            #import forgot
                            forg()

                    if not username.isdigit():
                        user_t()

                    usernumber=int(username)
                    x1=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                    xx1=x1.cursor()
                    xx1.execute("select phone_no from user_info")
                    user1=[]
                    for i in xx1:
                        user1.append(i[0])
                   #-- print(user1)
                    if usernumber in user1:
                    #--    print(usernumber)
                        x2=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                        xx2=x2.cursor()
                        xx2.execute(f"select date_of_birth from user_info where phone_no={usernumber}")
                        for j in xx2:
                            dob1=j[0]
                           #-- print(dob1)
                          #--  print(dob)
                          #--  print(type(dob1))
                           #-- print(type(dob))
                        if dob1==dob:

                            def new():
                                print()
                                print()
                                new_p=input('enter your new password')
                                new_p1=input('reenter your new password')
                                print()
                                print()
                                if new_p == new_p1:
                                    special=False
                                    number= False
                                    lower= False
                                    upper=False

                                    char='~!@#$%^&*()_-+=.,;/?<>'
                                    for i in new_p:
                                        if i in char:
                                            special=True
                                        elif i.isupper():
                                            upper=True
                                        elif i.islower():
                                            lower=True
                                        elif i.isdigit():
                                            number=True
                                    if special and number and lower and upper:  
                                            

                                        x4=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                                        xx4=x4.cursor()
                                        xx4.execute(f"select aadhar from user_info where phone_no={usernumber}")
                                            
                                        for k in xx4:
                                            aa=str(k[0])
                                       #-- print(aa)
                                        z=aa[4:8]
                                        new_p2=new_p1+z

                                        x3=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                                        xx3=x3.cursor()
                                        xx3.execute(f"update user_info set password=%s where phone_no={usernumber}",(new_p2,))
                                        x3.commit()
                                        xx3.close()
                                            
                                            
                                        print('sucessfully password has been changed')
                                        print('please login again')
                                        #import Exit
                                        print()
                                        print()
                                            

                                    else:
                                        print()
                                        print('password should contain one upppercase,lowercase,special charecter and number')
                                        new()
                                        print()
                                else:
                                    print()
                                    print('incorrect password ')
                                    new()
                            new()
                                    
                        else:
                            print()
                            print('invalid date of birth try again')
                                #import forgot
                            forg()
                            
                    else:
                        print()
                        print('username doesnot exist try again')
                            #import forgot
                        forg()

                forg()
                            
            elif x==4:
                
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
                                print()
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
                                    print()
                                    print('password is incorrect')
                                    

                        else:
                            print()
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
                                print()
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
                                  #--  print(zz)
                                    x11=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                                    xx11=x11.cursor()
                                    xx11.execute(f"update user_info set no_of_attempts=%s where email=%s",(zz,username))
                                    x11.commit()
                                    xx11.close()
                                print()
                                print('password is incorrect')
                                    
                                        
                                    
                        else:
                            print()
                            print('userid doesnot exist check the userid')
                            
                                    
                                            
                                    

                except:
                    print()
                    print('userid doesnot exist check the userid and password ')
              
                if home:
                    def re():
                    
                        while True:
                            print('enter 1 to delete your account from the bank')
                            print('enter 2 to open main menu')
                           # print(username)
                            print()
                            x=int(input('enter the number'))
                            # print(username)
                            if x==1:
                                print('are you sure to delete the account from the bank ')
                                print('if yes enter 1 or ')
                                print('to exit enter 2')
                                print()
                                
                                y= int(input('enter the number'))
                                print()
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

                                    print()
                                    print()
                                    print('sucessfully deletes')

     
                                elif y==2:
                                    re()
                            
                            elif x==2:
                                break
                            else:
                                print()
                                print('invalid input')
                    re()
     
            elif x==5:
                                
                a='Thank you'
                x=figlet_format(a)
                print(x)
                print('                                                  form KV BANK')


                break
                            
            else:
                print('invalid input try again')
    t()
