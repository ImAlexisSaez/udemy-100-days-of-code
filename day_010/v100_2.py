def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    f_name, l_name = f_name.title(), l_name.title()
    return f"{f_name} {l_name}"


formated_name = format_name("ALExis", "sáEZ")
print(formated_name)
