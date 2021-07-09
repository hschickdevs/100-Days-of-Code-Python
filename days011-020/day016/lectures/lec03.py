from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)

print(f'alignment: {table.align}')
table.align = 'l'
print(f'alignment: {table.align}')
print(table)
