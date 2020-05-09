import pyrebase
config={
    

}
firebase =pyrebase.initialize_app(config)
auth=firebase.auth()
db=firebase.database()
#create user
email=input("enter email")
password=input("enter password")
n= int(input("enter n"))
def create_post(id, text):
    db.child("posts").child(id).set({"text":text})
def login(email, password):
    user = auth.sign_in_with_email_and_password(email,password) 
    print(user['localId'])
    text="sample text abcd pqr"
    create_post(user['localId'],text)
    
    
def signup(email,password):
    auth.create_user_with_email_and_password(email.strip(), password.strip())

if(n==0):
    login(email,password)
    
elif(n==1):
    signup(email,password)
else:
    print("invalid n")


