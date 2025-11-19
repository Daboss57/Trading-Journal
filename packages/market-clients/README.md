# market-clients

Python helper package for calling third-party market data APIs.

## Example

```python
from market_clients import FinnhubClient

client = FinnhubClient(api_key="demo")
print(client.quote("TSLA"))
```

## TODO
- Add async variants using `httpx`.
- Cache responses in Redis when running inside the ingestion service.
- Extend coverage to CoinGecko + Yahoo Finance snapshot helpers.
