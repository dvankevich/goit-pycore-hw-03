import task01, task02, task03, task04

print("--- TASK 01 ---")
print("до нового року залишилось -", task01.get_days_from_today("2026-01-01"), "день/днів")
print("до 28-02-2025", task01.get_days_from_today("2025-02-28") )
print("goit-pycore-hw-03 deadline to go", task01.get_days_from_today("2025-03-10"))
print("\n")
print("--- TASK 02 ---")
print("Результати розіграшу лотереї:")
print("5 з 36", task02.get_numbers_ticket(1,36,5))
print("6 з 49", task02.get_numbers_ticket(1,49,6))
print("\n")
print("--- TASK 03 ---")
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

sanitized_numbers = [task03.normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:\n", sanitized_numbers)
assert sanitized_numbers == ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']

print("\n")
print("--- TASK 04 ---")
users = [
{"name": "John Doe", "birthday": "1985.01.23"},
{"name": "Jane Smith", "birthday": "1990.02.27"},
{"name": "Jonh Connor", "birthday": "1990.03.02"},
{"name": "Sarah Connor", "birthday": "1970.05.18"}
]

upcoming_birthdays = task04.get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:\n", upcoming_birthdays)