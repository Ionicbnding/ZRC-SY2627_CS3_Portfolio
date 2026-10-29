
# Parent class
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    # Getter methods
    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        if bill_amount >= 0:
            self.__bill_amount = bill_amount
        else:
            print("Invalid bill amount.")

    # Calculate full bill
    def calculate_bill(self):
        return self.__bill_amount


# Child class: SeniorPatient
class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


# Child class: PhilHealthPatient
class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


# Create objects
regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)


# Display patient bills
patients = [
    regular_patient,
    senior_patient,
    philhealth_patient
]

for patient in patients:
    print("\nPatient Name:", patient.get_name())
    print("Original Bill: PHP", patient.get_bill_amount())
    print("Final Bill: PHP", patient.calculate_bill())
