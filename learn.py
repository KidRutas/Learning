# Data Structures

# Array/List
arr = [1, 3, 6, 8, 2, 9]

arr.append(21)
arr.insert(0, "a")
arr.remove('a')
arr.pop(3)

print(f"List\n{arr}\n{arr[2]}\n{arr[-1]}\n")

# Tuple
my_tuple = (1, 3, 5)

a, b, c = my_tuple

print(f"Tuples\n{my_tuple}\n{my_tuple[0:2]}")
print(f"{a}\n{b}\n{c}\n")

# Dictionary
name = "Nkosi"
age = 21

dictionary = {
              "Name": name,
              "Age": age
             }
print(f"Dictionary\n{dictionary}\n{dictionary['Name']}\n{dictionary.keys()}")


# Comments

# KeyError: 'height'
# dictionary['height']

# TypeError: 'int' object is not subscriptable
# arr[-1][0]

# IndexError: list index out of range
# arr[len(arr)+1]

# TypeError: 'int' object is not subscriptable
# my_tuple[-1][4]

# IndexError: tuple index out of range
# my_tuple[3]