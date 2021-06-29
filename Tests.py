import hashlib
f= open("QuizQuest/Username.py", "a")


Username = input("please enter a username. please note that no numbers are allowed. \n")
Password = input("please enter a password. please note that no numbers are allowed. \n")
hashed_password = hashlib.sha224(f"{Password}").hexdigest()
f.write(f"{Username} = '{hashed_password}'\n")

#f= open("//dataserver2/CCates$/dev/QuizQuest/file.txt", "w+")
#for i in range(10):
#    f.write("This is line %d\r\n" % (i+1))
#f.close()
#f= open("//dataserver2/CCates$/dev/QuizQuest/file.txt", "r")
#print(f.read())
#f.close()