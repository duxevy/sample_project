from src.masks import mask_account, mask_card

def mask_account_card(numbers: str) -> str:
    splitted_numbers = numbers.split()
    numbers_type = " ".join(splitted_numbers[:-1])
    digits = splitted_numbers[-1]
    if len(digits) > 16:
        digits = mask_account(digits)
    else:
        digits = mask_card(digits)
    result = f"{numbers_type} {digits}"
    return result

if __name__ == "__main__":
    print(mask_account_card("Счёт 1234567890123456123"))