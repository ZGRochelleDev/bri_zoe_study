## DATA SOURCES ##

## delimited formats
#.csv
my_string = "Hello-World,-this is a sentence."
# Split the string by spaces
words = my_string.split()
print(words)

## JSON

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
    "quartly_profits": [
        {
            "Q1": 1232132312,
            "Q2": 1232132312,
            "Q3": 1232132312,
            "Q4": 1232132312
        }
    ]
}



print("------------------------")


employee_list = json_obj.get("employees")
qp = json_obj.get("quartly_profits")


for employee in employee_list:
    print(employee)



print("------------------------")

## SQL


