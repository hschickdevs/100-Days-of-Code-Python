class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, other):
        other.followers += 1
        self.following += 1


user1 = User("001", "angela")
user2 = User("002", "jack")

print(f'user1.id: {user1.id}, user1.username: {user1.username}, '
      f'user1.followers: {user1.followers}, user1.following: {user1.following}')
print(f'user2.id: {user2.id}, user2.username: {user2.username}, '
      f'user2.followers: {user2.followers}, user2.following: {user2.following}')

user1.follow(user2)

print(f'user1.id: {user1.id}, user1.username: {user1.username}, '
      f'user1.followers: {user1.followers}, user1.following: {user1.following}')
print(f'user2.id: {user2.id}, user2.username: {user2.username}, '
      f'user2.followers: {user2.followers}, user2.following: {user2.following}')
