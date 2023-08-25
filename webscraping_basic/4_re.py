import re
# abcd, book, desk
# ca?e

p = re.compile("ca.e")
# . : means one letter> care, cafe, case | caffe(x)
# ^ : means start of a string> ^de : desk, destination (o) | fade(x)
# $ : means end of a string> se$ : case, base (o) | face(x)


def print_match(m):
    if m:
        print("m.group(): ", m.group())  # matched string
        print("m.string: ", m.string)  # input string
        print("m.start(): ", m.start())  # start index of matched string
        print("m.end(): ", m.end())  # end index of matched string
        print("m.span(): ", m.span())  # start and end index of matched string
    else:
        print("no match")


# m = p.match("case") #match: check if the input string matches the pattern
# print_match(m)


# search: check if the pattern is in the input string
# m = p.search("good care")
# print_match(m)

# find all the matched strings and return them as a list
lst = p.findall("good care cafe")
print(lst)


# 1. p = re.compile("needed pattern")
# 2. m = p.match("string to match")
# 3. m = p.search("string to match")
# 4. lst = p.findall("string to match")

# . : means one letter> care, cafe, case | caffe(x)
# ^ : means start of a string> ^de : desk, destination (o) | fade(x)
# $ : means end of a string> se$ : case, base (o) | face(x)
