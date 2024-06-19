courses = ["Computer Science", "IT", "Software Engineering"]
print(courses)

# Accessing an element in an array
print(courses[1])

# looping through an array
for x in courses:
    print(x)


# adding a new element in an array-method
courses.append("Datascience")
for x in courses:
    print(x)

# Deleting an element in an array-method
courses.remove("IT")
print(courses)
