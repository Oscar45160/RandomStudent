import random

list_of_student = []
prenom = ""
choix = ""
list_secours = []
menu_random = ""
a = 5

menu = {
    "1": "Fill the list",
    "2": "Draw student",
    "0": "Quit the app"
}

while True:
    for key, value in menu.items():
        print(key, value)
    choice = input("Select a number to navigate trough the menu ")
    print(menu.get(choice, "The nomber is out of range"))
    if menu(choice) == "1":
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
