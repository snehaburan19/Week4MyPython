class Patient:
    def __init__(self, patient_id, name):
        self.__patient_id = patient_id
        self.name = name

    def display(self):
        print("Patient ID:", self.__patient_id)
        print("Patient Name:", self.name)


class Doctor(Patient):   # Inheritance

    def __init__(self, patient_id, name, specialization):
        super().__init__(patient_id, name)
        self.specialization = specialization

    def show(self):
        self.display()
        print("Specialization:", self.specialization)


# Object 1
p1 = Patient(1, "Sneha")
p1.display()

print("----------------")

# Object 2
d1 = Doctor(101, "Dr. Sharma", "Cardiology")
d1.show()

##OOP Concepts Used
#Constructor -----> __init__()
#Inheritance -----> Doctor(Patient)
#Encapsulation -----> __patient_id
#Objects -----> p1,  d1