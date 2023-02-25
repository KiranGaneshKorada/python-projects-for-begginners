def f():
    print("welcome to email slicer\n")

    email=input("paste the mail id\n")

    (username,domain)=email.split("@")
    (domain,extension)=domain.split(".")

    print("USERNAME:"+username+"\n")

    print("DOMAIN:"+domain+"\n")

    print("EXTENSION:"+extension+"\n")

    print("thank you\n")

f()