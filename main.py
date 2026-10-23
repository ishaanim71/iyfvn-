n=int(input("How many characters to preview:"))
file=open("notes.txt","r")
print(file.read(n))
file.close()
print()


file=open("notes.txt","r")
lines=file.readlines()
file.close()
print("Total lines:",len(lines))
for i in range(len(lines)):
    print(i+1,"->",lines[i].strip())
print()

f1=open("notes.txt","r")
f2=open("abc.txt","w")
for line in f1.readlines():
    if not line.startswith("#"):
        print(line)
        f2.write(line)
f2.close()
f1.close()