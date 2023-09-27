def are_anagram(str1,str2):
    return sorted(str1) == sorted(str2)

str1 = "listen"
str2 = "silent"
print(are_anagram(str1,str2))