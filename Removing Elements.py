def remove_every_other(my_list):
    new_list = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            new_list.append(my_list[i])
    return new_list

print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))