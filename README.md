# getBRAZA Python SDK

## Instalação

```bash
pip install -r requirements.txt
```

## Exemplo de uso
```python
from getbraza.client import GetBrazaClient

client = GetBrazaClient("app_id", "api_key", "account_number")

# Exemplo de transação PIX
response = await client.input_transaction({
    "url_callback": "https://example.com/callback",
    "amount": "100.00"
})
print(response)
```

## Testes
```bash
pytest tests/ --cov=getbraza --cov-report=html
```