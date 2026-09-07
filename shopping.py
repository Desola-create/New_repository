shopping_list = ["rice", "milk", "bread", "eggs" , "juice"]

def show_list(shopping_list):
    for item in shopping_list:
        print(item)

def add_item(shopping_list, new_item):
    shopping_list.append("cookies")
    shopping_list.append("chicken")

print("Shopping List:")
show_list(shopping_list)

add_item(shopping_list, "cookies")
add_item(shopping_list, "chicken")
print("Updated Shopping List:")
show_list(shopping_list)