def convert_to_base_x(base, number):
        base_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        if number < base:
            return base_array[number]
        else:
            return convert_to_base_x(base, (number//base)) + base_array[number%base]


#print(convert_to_base_x(16, 1002))
#print(convert_to_base_x(10, 1002))
#print(convert_to_base_x(12, 1002))
#print(convert_to_base_x(8, 1002))
#print(convert_to_base_x(2, 1002))


def reverse(str):
    if len(str) is 0:
        return ""

    if len(str) is 1:
        return str[0]
    else:
        return str[len(str) - 1:len(str)] + reverse(str[:len(str) - 1])


#print(reverse("1234567890"))
#print(reverse(""))
#print(reverse("a"))


def permutation_of_a_string(string, index):
    if len(string) == 0:
        print("")
        return

    if len(string) - 1 == index:
        print(str(string))
    else:
        for i in range(index, len(string)):
            string[i], string[index] = string[index], string[i]
            permutation_of_a_string(string, index+1)
            string[index], string[i] = string[i], string[index]


#permutation_of_a_string(list("abcd"), 0)
#permutation_of_a_string(list(""), 0)
#permutation_of_a_string(list("a"), 0)


"""
Assume that the input is an array of size 'n' where 'n' is an even number. 
Additionally, assume that  half the integers are even and the other half are odd. 
Print only those permutations where odd and even integers alternate, starting with odd.
[2,1,11,12,4,6,3,5,7,8]
[1,2,<recurse>]
[1,4,<recurse>]
[1,6,<recurse>]
[1,8,<recurse>]
"""


def position_value_okay(index, element):
    if (index % 2 == 1 and element % 2 == 0) or (index % 2 == 0 and element % 2 == 1):
        return True
    else:
        return False


def permutation_odd_even(arr, start_index):
    if start_index == len(arr) - 1:
        print(arr)
    else:
        for i in range(start_index, len(arr)):
            if position_value_okay(start_index, arr[i]):
                arr[start_index], arr[i] = arr[i], arr[start_index]
                permutation_odd_even(arr, start_index+1)
                arr[i], arr[start_index] = arr[start_index], arr[i]


#permutation_odd_even([1,2,3,4,5,6,7,8], 0)
#permutation_odd_even([2,4,6,8,1,3,5,7], 0)
#permutation_odd_even([1,4], 0)
#permutation_odd_even([4,1], 0)


"""
Assume that the input is an array of characters. Print any one permutation that is also a word in the dictionary. Assume
that you have two library functions you can use.

bool  ValidWord(char array a) returns true if and only if the string a is a dictionary word.
bool ValidWordPrefix(char array a, int a_size) returns true if and only if a[0...a_size-1] is a prefix of at least one 
word in the dictionary.
"""

