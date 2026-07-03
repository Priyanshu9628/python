import secrets


def generate_random_number(start=1, end=100):
    return secrets.randbelow(end - start + 1) + start


if __name__ == "__main__":
    print(generate_random_number())
