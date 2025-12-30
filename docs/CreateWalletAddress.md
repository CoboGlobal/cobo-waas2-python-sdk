# CreateWalletAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The wallet address. | 
**chain_id** | **str** | The chain ID of the address. | 

## Example

```python
from cobo_waas2.models.create_wallet_address import CreateWalletAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWalletAddress from a JSON string
create_wallet_address_instance = CreateWalletAddress.from_json(json)
# print the JSON string representation of the object
print(CreateWalletAddress.to_json())

# convert the object into a dict
create_wallet_address_dict = create_wallet_address_instance.to_dict()
# create an instance of CreateWalletAddress from a dict
create_wallet_address_from_dict = CreateWalletAddress.from_dict(create_wallet_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


