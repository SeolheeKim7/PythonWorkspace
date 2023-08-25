# lst = [1, 2, 3, 4, 5]
# print(lst)
# lst.reverse()
# print(lst)

# lst2 = [1, 2, 3, 4, 5]
# print("before reverse :", lst2)

# lst3 = reversed(lst2)
# print("after reverse :", lst2)
# print("after reverse lst3:", list(lst3))


eng = ["apple", "banana", "orange"]
kor = ["1", "2", "3"]

print(list(zip(eng, kor)))

mixed = [('apple', '1'), ('banana', '2'), ('orange', '3')]
print(list(zip(*mixed)))
