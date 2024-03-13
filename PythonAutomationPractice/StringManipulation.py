str = "Proshanta deBnath%*# Test"

str1 = "Test"

print(str[1])

print(str[0:7])  # print substring

print(str + str1)  # string concatenation for two string

# string is present or not/ Substring check
check: bool = str1 in str
print(check)

# Split string
var = str.split(" ")
print(var)

# Trim string
str2 = " hello "
print(str2.strip())
print(str2.lstrip())