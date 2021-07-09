pages = 0
word_per_page = 0

# #Print is Your Friend
# Notice the == instead of =.
# word_per_page is never changed.

print(f'pages: {pages}')
print(f'word_per_page: {word_per_page}')

pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))

print(f'pages: {pages}')
print(f'word_per_page: {word_per_page}')

total_words = pages * word_per_page
print(total_words)
print()

# Fixing it...
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
