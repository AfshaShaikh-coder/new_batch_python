def f1(n):
	if isinstance(n,int):# 10
		print(n,"int data type")
	elif isinstance(n,str):
		print(n,'string data type')
	else:
		print("wrong")

f1(10)

# decor

def outer(func):
	def inner(a,b):
		if b==0:
			print("cannot divide by zero")
		else:
			return func(a,b)
	return inner


# func==divide

@outer
def divide(a,b):
	print(a/b)

#o=outer(divide)
#o(10,20)# inner
#o(5,0)
divide(10,2)

is_rgister=True
is_logged_in=True


def register_required(func):
	def inner():
		if is_rgister==True:
			func()
		else:
			print("pls register first")
	return inner



def login_check(func):
	def inner():
		if is_logged_in==True:
			func()
		else:
			print("pls login first")
	return inner

@register_required# first gate
@login_check#2nd gate
def show_dashboard():
		print("welcome to dashboard")

show_dashboard()

#output=register_required(login_check(show_dashboard))



"""
@login_check
def view_profile():
	print("here is your profile")

view_profile()
"""