def my_functions(): 
    print('Hello World!')


my_functions()

def greet(name): 
    print('Hello', name)

greet('ahmed')

def sum(x, y): 
    print(x + y)

sum(3, 4)

def info_one(name, age): 
    print(f"Hello {name}, You are {age} years old")

info_one('Mohammed', 35)
def info_tow(name, age): 
    return(f"Hello {name}, You are {age} years old")

print(info_tow('Mohammed', 35))

def get_age(): 
    age = int(input("Enter Your Age: "))
    if age < 0: 
        return
    if age > 120:
        return
    print(age)
get_age()

def lang_list(): 
    return['Python', 'PHP', 'JavaScript', 'Ruby']

langs = lang_list()
print(langs)