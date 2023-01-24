import colorgram


def get_colors(image, num_colors):
    list_of_colors = []
    image_colors = colorgram.extract(image, num_colors)

    for color in image_colors:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        list_of_colors.append((red, green, blue))

    return list_of_colors[4:]  # Leave first colors (white background colors).


image_path = "image.jpg"
number_of_colors = 30

colors = get_colors(image_path, number_of_colors)