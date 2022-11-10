

def romanToInt(s):
    
    my_addition = 0
    counter = 0

    my_dict = {
        'I':1, 'V':5, 'X':10, 
        'L':50, 'C':100, 'D':500,
        'M':1000
    }
    
    if len(s) == 1:
        my_addition += my_dict[s]
        return my_addition

    else:
        list_of_romans = [x for x in s]
        for element in list_of_romans:
            my_addition += my_dict[element]
            if element == 'X' or element == 'V':
                print(type(list_of_romans[element]))
                counter = element - 1
                if list_of_romans[counter] == 'I':
                    print('here2')
                    my_addition = my_addition -2


            #my_addition += my_dict[element]

    return my_addition
            

print(romanToInt('IV'))