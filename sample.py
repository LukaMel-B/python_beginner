from random_multi import randomMulti
full_name = input ("What is your name? ")
# this is how you print varibles inside a string using f-string
print (f"your name is {full_name}")
# '''''' tripple quotes for mutliple line commenting hash for single line comment


list_data = ['john', 'hary', 'samuel','mary']
# print(f"\nThis is a third data of list in the list of datas: {list_data[2]}\n")

# tuples are unchangable lists
tuple_data = ('john', 'hary', 'samuel','mary')

list_data.append('Luha')
print(f"this is list_datas after append: {list_data}")
print(f"tuple_data cannot append: {tuple_data}")

# append tuple by converting it to list and adding one value then convert it back to tuple

sample_list = list(tuple_data)
sample_list.append('Luha')
tuple_data = tuple(sample_list)
print(f"this is tuple_data hacked to append: {tuple_data}")


# dictionary are same as maps in dart
dict_datas = {
    "name": "Luha",
    "age": 23,
    "birth_year": 2001,
    "birth_month": 4,
    "birth_day": 17,
    "father": "Ali Akbar",
    "mother": "Suhra",
    "marital_status": False,
}

print(dict_datas)
dict_datas.update({"siblings":"Hani and Emna"})
print(dict_datas)
dict_datas.pop("marital_status")
print(dict_datas)


bool_value = True
print(f"this is a boolean\nvariable:bool_value\nvalue:{bool_value}")


num_final =randomMulti(40, 10)
print(num_final)