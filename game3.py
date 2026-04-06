from game2 import start
f = open("users.txt")
users = {}
for user in f:
    name, money = user.split()
    users[name] = int(money)
username = input("Введите свое имя для входа в аккаунт: ")
if username in users:
    print(f"У вас на балансе: {users[username]}")
else:
    print("Привет новый пользователь")
    users[username] = 1000
f = open("users.txt", "w+")
print(users)
users[username] = start(users[username])
for name in users:
    f.write(name + " " + str(users[name]) + "\n")
