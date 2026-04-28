"""Tests for arithmetic operations."""

from decimal import Decimal

import pytest

from calc.operations import UnknownOperatorError, add, compute, divide, multiply, power, subtract


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


def test_power_raises_to_exponent() -> None:
    assert power(Decimal("2"), Decimal("10")) == Decimal("1024")


def test_compute_dispatches_addition() -> None:
    assert compute(Decimal("7"), "+", Decimal("3")) == Decimal("10")


def test_compute_dispatches_exponent() -> None:
    assert compute(Decimal("2"), "**", Decimal("8")) == Decimal("256")


def test_compute_unknown_operator_raises() -> None:
    with pytest.raises(UnknownOperatorError):
        compute(Decimal("1"), "?", Decimal("1"))


def test_compute_dispatches_square_root() -> None:
    assert compute(Decimal("16"), "sqrt", None) == Decimal("4")


def test_compute_dispatches_cube_root() -> None:
    assert compute(Decimal("27"), "cbrt", None) == Decimal("3")
