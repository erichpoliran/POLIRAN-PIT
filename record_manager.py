import os

FILE_NAME = 'patients.txt'

def add_patient(patient_id, name, age, gender, diagnosis):
    with open(FILE_NAME, 'a') as file:
        file.write(f"{patient_id},{name},{age},{gender},{diagnosis}\n")
    print("Patient record added.\n")

def view_patients():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    with open(FILE_NAME, 'r') as file:
        for line in file:
            print(line.strip())

def search_patient(pid):
    with open(FILE_NAME, 'r') as file:
        for line in file:
            if line.startswith(pid + ','):
                print("Record found:", line.strip())
                return
    print("Patient not found.")

def update_patient(pid, name, age, gender, diagnosis):
    lines = []
    updated = False
    with open(FILE_NAME, 'r') as file:
        for line in file:
            if line.startswith(pid + ','):
                lines.append(f"{pid},{name},{age},{gender},{diagnosis}\n")
                updated = True
            else:
                lines.append(line)
    with open(FILE_NAME, 'w') as file:
        file.writelines(lines)
    print("Patient record updated.\n" if updated else "Patient not found.")

def delete_patient(pid):
    lines = []
    deleted = False
    with open(FILE_NAME, 'r') as file:
        for line in file:
            if not line.startswith(pid + ','):
                lines.append(line)
            else:
                deleted = True
    with open(FILE_NAME, 'w') as file:
        file.writelines(lines)
    print("Patient record deleted.\n" if deleted else "Patient not found.")
