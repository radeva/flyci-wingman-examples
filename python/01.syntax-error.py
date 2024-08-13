# main.py

def main():
    employees = {"pam": 30,
                "jim": 28}

    for name, age in employees.items():
        print(f"{name.capitalize()} is {age} years old.")
        
if __name__ == "__main__":
    main()
