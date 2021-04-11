#Explain your work

#Question 1
Username="şeyma"
Password=4929
Kul_us=input("Username: ")
Kul_pas=int(input("Password: "))
if Username==Kul_us and Password==Kul_pas:
    print("kullanıcı adı ve şifre doğru !")
elif Username==Kul_us:
    print("Şifreyi yanlış girdiniz !")
elif Password==Kul_pas:
    print("kullanıcı adını yanlış girdiniz !")
else:
    print("kullanıcı adı ve şifre hatalı !")
