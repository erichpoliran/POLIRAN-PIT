FILE_NAME = "patient_records.txt"

# Check if the file exists, if not create it
def check_file():
    try:
        with open(FILE_NAME, "x") as file:
            print("File created successfully!")
    except FileExistsError:
        print("File already exists.")

# Add a new patient record
def add_patient(patient_id, name, age, gender, condition):
    try:
        with open(FILE_NAME, "a") as file:
            file.write(f"Patient ID: {patient_id}\n")
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Gender: {gender}\n")
            file.write(f"Condition: {condition}\n")
            file.write("-" * 30 + "\n")  # Separate records with a line
        print("Patient record added successfully!")
    except Exception as e:
        print(f"Error occurred while adding patient: {e}")

# Retrieve a patient's record by ID
def retrieve_patient(patient_id):
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
            found = False
            for i in range(0, len(lines), 6):  # Each patient record consists of 5 lines
                if f"Patient ID: {patient_id}" in lines[i]:
                    found = True
                    print("".join(lines[i:i+5]))  # Print the 5 lines that belong to the patient
                    break
            if not found:
                print("Patient ID not found.")
    except Exception as e:
        print(f"Error occurred while retrieving patient: {e}")

# Update a patient's condition
def update_patient_condition(patient_id, new_condition):
    try:
        updated = False
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        for i in range(len(lines)):
            if f"Patient ID: {patient_id}" in lines[i]:
                updated = True
                lines[i + 4] = f"Condition: {new_condition}\n"  # Update the condition line
                break

        if updated:
            with open(FILE_NAME, "w") as file:
                file.writelines(lines)  # Write the updated content back to the file
            print("Patient condition updated successfully!")
        else:
            print("Patient ID not found.")
    except Exception as e:
        print(f"Error occurred while updating patient: {e}")

# Delete a patient's record
def delete_patient_record(patient_id):
    try:
        found = False
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        new_lines = []
        for i in range(0, len(lines), 6):  # Check for each patient's 6 lines
            if f"Patient ID: {patient_id}" not in lines[i]:
                new_lines.extend(lines[i:i+6])  # Add non-matching records to the new list
            else:
                found = True

        if found:
            with open(FILE_NAME, "w") as file:
                file.writelines(new_lines)  # Write the remaining records back to the file
            print(f"Patient ID {patient_id} record deleted.")
        else:
            print("Patient ID not found.")
    except Exception as e:
        print(f"Error occurred while deleting patient: {e}")

# List all patient records
def list_all_patients():
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 6):  # Each patient record spans 6 lines
                print("".join(lines[i:i+5]))  # Print each patient record
                print("-" * 30)
    except Exception as e:
        print(f"Error occurred while listing patients: {e}")
