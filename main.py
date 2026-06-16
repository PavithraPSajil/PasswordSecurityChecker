from password_checker import check_password
from password_generator import generate_password

print("================================")
print(" PASSWORD STRENGTH ANALYZER")
print("================================")

password = input("Enter Password: ")

result = check_password(password)

print("\nPassword Analysis")
print("---------------------------")

for key, value in result.items():
    print(f"{key}: {value}")

if result["Strength"] != "Very Strong":
    print("\nSuggested Strong Password:")
    print(generate_password())

print("\nThank you for using the Password Strength Analyzer.")