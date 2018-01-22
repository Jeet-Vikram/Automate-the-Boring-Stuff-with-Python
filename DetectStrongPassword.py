import pyperclip,re
CheckPassword=re.compile(r'''(
	(?=.*?[A-Z])					#contains uppercase letter
	(?=.*?[a-z])					#contains at least one lowercase letter
	(?=.*?[0-9])					#has atleast one digit
	(?=.*?[#?!@$%^&*-+])			#contains at least one special case letters
	.{8,}						    #atleast 8 characters
	)''',re.VERBOSE)
def PasswordChecker():
	text=input("Enter a Password to check if it is strong or not: ")
	mo=CheckPassword.search(text)
	if(mo):
		print('Brovo, your Password is Strong')
		
	else:
		print('Sad, your Password is Weak')
		
PasswordChecker()
