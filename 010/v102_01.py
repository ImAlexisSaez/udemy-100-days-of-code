def format_name(f_name, l_name):
    """Returns a formated name in title case

    Args:
        f_name (str): first name
        l_name (str): last name

    Returns:
        str: formated name in title case
    """
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    f_name, l_name = f_name.title(), l_name.title()
    return f"{f_name} {l_name}"


formated_name = format_name("ALExis", "sáEZ")
print(formated_name)
