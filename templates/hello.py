def greet_user(name):
    """
    Greet a user by name.

    Args:
        name (str): The user's name.

    Returns:
        str: A greeting message.
    """
    message = f"Hello, {name}!"
    return message


def main():
    users = ["Alice", "Bob", "Charlie"]
    for user in users:
        greeting = greet_user(user)
        print(greeting)
        if user == "Bob":
            print("Special welcome for Bob!")


if __name__ == "__main__":
    main()
