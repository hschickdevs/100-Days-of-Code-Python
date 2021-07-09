def format_name1(f_name, l_name):
    print(f_name.title())
    print(l_name.title())


def format_name2(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    print(f'{formatted_f_name} {formatted_l_name}')


def format_name3(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f'{formatted_f_name} {formatted_l_name}'


format_name1("angela", "ANGELA")
print()

format_name2("AnGElA", "YU")

formatted_string = format_name3("AnGEla", "YU")
print(formatted_string)

print(format_name3("AnGEla", "YU"))
print()

output = len("Angela")
print(output)
