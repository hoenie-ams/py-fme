"""
Demo of best practices
"""
EUR_USD_EXCHANGE_RATE = 1.06

# Concatenated
streetname = "Main Street"
# camelCase
streetName = "..."
# PascalCase
StreetName = "..."
# kebab-case
# street-name = "..."
# snake_case
street_name = "..."


def convert(amount):
    return amount * 1.06


def convertEur2Usd(amount):
    return amount * 1.06


def convert_eur_to_usd(amount):
    """Converts using the current rate."""
    return amount * EUR_USD_EXCHANGE_RATE


print(convert_eur_to_usd(100))
print(convert_eur_to_usd.__doc__)