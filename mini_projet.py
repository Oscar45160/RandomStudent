import random

list_of_student = []
prenom = ""
choix = ""
menu = ""
list_secours = []
menu_random = ""
a = 5

while True:
    print("\tMenu")
    print("1 - Fill the list")
    print("2 - Draw student ")
    print("0 - Quit the app")
    menu = input()
    if menu == "1":
        while True:
            prenom = input("Enter the name of the student / Q to quit to menu : ")
            if list_of_student.count(prenom) > 0:
                print("This student is already registered !")
            elif prenom == "Q":
                break
            else:
                list_of_student.append(prenom)

        print("List of students : ", list_of_student)
        list_secours = list_of_student
        print(list_secours)

    elif menu == "2":
        while menu_random != "Q":
            menu_random = input("Tap enter to print a student / Q to quit to menu : ")
            if len(list_of_student) > 0:
                choix = random.choice(list_of_student)
                list_secours.append(choix)
                list_of_student.remove(choix)
                print(choix)
            else:
                list_of_student = list_secours
    elif menu == "0":
        break
