# isStringPermutation question
def isStringPermutation(string1, string2):
    word_bank = []
    word_bank2 = []
    char_list1 = list(string1)
    char_list2 = list(string2)

    for i in char_list1:
        word_bank.append(i)
        for j in char_list2:
            word_bank.append(j)
            if word_bank == word_bank2:
                return True
            else:
                return False
                
# Test Case
print(isStringPermutation("hey", "eyh"))

# pairsThatEqualSum question
def equal_sum(int_array, target):
    return_array = []

    for i in int_array:
        if int_array[i] == int_array[i+1]:
            return_array.append(i) and return_array.append(i+1)
            return return_array
        else:
            return_array = [0]
            return return_array




# Test Case
print(equal_sum([12, 3, 4, 9, 7], 7))
