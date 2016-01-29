str = raw_input("Enter your binary code")
#str = "0" + str[2:]
message = ""
while str != "":
    i = chr(int(str[:8], 2))
    message = message + i
    str = str[8:]
print message