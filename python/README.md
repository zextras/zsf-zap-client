# ZAP Client API - Python

## Requirements
```txt
Python : 3.10+
```

## Usage
### Usage without config file
Script
```py
from zap_client import Zap

zap = Zap()
zap.load_config({
    "APIKEY": "",
    "APISECRET": "",
    "URL_BASE": "",
    "URL_PORT": ""
})

# list all accounts
accounts = zap.get("/api/v1/accounts")

# list all accounts, page 2
accounts_page2 = zap.get("/api/v1/accounts", params={'page': 2})

# list one account
account = zap.get("/api/v1/accounts/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
```

### Usage with config file
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

zap = Zap()
zap.load_config_file('config.json')

# list all accounts
accounts = zap.get("/api/v1/accounts")

# list all accounts, page 2
accounts_page2 = zap.get("/api/v1/accounts", params={'page': 2})

# list one account
account = zap.get("/api/v1/accounts/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
```

