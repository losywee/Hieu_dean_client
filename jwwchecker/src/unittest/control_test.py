#test district
#For module:login_handler
def test():
	userinfo={'username':'test','password':'test'}
	hander=Handle_allpages()
	Get_checkcode(hander)
	print('get code:')
	code=input()
	Begin_login(hander,userinfo,code)


if __name__ == '__main__':
	test() 
