# calcfyi

Online calculators — financial, health and math API client — [calcfyi.com](https://calcfyi.com)

## Install

```bash
pip install calcfyi
```

## Quick Start

```python
from calcfyi.api import CalcFYI

with CalcFYI() as api:
    results = api.search("bmi")
    print(results)
```

## License

MIT
