# Python Credit Card Validator

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# STEP 1 - Remove '-' or ' '
card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

# STEP 2 - Add all digits odd places from right to left
for x in card_number[::2]:
    sum_odd_digits += int(x)

# STEP 3 - Double every second digit from right to left
for x in card_number[1::2]:
    x = int(x)*2
    if x >= 10:
        sum_even_digits += (x%10) + 1
    else:
        sum_even_digits += x

# STEP 4 - Sum even and odd digits
total = sum_odd_digits + sum_even_digits

# STEP 5 - Validation
if total%10 == 0:
    print("Valid!")
else:
    print("INVALID!")

