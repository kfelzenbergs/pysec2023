# https://www.w3schools.com/js/js_json_datatypes.asp

people = []
subjects = [
    "Python for Security Engineers",
    "Cybersecurity Policy"
]

profile_kristaps = {
    "name": "Kristaps",
    "role": "Teacher"
}

profile_anna = {
    "name": "Anna",
    "role": "Student"
}

profile_kristaps["subjects"] = subjects
# profile_anna["subjects"] = []

people.append(profile_kristaps)
people.append(profile_anna)

print(people)

for profile in people:
    for attribute, value in profile.items():
        print(attribute, value)


i = 0
while i < len(people):
    print(people[i])
    i +=1
else:
    print("empty or no more people to iterate")


for profile in people:
    if "subjects" in profile:
        subjects = profile["subjects"]
    elif "" in profile:
        # just a placeholder, does nothing
        pass

        # exits the inner most loop
        exit

        # continues with the next iteration
        continue
    else:
        subjects = []
    
    print('''
    ----------- profile -----------
    -- name: {}
    -- role: {}
    -- subjects: {}
    
    '''.format(profile['name'], profile['role'], subjects))


for profile in people:
    print('\n----------- profile -----------')
    for attribute, value in profile.items():
        print('-- {}: {}'.format(attribute, value))
