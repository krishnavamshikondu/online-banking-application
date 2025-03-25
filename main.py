'''

#import importlib
#import register
#import login
#import forgot
#import delete
#import Exit


def excute(x):
    if x==1:
            #print('hi')
            #register=importlib.import_module('register')
            #register.run_register()
        import register    
    elif x==2:
            #login=importlib.import_module('login')
            #login.run_login()
        import login
                    
    elif x==3:
            #forgot=importlib.import_module('forgot')
            #forgot.run_forgot()
        import forgot
                    
    elif x==4:
            #importlib.reload(delete)
        import delete
    elif x==5:
        import Exit
        return False
                    
    else:
        print('invalid input try again')
    return True

def mainn():
    while True:
        print('enter 1 to register for new user')
        print('enter 2 to login for existed user')
        print('enter 3 to reset your password')
        print('enter 4 to delete your user')
        print('enter 5 to exit')
        print()
        x=int(input('enter the number:  '))
                
        if not excute(x):
            break
            print('doesnot excest')
        

            
        
if __name__=="__main__":
    mainn()
'''
'''
def run_register():
    print('register file excuted')
if __name__=="__main__":
    run_register()
    
def run_login():
    print('login')
if __name__=="__main__":
    run_login()

def run_forgot():
    print('forgot')
if __name__=="__main__":
    run_forgot()
'''

"""
import subprocess

def execute_script(choice):
    if choice == '1':
        subprocess.run(['python3', '/mnt/data/banner.py'])
    elif choice == '2':
        subprocess.run(['python3', '/mnt/data/delete.py'])
    elif choice == '3':
        subprocess.run(['python3', '/mnt/data/login.py'])
    elif choice == '4':
        subprocess.run(['python3', '/mnt/data/register.py'])
    elif choice == '5':
        print("Exiting...")
        return False
    else:
        print("Invalid choice. Try again.")
    return True

def main():
    while True:
        print("\nChoose an option:")
        print("1. Execute banner.py")
        print("2. Execute delete.py")
        print("3. Execute login.py")
        print("4. Execute register.py")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if not execute_script(choice):
            break

if __name__ == "__main__":
    main()


"""


while True:
    print('enter 1 to register for new user')
    print('enter 2 to login for existed user')
    print('enter 3 to reset your password')
    print('enter 4 to delete your user')
    print('enter 5 to exit')
    print()
        
    x= int(input("Enter your choice: "))
    
    if x==1:
        import register    
    elif x==2:
        import login
                    
    elif x==3:
        import forgot
                    
    elif x==4:
        import delete
    elif x==5:
        import Exit
        break
                    
    else:
        print('invalid input try again')































