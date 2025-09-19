class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()
    def menu(self):
        user_input=input("""Welcome to chatbook !! How would you like to proceed ?
                         1.press 1 to signup
                         2.press 2 to singnup
                         3.press 3 to write a post 
                         4.press 4 to message a friend
                         5.press any other key to exit""")
        if user_input=="1" :
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.sendmessage()
        else:
            exit()
            
    def signup(self):
        email=input("enter your email here ->")
        pwd=input("setup your password here")
        self.username=email
        self.password=pwd
        print("you have signed up successfully")
        print()
        self.menu()
        
    def signin(self):
        if self.username==" " and self.password==" ":
            print("signup first by pressing the 1 in the main menu")
        else:
            usname=input("enter your email/username here -> ")
            pwd=input("enter the password here: ")
            if self.password==pwd and self.username==usname:
                print("you have signed in successfully")
                self.loggedin=True
            else:
                print("please input correct credentials") 
            print() 
            self.menu()
    def my_post(self):
        if self.loggedin==True:
            txt=input("enter you message here")
            print(f"following content has been posted ->{txt}") 
        else:
            print("you need to sign in first to post something")
        print()  
        self.menu()
    def sendmessage(self):
        if self.loggedin==True:
            txt=input("enter your message here-> ")
            frnd=input("whom to send the msg? -> ")
            print(f"message has been send to the friend")
        
obj=chatbook()        