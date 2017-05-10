def OddOdd(values):
	Toggle=True
	SumToReturn=0
	for value in values:
		if(Toggle==True):
			if(value%2==1):
				SumToReturn=SumToReturn+value
		Toggle= not Toggle
	return(SumToReturn)
low=OddOdd([1,5,2,7,3,5,2,6])
lying=OddOdd([3,2,2,2,2,2,2])
fruit=OddOdd([2,3,2,3,2,3,3])
print(low)
print(lying)
print(fruit)