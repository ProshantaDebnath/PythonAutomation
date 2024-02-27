# First Hello program in python
print("hello")

# Python always follow standard coding indention

# Variable and their types
a = 3
print(a)

str = "hello there!"
print(str)

# Multiple variable declaration
a, b, c = 5, 4, "there"
print(a)

# concatenation of two data types
print("{}{}".format("String", b))
print(c + "Hi")
print(type(c))

# List manipulation
values = [1, 2, "there", 65.00, "%%7&", 5]
print(values[3])
print(values[-1])  # 5
print(values[2:4])  # Access values by subindex
values.insert(5, "test")  # insert new values
values.reverse()  # [5, 'test', '%%7&', 65.0, 'there', 2, 1]
values[2] = "Automation"  # Update the existing values

# Tuple
val = (1, 2, 4, "*&^%", "test")
# val[1] ="test" # Difference between tuple and list is in tuple we can not update the properties of the list but in list it is possible

# Dictionary
dic_HashMap = {"a": 2, 4: "test"}
print(dic_HashMap[4])
print(dic_HashMap["a"])

# Creation dictionary and insert data in one by one
dict = {}
dict["FirstName"] = "P"
dict["LastName"] = "D"
dict[1] = 1
print(dict)