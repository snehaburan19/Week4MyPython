patients = []

def add_patient():
    name = input("Enter Patient Name: ")
    patients.append(name)
    print("Patient Added Successfully")


def view_patients():
    if len(patients) == 0:
        print("No Patients Found")
    else:
        for p in patients:
            print(p)


def search_patient():
    name = input("Enter Patient Name: ")

    if name in patients:
        print("Patient Found")
    else:
        print("Patient Not Found")


while True:

    print("\n===== HOSPITAL MENU =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")