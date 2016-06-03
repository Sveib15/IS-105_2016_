from random import randint

def makeCode():
	code = "";
	length = randint(1,10);
	
	for i in range(0, length):
		letter = randint(1,10);
		if letter == 1:
			code += "y";
		elif letter == 2:
			code += "c";
		else:
			code += "x";
	
	return encode(code);
		
	
def encode(message):
	code = "";
	for c in message:
		if c == "x":
			code += "0";
		if c == "y":
			code += "10";
		if c == "c":
			code += "11";
	return code;
	
	
def decode(message):
	code = "";
	index = 0;
	skip = False;
	
	while index < len(message):
		if message[index] == "1":
			if message[index + 1] == "0":
				code += "y";
			else:
				code += "c";				
			index+= 1;
			skip = True;	
						
		if skip == False:	
			if message[index] == "0":
				code += "x";	
						
		index+= 1;
		skip = False;	
					
	return code;
	
	
#Test
code = makeCode();
print code;
print decode(code);





		
