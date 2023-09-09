

a_sentence = "Hello world!"
a_sentence = 'Hellow world!'
a_multi_line_sentence = '''
This is one line
   and this is another
'''

multi_l_string = 'Hello \n world!'
raw_string = r'Hello \n world!'

# print(a_multi_line_sentence)
print(multi_l_string)
print(raw_string)


teikums = u"Šodien braucu ar trīspatsmito tramvaju!"
print(teikums)


a = "abc"
print(a*20)

print(teikums[6:])

# get last symbol of text string
print(teikums[-1])


letters = ["a", "b", "c", "d"]
print("last char is ", letters[-1])
print("last char is ", letters[len(letters)-1])


print(teikums.split(" "))


# syntax of format function

sentence = "name {} lastname {} age {}".format("kristaps", "felzenbergs", "32")
print(sentence)

sentence = "name {0} lastname {0} age {1}".format("kristaps", "felzenbergs")
print(sentence)


profile = {"name": "kristaps", "lastname": "felzenbergs", "age": 32}
sentence = "name {} lastname {} age {}".format(*profile.values())
print(sentence)

sentence = "name {name} lastname {lastname} age {age}".format(name="kristaps", lastname="felzenbergs", age=32)
print(sentence)

name = "kristaps"
print(f"my names is {name}")
