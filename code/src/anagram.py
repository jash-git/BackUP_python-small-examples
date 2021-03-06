from collections import Counter

# 检查两个字符串是否 相同字母异序词，简称：互为变位词


def anagram(str1, str2):
    return Counter(str1) == Counter(str2)


anagram('eleven+two', 'twelve+one')  # True 这是一对神器的变位词
anagram('eleven', 'twelve')  # False
