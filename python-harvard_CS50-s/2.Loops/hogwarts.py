"""
First task

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")

"""

students = [
    {"name": "Hermione", "house": "Gryffidor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffidor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffidor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")