def foo():
    try: return 1
    finally: return 2

# print(foo())

# ternary operator
age = 18
status = "Adult" if age >= 18 else "Minor"
# print(status)



# to set function attribute
def myFunction(x):
    var = x * 2

    # setting attributes for the function
    myFunction.input_value = x
    myFunction.description = f"Return {x} * 2"
    return var

# First, call the function to set the attributes
myFunction(5)

# Now it's safe to access the attributes
print(myFunction.input_value)     # Output: 5
print(myFunction.description)     # Output: Return 5 * 2



# ellipsis object (...) in python can be used as a placeholder in code where implementation is pending.
def func():
    ...
    # placeholder for future code
    if 3 < 6:
        ...
        for i in range(10):
            ...



# warlus operator ( := )
valueList = [1, 2, 3, 4]

if (n := len(valueList)) > 3:
    print(f"List is too long ({n} elements), expected <= 3")



class Parent:
    def show(self):
        print("Parent Class")
    
class Child(Parent):
    def show(self):
        super().show()
        print("Child Class")

obj = Child()
obj.show()




class Dog:
    def speak(self):
        return "Woof"
    
class Cat:
    def speak(self):
        return "Meow"
    
def make_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(make_sound(dog))
print(make_sound(cat))






