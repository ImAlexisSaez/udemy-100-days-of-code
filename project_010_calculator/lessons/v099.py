# functions with outputs

def format_name(f_name, l_name):
    f_name, l_name = f_name.title(), l_name.title()
    return f"{f_name} {l_name}"


formated_name = format_name("ALExis", "sáEZ")
print(formated_name)
