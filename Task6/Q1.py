f=open("onelinefile.txt","r")
string=str(f.read())
n=len(string)
temp=""
c=0
for i in range(n):
    if string[i].isalpha()==True:
        temp+=string[i]
        if i+1<n:
            if string[i+1].isalpha()!=True:
                if c!=3:
                    temp+=","
                c+=1
    elif string[i].isdigit()==True:
        temp+=string[i]
        if string[i+1]==".":
            temp+="."
        elif string[i+1].isdigit()!=True and string[i+1]!=".":
            if c!=3:
                temp+=","
            c+=1
    if c%4==0:
        temp+="\n"
        c=0
f.close()
f1=open("Filename2.csv","w")
f1.writelines(temp)
f1.close()
print("The lines written in the file are\n"+temp)
