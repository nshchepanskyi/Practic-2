import json
import os
import re


USERS_FILE = "users.json"


class User:
    def __init__(
        self,
        username,
        email,
        password,
    ):
        self.username = username
        self.email = email
        self.password = password


users = []


def load_users():
    global users

    if not os.path.exists(
        USERS_FILE
    ):
        with open(
            USERS_FILE,
            "w",
        ) as f:
            json.dump([], f)

    with open(
        USERS_FILE,
        "r",
    ) as f:
        data = json.load(f)

    users = []

    for item in data:
        users.append(
            User(
                item["username"],
                item["email"],
                item["password"],
            )
        )


def save_users():
    data = []

    for user in users:
        data.append(
            {
                "username": user.username,
                "email": user.email,
                "password": user.password,
            }
        )

    with open(
        USERS_FILE,
        "w",
    ) as f:
        json.dump(
            data,
            f,
            indent=4,
        )


def validate_email(email):
    pattern = (
        r"^[a-zA-Z0-9_.+-]+"
        r"@[a-zA-Z0-9-]+"
        r"\.[a-zA-Z0-9-.]+$"
    )

    return re.match(
        pattern,
        email,
    )


def validate_password(password):
    return len(password) >= 6


def validate_username(username):
    return len(username) >= 3


def register_user(
    username,
    email,
    password,
):
    load_users()

    if not validate_username(
        username
    ):
        return (
            False,
            "Username must contain at least 3 characters",
        )

    if not validate_email(email):
        return (
            False,
            "Invalid email",
        )

    if not validate_password(
        password
    ):
        return (
            False,
            "Password must contain at least 6 characters",
        )

    username_exists = next(
        (
            u
            for u in users
            if u.username == username
        ),
        None,
    )

    if username_exists:
        return (
            False,
            "Username already exists",
        )

    email_exists = next(
        (
            u
            for u in users
            if u.email == email
        ),
        None,
    )

    if email_exists:
        return (
            False,
            "Email already exists",
        )

    user = User(
        username,
        email,
        password,
    )

    users.append(user)

    save_users()

    return (
        True,
        "Registration successful",
    )


def login_user(
    login,
    password,
):
    load_users()

    user = next(
        (
            u
            for u in users
            if (
                u.username == login
                or u.email == login
            )
            and u.password == password
        ),
        None,
    )

    if not user:
        return (
            False,
            "Invalid credentials",
        )

    return (
        True,
        user,
    )