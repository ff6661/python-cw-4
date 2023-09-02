def my_name():
    print('my name is fatima')
def my_meal(food, drink):
    print(f"i like to eat {food} while drinking {drink}")
my_meal("french fries", "pepsi")
def cube(number):
    return number**3
#print(cube(5))
def by_three(number):
    if number % 3 == 0:
        return(cube(number))
    else:
        return False
print(by_three(9))