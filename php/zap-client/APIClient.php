<?php
//Check README.md to see usage examples.
//Check ZAP API doc for more infos.

class APIClient
{
    //your url address
    private $root;
    //your public key
    private $apiKey;
    //your private key
    private $apiSecret;

    //Automatically creates an instance of APIClient with your public and private keys and your url address.
    public function __construct($root, $apiKey, $apiSecret)
    {
        $this->root = $root;
        $this->apiKey = $apiKey;
        $this->apiSecret = $apiSecret;
    }

    //Method you can use to see all accounts, with page offset as $params.
    public function get_accounts(array $params = [])
    {
        $resource = '/api/v1/accounts';
        $method = 'GET';
        $id = '';
        $arr_body = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to see a single account picked by id.
    public function get_account($id)
    {
        $resource = '/api/v1/accounts/';
        $method = 'GET';
        $params = [];
        $arr_body = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to create an account with all attributes you want in $arr_body.
    //Check ZAP API doc to know available attributes.
    public function create_account($arr_body)
    {
        $resource = '/api/v1/accounts';
        $method = 'POST';
        $id = '';
        $params = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to update an account picked by id with all attributes you want to modify in $arr_body.
    public function update_account($id, $arr_body)
    {
        $resource = '/api/v1/accounts/';
        $method = 'PATCH';
        $params = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to delete an account picked by id.
    public function destroy_account($id)
    {
        $resource = '/api/v1/accounts/';
        $method = 'DELETE';
        $arr_body = [];
        $params = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to see all calendar resources, with page offset as $params.
    public function get_calendar_resources(array $params = [])
    {
        $resource = '/api/v1/calendar-resources';
        $method = 'GET';
        $id = '';
        $arr_body = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to see a single calendar resource picked by id.
    public function get_calendar_resource($id)
    {
        $resource = '/api/v1/calendar-resources/';
        $method = 'GET';
        $params = [];
        $arr_body = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to create a calendar_resource with all attributes you want in $arr_body.
    //Check ZAP API doc to know available attributes.
    public function create_calendar_resource($arr_body)
    {
        $resource = '/api/v1/calendar-resources';
        $method = 'POST';
        $id = '';
        $params = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to update a calendar resource picked by id with all attributes you want to modify in $arr_body.
    public function update_calendar_resource($id, $arr_body)
    {
        $resource = '/api/v1/calendar-resources/';
        $method = 'PATCH';
        $params = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to delete a calendar resource picked by id.
    public function destroy_calendar_resource($id)
    {
        $resource = '/api/v1/calendar-resources/';
        $method = 'DELETE';
        $arr_body = [];
        $params = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to see all classes of service, with page offset as $params.
    public function get_classes_of_service(array $params = [])
    {
        $resource = '/api/v1/classes-of-service';
        $method = 'GET';
        $id = '';
        $arr_body = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to see a single class of service picked by id.
    public function get_class_of_service($id)
    {
        $resource = '/api/v1/classes-of-service/';
        $method = 'GET';
        $params = [];
        $arr_body = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to see all distribution lists, with page offset as $params.
    public function get_distribution_lists(array $params = [])
    {
        $resource = '/api/v1/distribution-lists';
        $method = 'GET';
        $id = '';
        $arr_body = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to see a single distribution list picked by id.
    public function get_distribution_list($id)
    {
        $resource = '/api/v1/distribution-lists/';
        $method = 'GET';
        $params = [];
        $arr_body = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to create a distribution list with all attributes you want in $arr_body.
    //Check ZAP API doc to know available attributes.
    public function create_distribution_list($arr_body)
    {
        $resource = '/api/v1/distribution-lists';
        $method = 'POST';
        $id = '';
        $params = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to update a distribution list picked by id with all attributes you want to modify in $arr_body.
    public function update_distribution_list($id, $arr_body)
    {
        $resource = '/api/v1/distribution-lists/';
        $method = 'PATCH';
        $params = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to delete a distribution list picked by id.
    public function destroy_distribution_list($id)
    {
        $resource = '/api/v1/distribution-lists/';
        $method = 'DELETE';
        $arr_body = [];
        $params = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to see all domains, with page offset as $params.
    public function get_domains(array $params = [])
    {
        $resource = '/api/v1/domains';
        $method = 'GET';
        $id = '';
        $arr_body = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to see a single domain picked by id.
    public function get_domain($id)
    {
        $resource = '/api/v1/domains/';
        $method = 'GET';
        $params = [];
        $arr_body = [];

        return $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Calls methods which create url(1), timestamp(2), body(3), signature(4), headers(5) and make request(6).
    private function build_request(string $resource, string $method, string $id, array $params, array $arr_body)
    {
        $url = $this->make_url($resource, $id, $params);
        $timestamp = $this->make_timestamp();
        $body = $this->make_body($arr_body);
        $signature = $this->make_signature($url, $method, $body, $timestamp);
        $curleaders = $this->make_headers($timestamp, $signature);

        return $this->make_request($url, $curleaders, $method, $body);
    }

    //$resource = endpoint
    //$id = account id
    //$params = page offset
    private function make_url(string $resource, string $id = '', array $params = [])
    {
        if ($params === [])
        {
            $params = '';
        } else {
            $params = '?' . http_build_query($params);
        }

        return $this->root . $resource . $id . $params;
    }

    private function make_timestamp(): int
    {
        return round(microtime(true) * 1000);
    }

    //$arr_body = request body not 'json parsed'
    private function make_body(array $arr_body)
    {
        if ($arr_body === [])
        {
            $body = '';
        } else
        {
            $body = json_encode($arr_body);
        }

        return $body;
    }

    //$url = complete url
    //$method = http verb
    //$body = 'json parsed' body request
    //$timestamp = timestamp defines by make_timestamp()
    private function make_signature(string $url, string $method, string $body, int $timestamp)
    {
        return hash('sha256', "{$this->apiSecret}|{$timestamp}|{$method}|{$url}|{$body}");
    }

    //$timestamp = timestamp defines by make_timestamp()
    //$signature = hashed signature defined by make_signature()
    private function make_headers(int $timestamp, string $signature)
    {
        return [
            'Content-Type: application/json',
            "X-ZAP-API-Key: {$this->apiKey}",
            "X-ZAP-Signature: {$signature}",
            "X-ZAP-Timestamp: {$timestamp}",
        ];
    }

    //$url = complete url
    //$curleaders = array with Content-Type, X-ZAP-API-Key, X-ZAP-Signature and X-ZAP-Timestamp
    //$method = http verb
    //$body = 'json parsed' body request
    private function make_request(string $url, array $curleaders, string $method, string $body)
    {
        $curl = curl_init($url);

        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($curl, CURLOPT_HTTPHEADER, $curleaders);
        if ($method === 'POST')
        {
            curl_setopt($curl, CURLOPT_POST, true);
            curl_setopt($curl, CURLOPT_POSTFIELDS, $body);
        }
        if ($method === 'PATCH')
        {
            curl_setopt($curl, CURLOPT_CUSTOMREQUEST, 'PATCH');
            curl_setopt($curl, CURLOPT_POSTFIELDS, $body);
        }
        if ($method === 'DELETE')
        {
            curl_setopt($curl, CURLOPT_CUSTOMREQUEST, 'DELETE');
        }

        $response = curl_exec($curl);

        $error = curl_error($curl);
        $code = (int)curl_getinfo($curl, CURLINFO_HTTP_CODE);
        curl_close($curl);

        if($error) throw new Exception("ERROR $code: $error");
        if(!$response) return null;

        if($code < 200 || $code > 299 ) throw new Exception("ERROR $code: $response");

        return json_decode($response, true);
    }

}
