class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


user1 = User("001", "angela")
user2 = User("002", "jack")

# TypeError
# user3 = User()

print(f'user1.id: {user1.id}, user1.username: {user1.username}, user1.followers: {user1.followers}')
print(f'user2.id: {user2.id}, user2.username: {user2.username}, user2.followers: {user2.followers}')
