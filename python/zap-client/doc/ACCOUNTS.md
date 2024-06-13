# Accounts

```python
# Get all accounts
client.get_accounts()

# Get all accounts (page 2)
client.get_accounts(page=2)

# Get an account by its ZAP id
client.get_account('6cf425b4-e200-458d-8dc2-16aba19ca7b5')

# Create an account
client.create_account({
    'name': 'account-1@domain.test',
    'aliases': [
        'alias-1@domain.test',
        'alias-2@domain.test'
    ],
    'sn': 'Account 1'
})

# Update an account
client.update_account('6cf425b4-e200-458d-8dc2-16aba19ca7b5', {
    'name': 'account-2@domain.test',
    'aliasesToAdd': [
        'alias-3@domain.test'
    ],
    'aliasesToRemove': [
        'alias-2@domain.test'
    ]
})

# Destroy an account
client.destroy_account('6cf425b4-e200-458d-8dc2-16aba19ca7b5')
```
