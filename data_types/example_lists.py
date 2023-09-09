

# numbers = [ 0, 1, 2, 3, 4 ]
# print(numbers)

# strings = [ "one", "two", "etc.." ]
# print(strings)

# combined = numbers + strings
# print(combined)

# extra_combined = [ 0, "text", [0,1,2], {"kris": "taps"}, ("a", "b", "c") ]
# print(extra_combined)

# print("size of extra_combined is: {}".format(len(extra_combined)))


# extra_combined.append("another string")
# print(extra_combined)


# extra_combined.extend(strings)
# print(extra_combined)

# extra_combined.pop(0)
# print(extra_combined)

# extra_combined.insert(1, "here I insert")
# print(extra_combined)

description = '''
Here we learn list data type in Python
More examples will follow
'''

books = [
    "F. Scott Fitzgerald, 'The Great Gatsby'",
    "Emily Brontë, 'Wuthering Heights' Emily Brontë, 'Wuthering Heights'",
    "Margaret Atwood, 'The Handmaid's Tale'",
    "Chinua Achebe, 'Things Fall Apart'"
]



# print(books)
books.sort(reverse=False)

# ordered list of books
for book in books:
    print(book)


print(description)
