"""MCP server for calcfyi."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from calcfyi.api import CalcFYI

mcp = FastMCP("calcfyi")


@mcp.tool()
def search_calcfyi(query: str) -> dict[str, Any]:
    """Search calcfyi.com for content matching the query."""
    with CalcFYI() as api:
        return api.search(query)
