year = int(input("What's your year of birth? "))

# Play Computer
# If year is 1994 the user isn't classified as anything.
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")
