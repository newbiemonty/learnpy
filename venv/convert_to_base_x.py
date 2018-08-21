def convert_to_base_x(base, number):
        base_array = "0123456789abcdef"
        if number < base:
            return base_array[number]
        else:
            return convert_to_base_x(base, (number//base)) + base_array[number%base]


print(convert_to_base_x(16, 1002))
print(convert_to_base_x(10, 1002))
print(convert_to_base_x(12, 1002))
print(convert_to_base_x(8, 1002))
print(convert_to_base_x(2, 1002))

