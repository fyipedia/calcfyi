"""HTTP API client for calcfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install calcfyi[api]``

Usage::

    from calcfyi.api import CalcFYI

    with CalcFYI() as api:
        items = api.list_formulas()
        detail = api.get_formula("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class CalcFYI:
    """API client for the calcfyi.com REST API.

    Provides typed access to all calcfyi.com endpoints including
    list, detail, and search operations.

    Args:
        base_url: API base URL. Defaults to ``https://calcfyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://calcfyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_comparisons(self, **params: Any) -> dict[str, Any]:
        """List all comparisons."""
        return self._get("/api/v1/comparisons/", **params)

    def get_comparison(self, slug: str) -> dict[str, Any]:
        """Get comparison by slug."""
        return self._get(f"/api/v1/comparisons/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_formulas(self, **params: Any) -> dict[str, Any]:
        """List all formulas."""
        return self._get("/api/v1/formulas/", **params)

    def get_formula(self, slug: str) -> dict[str, Any]:
        """Get formula by slug."""
        return self._get(f"/api/v1/formulas/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_scenarios(self, **params: Any) -> dict[str, Any]:
        """List all scenarios."""
        return self._get("/api/v1/scenarios/", **params)

    def get_scenario(self, slug: str) -> dict[str, Any]:
        """Get scenario by slug."""
        return self._get(f"/api/v1/scenarios/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> CalcFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
