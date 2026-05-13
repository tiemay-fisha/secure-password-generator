import random
import string

print("  SECURE PASSWORD GENERATOR SYSTEM 🔐 ")
print("=================================================\n")

print("This system generates secure passwords based on user-defined rules.")
print("It evaluates strength and promotes cybersecurity awareness.\n")

history = []


# ================= PASSWORD GENERATOR =================

def generate_password(length, upper, lower, digits, symbols):
    password = []
    pool = ""

    # FORCE at least one from selected types
    if lower:
        password.append(random.choice(string.ascii_lowercase))
        pool += string.ascii_lowercase
    if upper:
        password.append(random.choice(string.ascii_uppercase))
        pool += string.ascii_uppercase
    if digits:
        password.append(random.choice(string.digits))
        pool += string.digits
    if symbols:
        password.append(random.choice(string.punctuation))
        pool += string.punctuation

    if pool == "":
        return None

    for _ in range(length - len(password)):
        password.append(random.choice(pool))

    random.shuffle(password)
    return "".join(password)


# ================= STRENGTH CHECK =================

def check_strength(password):
    score = 0
    feedback = []

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Include lowercase letters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Include uppercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include numbers")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Include symbols")

    return score, feedback


# ================= INPUT HANDLING =================

def ask_yes_no(text):
    while True:
        ans = input(text + " (y/n): ").lower().strip()
        if ans in ["y", "n"]:
            return ans == "y"
        print("⚠ Please enter y or n only")


def get_length():
    while True:
        try:
            length = int(input("Enter password length (min 6): ").strip())
            if length < 6:
                print("⚠ Minimum length is 6")
                continue
            return length
        except:
            print("⚠ Invalid input")


# ================= MODE =================

def choose_mode():
    print("\nSelect Mode:")
    print("1. Strong Password Generator 🔐")
    print("2. PIN Generator (4-digit) ")

    while True:
        choice = input("Choose (1/2): ").strip()

        if choice == "1":
            return "password"
        elif choice == "2":
            return "pin"
        else:
            print("⚠ Choose 1 or 2 only")


def generate_pin():
    return str(random.randint(1000, 9999))


# ================= MAIN PROGRAM =================

def main():

    mode = choose_mode()

    if mode == "pin":
        pin = generate_pin()

        print("\n================ RESULT ================")
        print("Generated PIN:", pin)
        print("Warning ⚠: PINs are less secure than passwords")
        print("========================================\n")

        history.append(pin)

    else:

        length = get_length()

        upper = ask_yes_no("Include uppercase letters?")
        lower = ask_yes_no("Include lowercase letters?")
        digits = ask_yes_no("Include numbers?")
        symbols = ask_yes_no("Include symbols?")

        if not (upper or lower or digits or symbols):
            print("\n⚠ Error: You must select at least one option")
            return

        password = generate_password(length, upper, lower, digits, symbols)
        score, feedback = check_strength(password)

        history.append(password)
        if len(history) > 5:
            history.pop(0)

        print("\n================ RESULT ================")
        print("Generated Password:", password)
        print("Strength Score:", f"{score}/4")

        if score == 4:
            print("Status: Strong 🔐")
        elif score == 3:
            print("Status: Medium ⚠")
        else:
            print("Status: Weak ❌")

        print("========================================\n")

        if feedback:
            print("IMPROVEMENT SUGGESTIONS:")
            for f in feedback:
                print("-", f)

        print("\nCYBERSECURITY TIPS:")
        print("- Use 12+ character passwords")
        print("- Never reuse passwords")
        print("- Enable 2FA 🔐")
        print("- Avoid personal information")
        print("- Use password managers")

    # ================= FINAL MESSAGE =================
    print("\n========================================")
    print(" THANK YOU FOR USING THIS SYSTEM 🙏 ")
    print(" Your security awareness matters 🔐 ")
    print(" Stay safe in the digital world 🌍 ")
 


# ================= RUN =================

if __name__ == "__main__":
    main()
