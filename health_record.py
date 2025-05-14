import record_manager as rm

def menu():
    while True:
        print("\n==== Digital Health Record System ====")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            pid = input("Enter Patient ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender: ")
            diagnosis = input("Enter Diagnosis: ")
            rm.add_patient(pid, name, age, gender, diagnosis)

        elif choice == '2':
            rm.view_patients()

        elif choice == '3':
            pid = input("Enter Patient ID to search: ")
            rm.search_patient(pid)

        elif choice == '4':
            pid = input("Enter Patient ID to update: ")
            name = input("Enter new Name: ")
            age = input("Enter new Age: ")
            gender = input("Enter new Gender: ")
            diagnosis = input("Enter new Diagnosis: ")
            rm.update_patient(pid, name, age, gender, diagnosis)

        elif choice == '5':
            pid = input("Enter Patient ID to delete: ")
            rm.delete_patient(pid)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

menu()
