# CreateDestinationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_name** | **str** | The destination name. | 
**destination_type** | [**DestinationType**](DestinationType.md) |  | 
**wallet_addresses** | [**List[CreateWalletAddress]**](CreateWalletAddress.md) | The wallet addresses of the destination. | [optional] 
**bank_accounts** | [**List[CreateDestinationBankAccount]**](CreateDestinationBankAccount.md) | The bank accounts of the destination. | [optional] 
**merchant_id** | **str** | The ID of the merchant linked to the destination. | [optional] 
**country** | **str** | The country of the destination, in ISO 3166-1 alpha-3 format. | [optional] 
**email** | **str** | The email of the destination. | [optional] 
**contact_address** | **str** | The contact address of the destination. | [optional] 

## Example

```python
from cobo_waas2.models.create_destination_request import CreateDestinationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDestinationRequest from a JSON string
create_destination_request_instance = CreateDestinationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDestinationRequest.to_json())

# convert the object into a dict
create_destination_request_dict = create_destination_request_instance.to_dict()
# create an instance of CreateDestinationRequest from a dict
create_destination_request_from_dict = CreateDestinationRequest.from_dict(create_destination_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


