password = input("Enter a password to validate: ")
is_valid = True

if len(password) < 8:
    print(" Failed: Password is too short (Must be at least 8 characters).")
    is_valid = False

has_upper = False
if "A" in password or "B" in password or "C" in
password or "D" in password or "E" in password or "F" in password or "G" in password or "H" in password 
or "I" in password or "J" in password or "K" in password or "L" in password or "M" in password or "N" in password or 
"O" in password or "P" in password or "Q" in password or "R" in password or "S" in password or "T" in password or "U" in password 
or "V" in password or "W" in password or "X" in password or "Y" in password or "Z" in password:
    has_upper = True

if has_upper == False:
    print(" Failed: Missing an uppercase letter (A-Z).")
    is_valid = False


has_digit = False
if "0" in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password 
or "6" in password or "7" in password or "8" in password or "9" in password:
    has_digit = True

if has_digit == False:
    print(" Failed: Missing a number (0-9).")
    is_valid = False


if "123456" in password:
    print(" Failed: Contains a prohibited pattern ('123456').")
    is_valid = False


if "aaa" in password or "bbb" in password or "ccc" in password or "111" in password or "000" in password:
    print(" Failed: Contains repeating characters in a row .")
    is_valid = False


if is_valid == True:
    print("Success: Your password is secure and meets all rules!")
else:
    print("Result: Password rejected. Please fix the errors above.")
