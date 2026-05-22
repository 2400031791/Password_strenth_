import string

password = input("Enter Password: ")

score = 0

# Length Check
if len(password) >= 8:
    score += 1
else:
    print("❌ Password should contain at least 8 characters")

# Uppercase Check
if any(char.isupper() for char in password):
    score += 1
else:
    print("❌ Add uppercase letters")

# Lowercase Check
if any(char.islower() for char in password):
    score += 1
else:
    print("❌ Add lowercase letters")

# Number Check
if any(char.isdigit() for char in password):
    score += 1
else:
    print("❌ Add numbers")

# Special Character Check
if any(char in string.punctuation for char in password):
    score += 1
else:
    print("❌ Add special characters")

# Final Result
print("\nPassword Strength Result:")

if score <= 2:
    print("🔴 Weak Password")
elif score <= 4:
    print("🟡 Medium Password")
else:
    print("🟢 Strong Password")