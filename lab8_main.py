import utils
from utils import average
from utils import build_username as make_user
import utils as u

# Tapşırıq 1
def print_student_card(name, group, year):
    print("Name: " + name)
    print("Group: " + group)
    print("Year: " + str(year))

print_student_card("Aysel Mammadova", "CE-101", 1)
print_student_card(year=2, name="Kamran Aliyev", group="CE-201")
# print_student_card("Aysel Mammadova", "CE-101") # Xəta verir: arqument çatmır

# Tapşırıq 4 (While dövrü)
students = []
while True:
    name = input("Name (quit to stop): ")
    if name.lower() == "quit":
        break
    score = int(input("Score: "))
    students.append(utils.make_student(name, score))

for s in students:
    print(s["name"] + ": " + str(s["score"]))

# Tapşırıq 7 (Modul import testləri)
print(utils.add_vat(200))
print(average(60, 70))
print(make_user("Nigar", "Hasanova"))
print(u.with_bonus([50, 95], 10))
