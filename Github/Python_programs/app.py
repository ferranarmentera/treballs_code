
# strings practiques
students_count = 1000
rating = 4.88
is_publish = False
course_name = "Python Programming"
print(course_name)
print(len(course_name))
print(course_name[0])
print(course_name[-1])
print(course_name[0:3])
print(course_name[0:])
print(course_name[:3])
print(course_name[:])

# escape sequences \"  \'   \\  \n
course_name = "Pyton \"Program"  # imprimira "
#course_name = 'Pyton "Program'
# course_name = "Pyton" \n "Program"
#course_name = "Pyton \"Program"
print(course_name)
# format strings
first = "Ferran"
last = "Colell"
full = first + " " + last

# alternative way with formatted strings
full = f"{first} {last}"
print(full)
# string Methods
course = "Pytohn Programing"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("Pro"))
print(course.repace("p", "J"))
