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

    //Calls methods which create url(1), timestamp(2), body(3), signature(4), headers(5) and make request(6).
    private function build_request(string $resource, string $method, string $id, array $params, array $arr_body)
    {
        $url = $this->make_url($resource, $id, $params);
        $timestamp = $this->make_timestamp();
        $body = $this->make_body($arr_body);
        $signature = $this->make_signature($url, $method, $body, $timestamp);
        $headers = $this->make_headers($timestamp, $signature);
        $this->make_request($url, $headers, $method, $body);
    }

    //1. Creates url.
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

    //2. Defines timestamp.
    private function make_timestamp(): int
    {
        return round(microtime(true) * 1000);
    }

    //3. Defines body.
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

    //4. Constructs signature.
    //$url = complete url
    //$method = http verb
    //$body = 'json parsed' body request
    //$timestamp = timestamp defines by make_timestamp()
    private function make_signature(string $url, string $method, string $body, int $timestamp)
    {
        return hash('sha256', "{$this->apiSecret}|{$timestamp}|{$method}|{$url}|{$body}");
    }

    //5. Constructs headers.
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

    //6. Makes request with elements defined in previous methods.
    //$url = complete url
    //$headers = array with Content-Type, X-ZAP-API-Key, X-ZAP-Signature and X-ZAP-Timestamp
    //$method = http verb
    //$body = 'json parsed' body request
    private function make_request(string $url, array $headers, string $method, string $body)
    {
        $curl = curl_init($url);

        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
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
        curl_close($curl);

        if ($response === false) {
            die('Error: "' . curl_error($curl) . '" - Code: ' . curl_errno($curl));
        }

        var_dump($response);
    }


    //Method you can use to see all accounts, with page offset as $params.
    public function get_accounts(array $params = [])
    {
        $resource = '/api/v1/accounts';
        $method = 'GET';
        $id = '';
        $arr_body = [];

        $result = $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to see a single account picked by id.
    public function get_account($id)
    {
        $resource = '/api/v1/accounts/';
        $method = 'GET';
        $params = [];
        $arr_body = [];

        $result = $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to create an account with all attributes you want in $arr_body.
    //Check ZAP API doc to know available attributes.
    public function create_account($arr_body)
    {
        $resource = '/api/v1/accounts';
        $method = 'POST';
        $id = '';
        $params = [];

        $result = $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to update an account picked by id with all attributes you want to modify in $arr_body.
    public function update_account($id, $arr_body)
    {
        $resource = '/api/v1/accounts/';
        $method = 'PATCH';
        $params = [];

        $result = $this->build_request($resource, $method, $id, $params, $arr_body);
    }

    //Method you can use to delete an account picked by id.
    public function destroy_account($id)
    {
        $resource = '/api/v1/accounts/';
        $method = 'DELETE';
        $arr_body = [];
        $params = [];

        $result = $this->build_request($resource, $method, $id, $params, $arr_body);
    }
}
