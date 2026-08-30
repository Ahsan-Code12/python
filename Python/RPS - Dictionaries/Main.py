def user_name():
    username = input("enter your name: ")
    return username

choice_user_name = user_name()

def user_color():
    usercolor = input("enter color: ")
    return usercolor

color = user_color()

dict = {"name": choice_user_name, "color": color}
print(dict)