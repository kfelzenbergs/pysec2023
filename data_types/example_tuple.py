profile = ("Kristaps", "Felzenbergs", "Teacher", ["Python for security engineers", "Cybersecurity policy"])

firstname, lastname, role, subjects = profile


print("name", firstname)
print("subjects", subjects)


profile_list = list(profile)
profile_list.insert(1, "<mid-name>")


profile = tuple(profile_list)

firstname, midname, lastname, role, subjects = profile

print("name", firstname)
print("midname", midname)
print("subjects", subjects)
