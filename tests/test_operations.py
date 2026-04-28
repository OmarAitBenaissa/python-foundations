"""Tests for arithmetic operations."""

from decimal import Decimal

import pytest

from calc.operations import add, divide, multiply, subtract


def test_add_two_positives() -> None:
    assert add(Decimal("1.5"), Decimal("2.5")) == Decimal("4.0")


def test_add_negative_and_positive() -> None:
    assert add(Decimal("-3"), Decimal("1")) == Decimal("-2")


def test_subtract_yields_negative() -> None:
    assert subtract(Decimal("1.5"), Decimal("2.5")) == Decimal("-1.0")


def test_multiply_decimals() -> None:
    assert multiply(Decimal("1.5"), Decimal("2.5")) == Decimal("3.75")


def test_divide_clean_division() -> None:
    assert divide(Decimal("6"), Decimal("2")) == Decimal("3")


def test_divide_by_zero_raises() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(Decimal("1"), Decimal("0"))
