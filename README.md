# calcfyi

[![PyPI version](https://agentgif.com/badge/pypi/calcfyi/version.svg)](https://pypi.org/project/calcfyi/)
[![Python](https://img.shields.io/pypi/pyversions/calcfyi)](https://pypi.org/project/calcfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](https://pypi.org/project/calcfyi/)

Python API client for [calcfyi.com](https://calcfyi.com/) -- a collection of 200+ online calculators spanning financial, health, math, and science categories. Access calculator formulas, comparison scenarios, and computation guides through a free REST API, CLI, or MCP server for AI assistants.

[CalcFYI](https://calcfyi.com/) provides structured calculator data with underlying formulas, step-by-step explanations, and real-world scenarios -- built for developers, educators, and content creators who need computation reference data.

> **Try the calculators at [calcfyi.com](https://calcfyi.com/)** -- financial, health, math, and science calculators with formulas and explanations.

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/calcfyi/main/demo.gif" alt="calcfyi demo -- online calculator API client for Python" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You Can Do](#what-you-can-do)
  - [Financial Calculators](#financial-calculators)
  - [Health and Fitness Calculators](#health-and-fitness-calculators)
  - [Math and Science Formulas](#math-and-science-formulas)
  - [Comparison Scenarios](#comparison-scenarios)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [REST API Client](#rest-api-client)
- [API Reference](#api-reference)
- [Learn More About Calculators](#learn-more-about-calculators)
- [Guide FYI Family](#guide-fyi-family)
- [FYIPedia Developer Tools](#fyipedia-developer-tools)
- [License](#license)

## Install

```bash
pip install calcfyi              # Core (zero deps)
pip install "calcfyi[cli]"       # + Command-line interface
pip install "calcfyi[mcp]"       # + MCP server for AI assistants
pip install "calcfyi[api]"       # + HTTP client for calcfyi.com API
pip install "calcfyi[all]"       # Everything
```

## Quick Start

```python
from calcfyi.api import CalcFYI

with CalcFYI() as api:
    # List available formulas
    formulas = api.list_formulas()

    # Get a specific formula with explanation
    compound_interest = api.get_formula("compound-interest")

    # Browse comparison scenarios
    scenarios = api.list_scenarios()

    # Search across all calculator content
    results = api.search("mortgage")
```

## What You Can Do

### Financial Calculators

Financial calculators apply time-value-of-money principles to real-world decisions. Compound interest -- the concept of earning interest on interest -- is the foundation of most financial calculations. The compound interest formula A = P(1 + r/n)^(nt) computes future value given principal (P), annual rate (r), compounding frequency (n), and time (t).

| Calculator | Formula | Use Case |
|-----------|---------|----------|
| Compound Interest | A = P(1 + r/n)^(nt) | Savings growth, investment returns |
| Mortgage Payment | M = P[r(1+r)^n]/[(1+r)^n-1] | Monthly home loan payments |
| ROI | ROI = (Gain - Cost) / Cost x 100 | Investment performance |
| Break-Even | BEP = Fixed Costs / (Price - Variable Cost) | Business planning |
| Loan Amortization | Declining balance schedule | Debt repayment planning |
| Present Value | PV = FV / (1 + r)^n | Discounted cash flow analysis |

```python
from calcfyi.api import CalcFYI

# Explore financial calculator formulas and explanations
with CalcFYI() as api:
    compound = api.get_formula("compound-interest")
    print(compound["name"])    # Compound Interest formula details

    # Browse guides on financial topics
    guides = api.list_guides()
    guide = api.get_guide("compound-interest-guide")
```

Learn more: [Browse Calculators](https://calcfyi.com/) · [Glossary](https://calcfyi.com/glossary/) · [Guides](https://calcfyi.com/guides/)

### Health and Fitness Calculators

Health calculators provide evidence-based estimates for body composition, nutritional needs, and fitness metrics. BMI (Body Mass Index) -- weight in kg divided by height in meters squared -- is the most widely used screening tool, though it has known limitations for athletes and elderly populations.

| Calculator | Formula | Measures |
|-----------|---------|----------|
| BMI | weight(kg) / height(m)^2 | Body mass classification |
| BMR (Mifflin-St Jeor) | 10w + 6.25h - 5a + s | Basal metabolic rate |
| TDEE | BMR x Activity Factor | Total daily energy expenditure |
| Body Fat % | Navy method, skinfold | Body composition estimate |
| Heart Rate Zones | (HRmax - HRrest) x % + HRrest | Training intensity targets |
| Macros | TDEE split by P/C/F ratios | Daily macronutrient targets |

```python
from calcfyi.api import CalcFYI

# Explore health and fitness calculator formulas
with CalcFYI() as api:
    bmi = api.get_formula("bmi")
    bmr = api.get_formula("bmr-mifflin-st-jeor")

    # Access glossary terms for health terminology
    glossary = api.list_glossary()
    term = api.get_term("basal-metabolic-rate")
```

Learn more: [Health Calculators](https://calcfyi.com/) · [Glossary](https://calcfyi.com/glossary/) · [API Docs](https://calcfyi.com/developers/)

### Math and Science Formulas

Mathematical and scientific calculators cover geometry, trigonometry, statistics, physics, and chemistry. Each formula includes derivation context, variable definitions, and practical application examples.

| Category | Examples | Key Formulas |
|----------|----------|-------------|
| Geometry | Area, volume, surface area | Circle: A = pi*r^2, Sphere: V = 4/3*pi*r^3 |
| Statistics | Mean, std dev, z-score | z = (x - mu) / sigma |
| Physics | Force, energy, velocity | F = ma, E = mc^2, KE = 1/2*mv^2 |
| Chemistry | Molarity, dilution, pH | pH = -log[H+], M1V1 = M2V2 |
| Conversion | Temperature, units | C = (F - 32) x 5/9 |

```python
from calcfyi.api import CalcFYI

# Explore math and science formulas
with CalcFYI() as api:
    formulas = api.list_formulas()

    # Browse comparison scenarios between different approaches
    comparisons = api.list_comparisons()
    comparison = api.get_comparison("simple-vs-compound-interest")
```

Learn more: [Browse Formulas](https://calcfyi.com/) · [Comparisons](https://calcfyi.com/) · [Guides](https://calcfyi.com/guides/)

### Comparison Scenarios

Calculator comparisons show side-by-side results for different inputs or methods. For example, comparing simple interest vs compound interest over 10 years, or comparing BMI vs body fat percentage for the same individual. These scenarios help users understand when and why different formulas apply.

```python
from calcfyi.api import CalcFYI

# Explore comparison scenarios
with CalcFYI() as api:
    scenarios = api.list_scenarios()
    scenario = api.get_scenario("renting-vs-buying")

    # Browse FAQs about calculator usage
    faqs = api.list_faqs()
```

Learn more: [Scenarios](https://calcfyi.com/) · [FAQs](https://calcfyi.com/) · [Glossary](https://calcfyi.com/glossary/)

## Command-Line Interface

```bash
pip install "calcfyi[cli]"

# Search for calculators
calcfyi search "compound interest"

# Output is JSON for easy piping
calcfyi search "BMI" | jq '.results[0]'
```

## MCP Server (Claude, Cursor, Windsurf)

Add calculator data tools to any AI assistant that supports [Model Context Protocol](https://modelcontextprotocol.io/).

```bash
pip install "calcfyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "calcfyi": {
            "command": "python",
            "args": ["-m", "calcfyi.mcp_server"]
        }
    }
}
```

**Available tools**: `search_calcfyi`

## REST API Client

```python
from calcfyi.api import CalcFYI

with CalcFYI() as api:
    # List endpoints
    formulas = api.list_formulas()
    comparisons = api.list_comparisons()
    scenarios = api.list_scenarios()
    glossary = api.list_glossary()
    guides = api.list_guides()

    # Detail endpoints
    formula = api.get_formula("compound-interest")
    guide = api.get_guide("financial-formulas")

    # Search
    results = api.search("mortgage calculator")
```

## API Reference

| Method | Description |
|--------|-------------|
| `list_formulas(**params)` | List all calculator formulas |
| `get_formula(slug)` | Get formula detail |
| `list_comparisons(**params)` | List all comparisons |
| `get_comparison(slug)` | Get comparison detail |
| `list_scenarios(**params)` | List all scenarios |
| `get_scenario(slug)` | Get scenario detail |
| `list_glossary(**params)` | List glossary terms |
| `get_term(slug)` | Get glossary term detail |
| `list_guides(**params)` | List all guides |
| `get_guide(slug)` | Get guide detail |
| `list_faqs(**params)` | List all FAQs |
| `get_faq(slug)` | Get FAQ detail |
| `search(query)` | Search across all content |

Full API documentation at [calcfyi.com/developers/](https://calcfyi.com/developers/).

## Learn More About Calculators

- **Browse**: [Calculators](https://calcfyi.com/) · [Formulas](https://calcfyi.com/) · [Comparisons](https://calcfyi.com/)
- **Guides**: [Glossary](https://calcfyi.com/glossary/) · [Guides](https://calcfyi.com/guides/)
- **API**: [REST API Docs](https://calcfyi.com/developers/) · [OpenAPI Spec](https://calcfyi.com/api/openapi.json)

## Guide FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem -- life reference guides, calculators, education, and games.

| Package | PyPI | Description |
|---------|------|-------------|
| **calcfyi** | [PyPI](https://pypi.org/project/calcfyi/) | **200+ calculators, financial, health, math -- [calcfyi.com](https://calcfyi.com/)** |
| salaryfyi | [PyPI](https://pypi.org/project/salaryfyi/) | Salary comparison, tax calculators, 36 countries -- [salaryfyi.com](https://salaryfyi.com/) |
| univfyi | [PyPI](https://pypi.org/project/univfyi/) | University rankings, programs, admissions -- [univfyi.com](https://univfyi.com/) |
| boardgamefyi | [PyPI](https://pypi.org/project/boardgamefyi/) | Board games, rules, reviews, recommendations -- [boardgamefyi.com](https://boardgamefyi.com/) |

## FYIPedia Developer Tools

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| colorfyi | [PyPI](https://pypi.org/project/colorfyi/) | [npm](https://www.npmjs.com/package/@fyipedia/colorfyi) | Color conversion, WCAG contrast, harmonies -- [colorfyi.com](https://colorfyi.com/) |
| emojifyi | [PyPI](https://pypi.org/project/emojifyi/) | [npm](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata -- [emojifyi.com](https://emojifyi.com/) |
| symbolfyi | [PyPI](https://pypi.org/project/symbolfyi/) | [npm](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats -- [symbolfyi.com](https://symbolfyi.com/) |
| unicodefyi | [PyPI](https://pypi.org/project/unicodefyi/) | [npm](https://www.npmjs.com/package/unicodefyi) | Unicode lookup with 17 encodings -- [unicodefyi.com](https://unicodefyi.com/) |
| fontfyi | [PyPI](https://pypi.org/project/fontfyi/) | [npm](https://www.npmjs.com/package/fontfyi) | Google Fonts metadata & CSS -- [fontfyi.com](https://fontfyi.com/) |
| distancefyi | [PyPI](https://pypi.org/project/distancefyi/) | [npm](https://www.npmjs.com/package/distancefyi) | Haversine distance & travel times -- [distancefyi.com](https://distancefyi.com/) |
| timefyi | [PyPI](https://pypi.org/project/timefyi/) | [npm](https://www.npmjs.com/package/timefyi) | Timezone ops & business hours -- [timefyi.com](https://timefyi.com/) |
| namefyi | [PyPI](https://pypi.org/project/namefyi/) | [npm](https://www.npmjs.com/package/namefyi) | Korean romanization & Five Elements -- [namefyi.com](https://namefyi.com/) |
| unitfyi | [PyPI](https://pypi.org/project/unitfyi/) | [npm](https://www.npmjs.com/package/unitfyi) | Unit conversion, 220 units -- [unitfyi.com](https://unitfyi.com/) |
| holidayfyi | [PyPI](https://pypi.org/project/holidayfyi/) | [npm](https://www.npmjs.com/package/holidayfyi) | Holiday dates & Easter calculation -- [holidayfyi.com](https://holidayfyi.com/) |
| **calcfyi** | [PyPI](https://pypi.org/project/calcfyi/) | -- | **200+ calculators, financial, health, math -- [calcfyi.com](https://calcfyi.com/)** |
| cocktailfyi | [PyPI](https://pypi.org/project/cocktailfyi/) | -- | Cocktail ABV, calories, flavor -- [cocktailfyi.com](https://cocktailfyi.com/) |
| fyipedia | [PyPI](https://pypi.org/project/fyipedia/) | -- | Unified CLI for all FYI tools -- [fyipedia.com](https://fyipedia.com/) |

## License

MIT
