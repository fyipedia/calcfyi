"""MCP server for calcfyi — AI assistant tools for calcfyi.com.

Run: uvx --from "calcfyi[mcp]" python -m calcfyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CalcFYI")


@mcp.tool()
def list_formulas(limit: int = 20, offset: int = 0) -> str:
    """List formulas from calcfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from calcfyi.api import CalcFYI

    with CalcFYI() as api:
        data = api.list_formulas(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No formulas found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_formula(slug: str) -> str:
    """Get detailed information about a specific formula.

    Args:
        slug: URL slug identifier for the formula.
    """
    from calcfyi.api import CalcFYI

    with CalcFYI() as api:
        data = api.get_formula(slug)
        return str(data)


@mcp.tool()
def list_scenarios(limit: int = 20, offset: int = 0) -> str:
    """List scenarios from calcfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from calcfyi.api import CalcFYI

    with CalcFYI() as api:
        data = api.list_scenarios(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No scenarios found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_calc(query: str) -> str:
    """Search calcfyi.com for calculators, formulas, and math scenarios.

    Args:
        query: Search query string.
    """
    from calcfyi.api import CalcFYI

    with CalcFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
