"""
Demo of pylint

Types:
- Conventions
- Refactorings
- Warnings
- Errors
- Fatal
"""


def main():
    print(convert_eur_to_usd(500))


def convert_eur_to_usd(amount):
    result = amount * 1.06
    return result


if __name__ == "__main__":
    main()
