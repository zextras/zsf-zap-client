```php
//Creates an APIClient instance.
//Fill with your url address, your public key and your private key.
$client = new APIClient('http://domain:port', 'xxxxxxxx...', 'xxxxxxxx...');

//Lists all accounts.
$client->get_accounts();

//Lists all accounts in page 2.
$client->get_accounts([
    'page' => 2
]);

//Lists a single account picked by UUID id.
$client->get_account('xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx');

//Creates an account with attributes you want.
//In this example we only set name, displayName and zimbra PasswordMustChange
//classOfServicesId is required 
//Check API doc to see all the available ones.
$client->create_account([
    'name' => 'fill here with email address',
    'classOfServideId' => 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
    'displayName' => 'fill here with name to display',
    'zimbraPasswordMustChange' => true,
]);

//Updates an account picked by UUID id.
//In this example we only update zimbraAccountStatus.
//Check API doc to see all the available ones.
$client->update_account('xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
    ['zimbraAccountStatus' => 'active']);

//Deletes an account picked by UUID id.
$client->destroy_account('xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx');