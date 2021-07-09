def format_name1(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f'{formatted_f_name} {formatted_l_name}'
    print("This got printed!")  # It didn't


def format_name2(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f'Result: {formatted_f_name} {formatted_l_name}'


def format_name3(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f'Result: {formatted_f_name} {formatted_l_name}'


print(format_name1("AnGEla", "YU"))
print(format_name2(input("What is your first name? "), input("What is your last name? ")))
print(format_name3(input("What is your first name? "), input("What is your last name? ")))
