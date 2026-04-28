from collections.abc import Callable
from decimal import Decimal
from math import exp as math_exp


def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b


def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b


def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b


def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def power(a: Decimal, b: Decimal) -> Decimal:
    return a**b


def square_root(a: Decimal) -> Decimal:
    return a ** Decimal("0.5")


def cube_root(a: Decimal) -> Decimal:
    return a ** (Decimal(1) / Decimal(3))


def exponential(a: Decimal) -> Decimal:
    return Decimal(math_exp(a))


class UnknownOperatorError(ValueError):  # fix: inherit from ValueError, not `value`
    """Raised when an operator symbol has no known implementation."""


_OPERATIONS: dict[str, Callable[..., Decimal]] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    "sqrt": square_root,
    "cbrt": cube_root,
    "exp": exponential,
}

# Unary operators that only take one operand
_UNARY_OPERATORS = {"sqrt", "cbrt", "exp"}


def compute(a: Decimal, operator: str, b: Decimal | None) -> Decimal:
    try:
        impl = _OPERATIONS[operator]
    except KeyError as exc:  # fix: `except` + `KeyError`
        raise UnknownOperatorError(f"Unknown operator: {operator}") from exc

    if operator in _UNARY_OPERATORS:  # fix: don't pass `b` to unary ops
        return impl(a)
    return impl(a, b)
