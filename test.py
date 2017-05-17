def funWithStrings(InputList):
	tmp=InputList[2]
	InputList.remove(tmp)
	InputList.insert(0,tmp)
	sentence=InputList[0]+"You rock!!!"+InputList[1]+InputList[2]
	finalvalue=""
	for letter in sentence:
		finalvalue=letter+"."+finalvalue
	return(finalvalue)
a=["hi","there","coder!"]
print(funWithStrings(a))


def removeLetter(source,letter):
	answer=""
	for Character in source:
		if(Character!=letter):
			answer+=Character
	return(answer)

print(removeLetter("Python Programing.","o"))