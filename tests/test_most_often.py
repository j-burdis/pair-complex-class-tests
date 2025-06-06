import pytest
from lib.most_often import MostOften

def test_adds_one_new_integer():
    most_often = MostOften([])
    most_often.add_new(1)
    assert most_often.starting_list == [1]

def test_adds_one_new_string():
    most_often = MostOften([])
    assert most_often.starting_list == []
    most_often.add_new("hello")
    assert most_often.starting_list == ["hello"]

def test_get_most_often_numbers_list():
    most_often = MostOften([1, 2, 3, 3])
    assert most_often.get_most_often() == 3

def test_get_not_most_often_numbers_list():
    most_often = MostOften([1, 2, 3])
    assert most_often.get_most_often() == "no clear winner"

def test_get_most_often_mixed_list():
    most_often = MostOften([1, "b", 3, "b"])
    assert most_often.get_most_often() == "b"

def test_get_not_most_often_mixed_list():
    most_often = MostOften([1, "b", 3])
    assert most_often.get_most_often() == "no clear winner"

def test_add_new_empty_returns_error():
    most_often = MostOften([1, 2, 3])
    with pytest.raises(TypeError) as e:
        most_often.add_new()
    message = str(e.value)
    assert "missing 1 required positional argument" in message

def test_get_most_often_empty_list():
    most_often = MostOften([])
    assert most_often.get_most_often() == "no clear winner"