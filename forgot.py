import mysql.connector
 

 

def forg():
    global username
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
                print(i[0])
                print(username)

        else:
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
    print(user1)
    if usernumber in user1:
        print(usernumber)
        x2=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
        xx2=x2.cursor()
        xx2.execute(f"select date_of_birth from user_info where phone_no={usernumber}")
        for j in xx2:
            dob1=j[0]
            print(dob1)
            print(dob)
            print(type(dob1))
            print(type(dob))
        if dob1==dob:

            def new():
                new_p=input('enter your new password')
                new_p1=input('reenter your new password')
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
                        print(aa)
                        z=aa[4:8]
                        new_p2=new_p1+z

                        x3=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
                        xx3=x3.cursor()
                        xx3.execute(f"update user_info set password=%s where phone_no={usernumber}",(new_p2,))
                        x3.commit()
                        xx3.close()
                            
                            
                        print('sucessfully password has been changed')
                        print('please login again')
                        import Exit
                            

                    else:
                        print('password should contain one upppercase,lowercase,special charecter and number')
                        new()
                else:
                    print('incorrect password ')
                    new()
            new()
                    
        else:
            print('invalid date of birth try again')
                #import forgot
            forg()
            
    else:
        print('username doesnot exist try again')
            #import forgot
        forg()

forg()
    #def menu():
     #   import main
        

