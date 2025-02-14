# colors_tuple = ("blue", "red", "green", "white")
#
# print(colors_tuple)
# print(type(colors_tuple))
# print(colors_tuple[1])
#
# for color in range(len(colors_tuple)):
#     print(colors_tuple[color])
#
# for color in colors_tuple:
#     print(color)

full_name = "Nguyen Khanh Duy"
full_name_tuple = tuple(full_name)

print(type(tuple(full_name)))

for word in full_name_tuple:
    print(word)