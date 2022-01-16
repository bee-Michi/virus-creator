terminalamount = int(input("Select the number of terminal's to create: "))
f = open("virus.bat", "wt")
for terminal in range(terminalamount):
    f.write("start\n")
print("File created")