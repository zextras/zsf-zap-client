from zap_client import Zap

client = Zap()
client.load_config_file('config.json')

# client.load_config({
#     "APIKEY": "",
#     "APISECRET": "",
#     "URL_BASE": "",
#     "URL_PORT": ""
# })

print(client.get("/api/v1/accounts"))
# print(client.get("/api/v1/accounts", params={'page': 2}))

# print(client.get("/api/v1/accounts/42d6853a-c248-4090-b983-95362737b62c"))

