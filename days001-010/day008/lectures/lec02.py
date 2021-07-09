def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with("Jack Bauer", "Nowhere")
print()

greet_with("Nowhere", "Jack Bauer")
print()

greet_with(name="Angela", location="London")
print()

greet_with(location="London", name="Angela")
