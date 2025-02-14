number_list = [11, 22, 22, 33, 43, 544]

# print(number_list[0])
# print(number_list[1])
# print(len(number_list))
#
# for i in range(len(number_list)):
#     print(number_list[i])
#
# for number in number_list:
#     print(number)

number_list.append(12)
number_list.insert(0, 1111)
number_list.remove(1111)
number_list.sort()

print(number_list)
print(number_list.count(22))