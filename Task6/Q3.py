import re

print("\nThe atleast 6 character words are");  
file = open("data.txt", "r")  
text=file.read()
lis=re.findall(r"\b\w{6,}\b", text)
print(*lis,sep='\n')
file.close()

count = 0  
word = ""  
maxCount = 0  
words = [] 
file = open("data.txt", "r")
for line in file:    
    string = line.lower().replace(',','').replace('.','').split(" ");    
    for s in string:  
        words.append(s);  
for i in range(0, len(words)):  
    count = 1;   
    for j in range(i+1, len(words)):  
        if(words[i] == words[j]):  
            count = count + 1;   
    if(count > maxCount):  
        maxCount = count;  
        word = words[i];            
print("Most repeated word: " + word);  
file.close();
