#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't (140 chars max).

Judge angle: a one-line weather forecast for an invented city, the city
named, the weather the whole point, in the rhythm of a real broadcast
forecast bent just enough to smile at. Velmora gets one concrete detail of
its life -- a parade of lost umbrellas crossing Main Street -- so it feels
like a place, and the forecast register ("sunny with a chance of...") does
the smiling.
"""

import os

GATE = 140

CITY = "VELMORA"
SKY = "sunny with a chance of confetti"
DETAIL = "the parade of lost umbrellas crosses Main Street at noon"


def forecast(city, sky, detail):
    """A broadcast forecast: CITY: sky. Expect delays -- the local detail."""
    return f"{city}: {sky}. Expect delays — {detail}."


def check_forecast(line):
    """The sealed gate: 1..140 UTF-8 characters, not only whitespace."""
    assert line.strip(), "entry must not be blank"
    assert 1 <= len(line) <= GATE, f"entry is {len(line)} chars, gate is {GATE}"
    assert line.startswith("VELMORA:"), "the invented city must be named first"
    assert "parade" in line, "the city needs one concrete detail of its life"
    assert "Expect delays" in line, "must keep the forecast register"
    # A forecast is one sentence of sky plus one of consequence.
    assert line.count(".") == 2, "forecast must be exactly two sentences"
    return line


def main():
    line = check_forecast(forecast(CITY, SKY, DETAIL))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
