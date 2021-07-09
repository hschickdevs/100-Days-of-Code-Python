import colorgram

original_colors = colorgram.extract('color_palette.png', 8)

colors = []
for original_color in original_colors:
    color = original_color.rgb
    r = color.r
    g = color.g
    b = color.b
    rgb = (r, g, b)
    colors.append(rgb)

print(colors)
