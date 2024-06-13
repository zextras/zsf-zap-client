# Documentation
## Usage
### Creating an API client

```python
import zap_client

client = zap_client.Client(
    api_key=zap_client.ApiKey(
        'API key id here',
        'API key secret here',
    ),
    host='zap.carboniocloud.fr',
)
```

### Using the API client

- [create, read, update and delete accounts](ACCOUNTS.md)
- [create, read, update and delete calendar resources](CALENDAR_RESOURCES.md)
- [create, read, update and delete distribution lists](DISTRIBUTION_LISTS.md)
- [read classes of service](CLASSES_OF_SERVICE.md)
- [read domains](DOMAINS.md)
