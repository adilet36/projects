import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("7. File I O/students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home":home})