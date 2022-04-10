while(True):
	a= int(input("please enter your age and dob"))
	if a<1:
		print('please enter valid input and retry')
	
	else:
		if a>1500:
			A=2022
			b=100-A
		else:
			b=100-a
		if a>=2022:
			print('youn are not born yet')
		else:
			if b==100 or b==0:
				print('you are exectly 100 years old')
			else:
				if b<-50:
					if a>1500:
						print('you are too old and age is',b*-1,'years more than 100 years and current age is',A)
					else:
						print('you are too old and age is',b*-1,'years more than 100 years')
	
				else:
					if a>1500:
						print(f'your curerent age is {A} and you will become 100 years old after {b} years') 
					else:
						if a>100:
							print('your age is', b*-1,' more than 100 years')
						else: 
							print(f'you will become 100 years old after {b} years')
	if a<1:
		break
	

	 

