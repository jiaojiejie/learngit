_username = "jiaojiejie666"
_password = "123666"
flag = False
for i in range(3):
     username = input("username:")
     password = input("password:")
     if username == _username and password == _password:
         print("welcome %s to login" % _username)
         flag = True
         break
     else:
        print("Invalid username or password !")

if not flag:
    print("输错三次，锁定")
