def mask_card(card_number: str) -> str:
    """
    Маскирует номер карты (например, 1234567890123456).
    Оставляет 6 цифр в начале и 4 в конце.
    """
    # Убираем возможные пробелы
    if type(card_number) != str:
        raise ValueError
    cleaned = card_number.replace(" ", "")
    if len(cleaned) < 10:
        return "Неверный номер"
    return f"{cleaned[:4]} {cleaned[4:6]}** **** {cleaned[-4:]}"

def mask_account(account_number: str) -> str:
    """
    Маскирует номер счета (например, 40817810500000001234).
    Показывает последние 4 цифры.
    """
    cleaned = str(account_number).replace(" ", "")
    if len(cleaned) < 10:
        return "Неверный номер"
    return f"**{cleaned[-4:]}"

print(__name__)

if __name__ == "__main__":
    # Примеры использования
    card = "1234567890123456"
    account = "40817810500000001234"

    print(mask_card(card))
    print(mask_account(account))