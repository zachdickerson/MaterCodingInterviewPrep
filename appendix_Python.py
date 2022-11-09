def my_list():
    new_list = [1,2,3,4,5]
    return new_list

def push(item):
    get_item = [item]
    our_list = my_list() + get_item
    return our_list

print(push(6))

new_list = []
print(new_list + push(6))



