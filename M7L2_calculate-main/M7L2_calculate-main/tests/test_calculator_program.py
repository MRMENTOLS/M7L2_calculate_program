import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2


def test_calculate_subtraction():
    assert calculate(5, 3, '-') == 2


def test_calculate_multiplication():
    assert calculate(3, 4, '*') == 12


def test_calculate_division():
    assert calculate(8, 2, '/') == 4


def test_calculate_division_by_zero():
    assert calculate(5, 0, '/') == "Ошибка: Деление на ноль."


def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."


def test_calculate_negative_numbers_addition():
    assert calculate(-10, -5, '+') == -15


def test_calculate_mixed_number_types():
    assert calculate(3.5, 1.5, '+') == 5.0


def test_calculate_multiply_with_zero():
    assert calculate(7, 0, '*') == 0


def test_calculate_multiply_negative_and_positive():
    assert calculate(-4, 5, '*') == -20
'''
Задача. В настоящий момент реализовано три unit-теста
Проверяется корректность работы калькулятора для действий сложения, деления и неизвестной операции
Необходимо, как минимум, добавить тесты для следующих операций:
1. Вычитание
2. Умножение
Но будет круто, если ты сможешь придумать и добавить дополнительные тесты
'''
