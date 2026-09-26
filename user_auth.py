users = {
    "admin": "1234"
}

def login(username, password):
    if username in users and users[username] == password:
        return "Login successful"
    return "Invalid username or password"