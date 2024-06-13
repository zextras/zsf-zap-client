# Calendar resources

```python
# Get all calendar resources
client.get_calendar_resources()

# Get all calendar resources (page 2)
client.get_calendar_resources(page=2)

# Get a calendar resource by its ZAP id
client.get_calendar_resource('b4ca1345-9509-4e51-9fb3-fe794549bc70')

# Create a calendar resource
client.create_calendar_resource({
    'name': 'calendar-resource-1@domain.test',
    'zimbraCalResType': 'Location',
    'zimbraPrefCalendarForwardInvitesTo': [
        'account-1@domain.test'
    ]
})

# Update a calendar resource
client.update_calendar_resource('b4ca1345-9509-4e51-9fb3-fe794549bc70', {
    'name': 'calendar-resource-2@domain.test',
    'zimbraCalResType': 'Equipment',
    'zimbraPrefCalendarForwardInvitesTo': [
        'account-1@domain.test',
        'account-2@domain.test'
    ]
})

# Destroy a calendar resource
client.destroy_calendar_resource('b4ca1345-9509-4e51-9fb3-fe794549bc70')
```
