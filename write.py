#WRITE mode
f=open("test.txt","w")
f.write("hi")
f.write("\nbyeee")
f.close()

#APPEND mode
f=open("test.txt","a")
f.write("\nsee uuu ")
f.close()

#tyo lekako file laii read gareko
f=open("test.txt","r")
print(f.read())
f.close()


