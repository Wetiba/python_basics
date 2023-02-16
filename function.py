def hello():
    print("This is my first function")
hello()
hello()
def majina(fname,lname):
    print(fname+ " "+lname)
majina("Erick","Were")

def greetings(name, greeting="Hello"):
    print(greeting +" "+ name)
greetings("Erick")
greetings("Joan", "Niaje")

def maxvalu(a, b, c, d, e, f):
    return max(a,b,c,d,e,f)
result=maxvalu(7,9,1,8,17,45)
print(result)
def sort_list(lst):
     return sorted(lst)
answer=sort_list([3,9,0,2,7,1,5,4])
print(answer)
def print_mumbers(n):
    for i in range(n):
        print(i)
print_mumbers(5)