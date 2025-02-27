import re

def normalize_phone(phone_number):
    '''
    normalizes phone numbers to a standard format.
    Args:
        phone_number (str): a string with a phone number in any format
    Returns:
        str: string with normalized phone number
    '''
    cleaned_number = re.sub(r'[^0-9]','', phone_number)
    return "+38" + cleaned_number.removeprefix("38")


if __name__ == "__main__":
    print(normalize_phone.__doc__)

    #print(normalize_phone("+380 44 123 4567"))

    assert normalize_phone("+380 44 123 4567") == "+380441234567"
    assert normalize_phone("380501234567") == "+380501234567"
    assert normalize_phone("(050)8889900") == "+380508889900"

    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)