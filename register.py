
import mysql.connector
#import app.py
#import random
#import smtplib
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
'''
try:
    a='KV BANK'
    x=figlet_format(a)
    print(x)


    while True:
        print('enter 1 to register for new user')
        print('enter 2 to login for existed user')
        print('enter 3 to reset your password')
        print('enter 4 to exit')
        print()
        x=int(input('enter the number:  '))

        if x==1:
    '''

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
        print('this mail is already exist')
        mail(input('enter you mail ID:  '))
                
    for x in a:
        if x in char:
            special=True

                
    if not email and special and a==b:
        data.append(a)
        money.append(a)
        f_name(input('enter your name:  '))
                    
    else:
        print('invalid mail check the mail ')
        mail(input('enter you mail ID:  '))
                        
            
def f_name(a):
    b=input('reenter your first name:  ')
    if a==b:
        data.append(b)
        l_name(input('enter your last name:  '))

    else:
        print('name doesnot match please reenter your name')
        f_name(input('enter your name:  '))

def l_name(a):
    b=input('reenter your last name:  ')
    if a==b:
        data.append(b)
        number(int(input('enter your number:  ')))      
    else:
        print('the last name doesnot match please reenter')
        l_name(input('enter your last name:  '))

                    
def number(a):
    b=int(input('reenter your phone number:  '))
    if a==b and len(str(a))==10 :
        data.append(b)
        money.append(b)
        dob(input('enter your date of birth DD/MM/YYYY:  '))

    else:
        print('please check the number ')
        number(int(input('enter your number')))
                    
def dob(a):
    b=input('reenter your date of birth DD/MM/YYYY:  ')
    if a==b:
        data.append(b)
        aadhar(int(input('enter the aadhar number:  ')))

    else:
        print('please recheck your date of birth')
        dob(input('enter your date of birth DD/MM/YYYY:  '))
                    
def aadhar(a):
    b=int(input('reenter the aadhar number:  '))
    if a==b and len(str(a))==12 :
        data.append(b)
        print('PASSWORD SHOULD HAVE')
        print('number,uppercase,lowercase,special charecter and 8 letters')
        password(input('enter the password:  '))
    else:
        print('aadhar number doesnt match try again')
        aadhar(int(input('enter the aadhar number:  ')))
                        
def password(a):
    b=input('reenter the password')
    upper= False
    lower= False
    digit= False
    special= False

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
        sno()
                    
    else:
        print('password doesnt match try again')
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
        print('your successfully registered to kv bank')
                
                
        no_of_attempt=0
        data.append(no_of_attempt)
        print(data)
        xx=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
        xxx=xx.cursor()
        insert='insert into user_info (email,first_name,last_name,phone_no,date_of_birth,aadhar,password,sno,no_of_attempts) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        values=(data)
        xxx.execute(insert,values)
        xx.commit()
        xx.close()

        print(money)
        xx2=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
        xxx2=xx2.cursor()
        insert2='insert into user_tran (email,phone_no,sno,available_balence) values(%s,%s,%s,%s)'
        values2=(money)
        xxx2.execute(insert2,values2)
        xx2.commit()
        xx2.close()

        def x():
            
            print('enter 1 to login')
            print('enter 2 to exit')
            print('enter 3 to delete user')
            x=int(input('enter the number'))
            if x==1:
                import login
            elif x==2:
                import Exit
                #    break
            elif x==3:
                import delete
            #    break
            else:
                print('invalid input')
        x()        

    else:
        print('invalid input try again')
        deposit()
                
mail(input('enter your email id:  '))
'''



money=['zzz@gmail.com', 9632587412, 10, 10000]
xx2=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='bank')
xxx2=xx2.cursor()
insert2='insert into user_tran (email,phone_no,sno,available_balence) values(%s,%s,%s,%s)'
values2=(money)
xxx2.execute(insert2,values2)
xx2.commit()
xx2.close()

'''
"""

def rando():
    otp=random.randint(100000,999999)
    print(otp)
    return otp

def opt_s(r_mail,otp):
    s_mail="krishnakondu108@gmail.com"
    s_pass="Vamshi@28"
    message=MIMEMultipart()
    message["from"]=s_mail
    message["to"]=r_mail
    message['subject']='your otp form KV Bank'

    body=f'your otp code is {otp}, please enter the otp to identify'
    message.attach(MIMEText(body,'plain'))

    try:
        server= smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(s_mail,s_pass)
        server.sendmail(s_mail,r_mail,message.as_string())
        server.quit()
        print('sucessfully otp has sent')

    except Exception as e :
        print(f'error {e}')
        
def verify(entered_otp):
    b=otp_g
    if b == entered_otp:
        print('sucessfully verified mail')
    else:
        print('invalid otp try again')

otp_g=rando()
s=input('enter the email to sent otp')
opt_s(s,otp_g)
verify(int(input('enter the otp:  ')))


"""













