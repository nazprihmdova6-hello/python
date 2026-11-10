from utils import make_student

def add_student(students, name, score):
    students.append(make_student(name, score))

def average_score(students):
    if not students:
        return 0
    return sum(s["score"] for s in students) / len(students)

def top_student(students):
    if not students:
        return None
    top = students[0]
    for s in students:
        if s["score"] > top["score"]:
            top = s
    return top

students = []
while True:
    choice = input("Choice: ")
    if choice == "1":
        name = input("Name: ")
        score = int(input("Score: "))
        add_student(students, name, score)
    elif choice == "2":
        for s in students:
            print(s["name"] + ": " + str(s["score"]))
        print("Average: " + str(average_score(students)))
        top = top_student(students)
        if top:
            print("Top student: " + top["name"] + " (" + str(top["score"]) + ")")
    elif choice == "3":
        break
