def say_hi():
    print("Hello user") 

print("Top")
say_hi()
print("Bottom")


def say_hi(name):
    print("Hello "+ name) 

say_hi("Thomas")
say_hi("Geir")

def say_hi(name, age):
    print("Hello "+ name + ", you are " + str(age))

say_hi("Thomas", 23)
say_hi("Geir", 44)

