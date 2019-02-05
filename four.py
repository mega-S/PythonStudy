def create_default_user():
    name = "Tom"
    age = 33
    return age, name
 
 
user_name, user_age = create_default_user()
print("Name:", user_name, "\t Age:", user_age)