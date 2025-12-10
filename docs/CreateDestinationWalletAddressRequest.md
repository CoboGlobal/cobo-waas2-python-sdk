# CreateDestinationWalletAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_id** | **str** | The destination ID. | 
**address** | **str** | The wallet address. | 
**chain_id** | **str** | The chain ID of the cryptocurrency. | 

## Example

```python
from cobo_waas2.models.create_destination_wallet_address_request import CreateDestinationWalletAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDestinationWalletAddressRequest from a JSON string
create_destination_wallet_address_request_instance = CreateDestinationWalletAddressRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDestinationWalletAddressRequest.to_json())

# convert the object into a dict
create_destination_wallet_address_request_dict = create_destination_wallet_address_request_instance.to_dict()
# create an instance of CreateDestinationWalletAddressRequest from a dict
create_destination_wallet_address_request_from_dict = CreateDestinationWalletAddressRequest.from_dict(create_destination_wallet_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


