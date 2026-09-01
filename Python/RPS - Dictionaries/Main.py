def username():
    userchoice = input("enter your name: ")
    return userchoice

name_response = username()

def get_color():
    getcolor = input("enter your color: ")
    return getcolor

color_response = get_color()

lists = {"name: ": name_response, "color: ": color_response}
print(lists)
