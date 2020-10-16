def get_user(request):
	user_value = request.get_argument('username')
	password_value = request.get_argument('password')

	print(f"user_value: {user_value}")
	print(f"password_value: {password_value}")

	if(user_value == 'nyc' and password_value == 'iheartnyc'):
		return 1
	else:
		return None

login_url = '/login'
