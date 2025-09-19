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
            pass
        elif user_input=="4":
            pass
        else:
            exit()
            
    def signup(self):
        email=input("enter your email here ->")
        password=input("setup your password here")
        self.username=email
        self.password=password
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
        
obj=chatbook()        