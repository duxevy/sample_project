import pytest
from src.masks import mask_account, mask_card

@pytest.mark.parametrize("account_numbers, masked_account", [
    ("40817810500000001234", "**1234"),
    ("90617810512005001871", "**1871"),
    ("11117812500400001294", "**1294"),
    ("111178", "Неверный номер"),
])
def test_mask_account(account_numbers, masked_account):
    result = mask_account(account_numbers)
    expected = masked_account
    assert result == expected

@pytest.mark.parametrize("card_numbers, masked_card", [
    ("4081781050001234", "4081 78** **** 1234"),
    ("9061781051201871", "9061 78** **** 1871"),
    ("1111781200001294", "1111 78** **** 1294"),
    ("111178", "Неверный номер"),
])
def test_mask_card(card_numbers, masked_card):
    result = mask_card(card_numbers)
    expected = masked_card
    assert result == expected

def test_mask_card_error():
    with pytest.raises(ValueError):
        result = mask_card(1234567890)