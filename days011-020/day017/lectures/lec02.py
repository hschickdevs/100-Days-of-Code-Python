class User:
    def __init__(self):
        print("New User being created...")


user1 = User()
user2 = User()

user1.id = "001"
user1.username = "angela"
print(f'user1.id: {user1.id}, user1.username: {user1.username}')

user2.id = "002"
user2.username = "jack"
print(f'user2.id: {user2.id}, user2.username: {user2.username}')
