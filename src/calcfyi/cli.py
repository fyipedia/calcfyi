"""Command-line interface for calcfyi."""

from __future__ import annotations

import json

import typer

from calcfyi.api import CalcFYI

app = typer.Typer(help="CalcFYI — Online calculators — financial, health and math API client.")


@app.command()
def search(query: str) -> None:
    """Search calcfyi.com."""
    with CalcFYI() as api:
        result = api.search(query)
        typer.echo(json.dumps(result, indent=2))
