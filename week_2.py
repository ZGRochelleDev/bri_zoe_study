
################
## variables ###
## printing ####
## user input ##
################

## Variables ##
x = 0
some_var = 2

## data types ##
# int
# examples:
    # 12321312321
    # 666
an_int = 666

# float
a_float = 3.14

# char
a_char = "A"
another_char = "B"
another_char = '!'
another_char = "."

# strings
some_string = "America"
another_string = "123"
another_string = "1A2b!%^()_--potato"


# variables have types aka "datatypes"
ans = type(another_string)
# print(ans)

## how to print stuff ##
x = 1
print(x)
print("strings")
print("strings", x)

some_var = "12345"
print("this is your var: ", some_var)

the_var = "some var"
print(f"this is a var {the_var}")

## User input ##
val_1 = input("enter yo name plz: ")
val_2 = input("enter yo dob plz: ")
val_3 = input("enter yo addr plz: ")

data_array = []

data_array.append(val_1)
data_array.append(val_2)
data_array.append(val_3)

for ele in data_array:
    print(f"this is your data: {ele}")





