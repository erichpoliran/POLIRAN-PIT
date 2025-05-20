import patient_records  # type: ignore

def main():
    patient_records.check_file()  

    while True:
        print("\n--- Digital Health Record System---")
        print("1. Add Patient Record")
        print("2. Retrieve Patient Record")
        print("3. List All Patient Records")
        print("4. Update Patient Condition")
        print("5. Delete Patient Record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = input("Enter Patient Age: ")
            gender = input("Enter Patient Gender: ")
            condition = input("Enter Patient Condition: ")
            patient_records.add_patient(patient_id, name, age, gender, condition)

        elif choice == "2":
            patient_id = input("Enter Patient ID to retrieve: ")
            patient_records.retrieve_patient(patient_id)

        elif choice == "3":
            patient_records.list_all_patients()

        elif choice == "4":
            patient_id = input("Enter Patient ID to update: ")
            new_condition = input("Enter New Condition: ")
            patient_records.update_patient_condition(patient_id, new_condition)

        elif choice == "5":
            patient_id = input("Enter Patient ID to delete: ")
            patient_records.delete_patient_record(patient_id)

        elif choice == "6":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
