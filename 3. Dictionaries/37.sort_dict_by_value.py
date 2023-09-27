my_dictionary = {'name':'Human','age':'80', 'city':'Planet', 'job':'Programmer'}
sorted_dict = {k: v for k,v in sorted(my_dictionary.items(), key=lambda item:item[1])}
print(sorted_dict)