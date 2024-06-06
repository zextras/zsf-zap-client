# ZAP CLient API - Python

## Requirements
```txt
Python : 3.10+
```

## Usage
Config File
```json
{
  "APIKEY": "",
  "APISECRET": "",
  "URL_BASE": "",
  "URL_PORT": ""
}
```

Script
```py
from zap_client import Zap

client = Zap()
client.load_config('config.json')

# list all accounts
accounts = client.get("/api/v1/accounts")

# list all accounts, page 2
accounts_page2 = client.get("/api/v1/accounts", params={'page': 2})

# list one account
account = client.get("/api/v1/accounts/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
```

