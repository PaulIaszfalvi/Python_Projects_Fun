def writeFile(text): 
    f = open("personal_info.txt", "w")
    f.write(text + "\n")
    f.close()

#open and read the file after the appending:
f = open("personal_info.txt", "r")
print(f.read())
f.close()