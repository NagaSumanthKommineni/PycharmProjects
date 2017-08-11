from pytesting.PhoneBook import PhoneBook
import pytest

@pytest.fixture
def phonebook():
    return PhoneBook()

def test_add_and_lookup_entry(phonebook):
    phonebook.add("abc", 123)
    assert 123 == phonebook.lookup("abc")

def test_phonebook_provides_access_to_names_and_numbers(phonebook):
    phonebook.add("abc", 123)
    phonebook.add("def", 456)
    assert "abc", "def" in phonebook.names()
    assert 123, 456 in phonebook.numbers()

def test_missing_entry_raise_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Mark")


