# DestinationDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_id** | **str** | The destination ID. | 
**destination_type** | [**DestinationType**](DestinationType.md) |  | 
**destination_name** | **str** | The destination name. | 
**country** | **str** | The country of the destination, in ISO 3166-1 alpha-3 format. | [optional] 
**email** | **str** | The email of the destination. | [optional] 
**contact_address** | **str** | The contact address of the destination. | [optional] 
**wallet_addresses** | [**List[WalletAddress]**](WalletAddress.md) | The wallet addresses of the destination. | [optional] 
**bank_accounts** | [**List[DestinationBankAccount]**](DestinationBankAccount.md) | The bank accounts of the destination. | [optional] 
**merchant_id** | **str** | The ID of the merchant linked to the destination. | [optional] 
**created_timestamp** | **int** | The created time of the destination, represented as a UNIX timestamp in seconds. | 
**updated_timestamp** | **int** | The updated time of the destination, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.destination_detail import DestinationDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationDetail from a JSON string
destination_detail_instance = DestinationDetail.from_json(json)
# print the JSON string representation of the object
print(DestinationDetail.to_json())

# convert the object into a dict
destination_detail_dict = destination_detail_instance.to_dict()
# create an instance of DestinationDetail from a dict
destination_detail_from_dict = DestinationDetail.from_dict(destination_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


