# Distribution lists

```python
# Get all distribution lists
client.get_distribution_lists()

# Get all distribution lists (page 2)
client.get_distribution_lists(page=2)

# Get a distribution list by its ZAP id
client.get_distribution_list('0d1248ad-5be1-48fb-a937-76aa4495dde2')

# Create a distribution list
client.create_distribution_list({
    'name': 'distribution-list-1@domain.test',
    'aliases': [
        'alias-4@domain.test',
        'alias-5@domain.test'
    ],
    'members': [
        'account-1@domain.test',
        'external-address@example.com'
    ],
    'senders': [
        {
            'type': 'pub'
        }
    ]
})

# Update a distribution list
client.update_distribution_list('0d1248ad-5be1-48fb-a937-76aa4495dde2', {
    'name': 'distribution-list-2@domain.test',
    'aliasesToAdd': [
        'alias-6@domain.test'
    ],
    'aliasesToRemove': [
        'alias-5@domain.test'
    ],
    'membersToAdd': [
        'account-2@domain.test',
    ],
    'membersToRemove': [
        'external-address@example.com'
    ],
    'sendersToAdd': [
        {
            'name': 'domain.test',
            'type': 'dom'
        },
        {
            'name': 'account-1@domain.test',
            'type': 'usr'
        }
    ],
    'sendersToRemove': [
        {
            'type': 'pub'
        }
    ]
})

# Destroy a distribution list
client.destroy_distribution_list('0d1248ad-5be1-48fb-a937-76aa4495dde2')
```
