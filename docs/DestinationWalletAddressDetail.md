# DestinationWalletAddressDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_id** | **str** | The destination ID. | 
**destination_name** | **str** | The name of the destination. | 
**destination_type** | [**DestinationType**](DestinationType.md) |  | 
**merchant_id** | **str** | The ID of the merchant linked to the destination. | [optional] 
**wallet_address_id** | **str** | The wallet address ID. | 
**address** | **str** | The wallet address. | 
**chain_id** | **str** | The chain ID of the cryptocurrency. | 
**updated_timestamp** | **int** | The updated time of the wallet address, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.destination_wallet_address_detail import DestinationWalletAddressDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationWalletAddressDetail from a JSON string
destination_wallet_address_detail_instance = DestinationWalletAddressDetail.from_json(json)
# print the JSON string representation of the object
print(DestinationWalletAddressDetail.to_json())

# convert the object into a dict
destination_wallet_address_detail_dict = destination_wallet_address_detail_instance.to_dict()
# create an instance of DestinationWalletAddressDetail from a dict
destination_wallet_address_detail_from_dict = DestinationWalletAddressDetail.from_dict(destination_wallet_address_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


