## DATA SOURCES ##

## delimited formats ##
#.csv
my_string = "Hello-World,-this is a sentence."
# Split the string by spaces
words = my_string.split()
print(words)

## JSON ##

import json # you'll want to import the json module in order to use loads/dumps
json_obj = {
    "employees": [
        {
            "name": "Shyam",
            "email": "shyamjaiswal@gmail.com"
        },
        {
            "name": "Bob",
            "email": "bob32@gmail.com"
        },
        {
            "name": "Jai",
            "email": "jai87@gmail.com"
        }
    ],
    "quartly_profits": [      # list
        {
            "Q1": 1232132312, # 0
            "Q2": 1232132312, # 1
            "Q3": 1232132312, # 2
            "Q4": 1232132312  # 3
        }
    ],
    "holidays": {               # dictionary
        "october": "halloween"  # dictionary
    }
}

## converts JSON obj to a string ##
json_object_1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(json_object_1)
print(f"json_string --> {json_string}")

## converts a string to JSON obj ##
json_string = '{"name": "John", "age": 30, "city": "New York"}'

json_object_2 = json.loads(json_string)
print(f"Json_obj --> {json_object_2['name']}")


# ans = json_object_2['potato']
ans = json_object_2.get("potato", "not in list")

#########################
## python get vs index ##
#########################
# notice below, that get will tell you if the key exists
# due to the datatype being a dictionary
# can not use .get() on lists
october_holidays = json_obj.get("holidays").get("october")
december_holidays = json_obj.get("holidays").get("december")

print(f"october_holidays: {october_holidays}")
print(f"december_holidays: {december_holidays}")


# x = 2
# print("hello world", x)
# print(f"hello world {x}")
# print("hello world {0}".format(x))

print("------------------------")

employee_list = json_obj.get("employees")
qp = json_obj.get("quartly_profits")

for employee in employee_list:
    print(employee)

print("------------------------")

## SQL ##
# ??? - for the future

