import pytest
from StringUtil import StringUtils

# Создаем экземпляр класса для использования в тестах
utils = StringUtils()

# Тесты для метода capitalize
def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"  # Первая буква становится заглавной
    assert utils.capitalize("SkyPro") == "Skypro"  # Остальные буквы в нижнем регистре
    assert utils.capitalize("hello world") == "Hello world"  # Только первое слово меняется

def test_capitalize_negative():
    assert utils.capitalize(" skypro") == " skypro"  # Пробел не должен измениться
    assert utils.capitalize("") == ""  # Пустая строка
    assert utils.capitalize("   ") == "   "  # Строка, состоящая только из пробелов

# Тесты для метода trim
def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"  # Пробелы удалены
    assert utils.trim("skypro") == "skypro"  # Без пробелов

def test_trim_negative():
    assert utils.trim("") == ""  # Пустая строка
    assert utils.trim("   ") == ""  # Строка только из пробелов

# Тесты для метода to_list
def test_to_list_positive():
    assert utils.to_list("a,b,c") == ["a", "b", "c"]  # Разделение по запятой
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]  # Разделение по указанному разделителю

def test_to_list_negative():
    assert utils.to_list("") == []  # Пустая строка
    assert utils.to_list("abc") == ["abc"]  # Без разделителей
    assert utils.to_list("1,2,3", ":") == ["1,2,3"]  # Разделитель не найден

# Тесты для метода contains
def test_contains_positive():
    assert utils.contains("SkyPro", "S") is True  # Символ найден
    assert utils.contains("SkyPro", "Pro") is True  # Подстрока найдена

def test_contains_negative():
    assert utils.contains("SkyPro", "X") is False  # Символ не найден
    assert utils.contains("", "S") is False  # Пустая строка
    with pytest.raises(TypeError):  # Проверка на None
        utils.contains(None, "S")

# Тесты для метода delete_symbol
def test_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"  # Удаление символа
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"  # Удаление подстроки

def test_delete_symbol_negative():
    assert utils.delete_symbol("SkyPro", "X") == "SkyPro"  # Символ не найден
    assert utils.delete_symbol("", "X") == ""  # Пустая строка

# Тесты для метода starts_with
def test_starts_with_positive():
    assert utils.starts_with("SkyPro", "S") is True  # Начинается с символа
    assert utils.starts_with("SkyPro", "Sky") is True  # Начинается с подстроки

def test_starts_with_negative():
    assert utils.starts_with("SkyPro", "P") is False  # Не начинается с символа
    assert utils.starts_with("", "S") is False  # Пустая строка

# Тесты для метода end_with
def test_end_with_positive():
    assert utils.end_with("SkyPro", "o") is True  # Заканчивается символом
    assert utils.end_with("SkyPro", "Pro") is True  # Заканчивается подстрокой

def test_end_with_negative():
    assert utils.end_with("SkyPro", "S") is False  # Не заканчивается символом
    assert utils.end_with("", "o") is False  # Пустая строка

# Тесты для метода is_empty
def test_is_empty_positive():
    assert utils.is_empty("") is True  # Пустая строка
    assert utils.is_empty("   ") is True  # Строка только из пробелов

def test_is_empty_negative():
    assert utils.is_empty("SkyPro") is False  # Строка с символами
    assert utils.is_empty("  SkyPro  ") is False  # Пробелы и символы

# Тесты для метода list_to_string
def test_list_to_string_positive():
    assert utils.list_to_string([1, 2, 3]) == "1, 2, 3"  # Соединение чисел
    assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"  # Соединение строк

def test_list_to_string_negative():
    assert utils.list_to_string([]) == ""  # Пустой список
    assert utils.list_to_string([1]) == "1"  # Один элемент списка
