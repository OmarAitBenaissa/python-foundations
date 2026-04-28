"""Tests for the CLI entry point."""

import pytest

from calc.cli import main


def test_main_addition_prints_result(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["7", "+", "3"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "10"


def test_main_exponent(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["2", "**", "10"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "1024"


def test_main_unknown_operator_returns_2(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["1", "?", "1"])
    captured = capsys.readouterr()
    assert exit_code == 2
    assert "Unknown operator" in captured.err


def test_main_division_by_zero_returns_1(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["1", "/", "0"])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "division by zero" in captured.err


def test_main_invalid_number_exits(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit):
        main(["7x", "+", "3"])
