user1 = {
    "Tom":19,
    "john":34,
    "Ray":21
}

user2 = {
    "Hulk":45,
    "Spidy":20,
    "Robert":30
}

# method 1
users = user1 | user2
# method 2
users1 = {**user1,**user2}
# output
print(users)
print(users1)