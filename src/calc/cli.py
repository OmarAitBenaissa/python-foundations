"""Command-line interface for the calc package."""

import argparse
import sys
from collections.abc import Sequence
from decimal import Decimal, InvalidOperation

from calc.operations import UnknownOperatorError, compute


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="calc",
        description="Exact-precision Decimal calculator.",
    )
    parser.add_argument("a", help="left operand")
    parser.add_argument("operator", help="one of: + - * / **")
    parser.add_argument("b", help="right operand")
    return parser


def _parse_decimal(label: str, raw: str) -> Decimal:
    try:
        return Decimal(raw)
    except InvalidOperation as exc:
        raise SystemExit(f"error: {label} is not a valid number: {raw!r}") from exc


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    a = _parse_decimal("left operand", args.a)
    b = _parse_decimal("right operand", args.b)

    try:
        result = compute(a, args.operator, b)
    except UnknownOperatorError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    except ZeroDivisionError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())