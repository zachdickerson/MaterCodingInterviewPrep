

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

        enum = enumerate(list_of_romans)
        romans_dic = dict((i,j) for i,j in enum)

        for i,element in enumerate(list_of_romans):
            my_addition += my_dict[element]
            if i >= 1:
                if element == 'X' or element == 'V':
                    if romans_dic[i - 1] == 'I':
                        my_addition = my_addition - 2
                elif element == 'L' or element == 'C':
                    if romans_dic[i - 1] == 'X':
                        my_addition = my_addition - 20
                elif element == 'D' or element == 'M':
                    if romans_dic[i - 1] == 'C':
                        my_addition = my_addition - 200
    return my_addition
            
print(romanToInt('MCMXCIV'))
