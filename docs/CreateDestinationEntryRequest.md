# CreateDestinationEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_id** | **str** | The destination ID. | 
**wallet_addresses** | [**List[CreateWalletAddress]**](CreateWalletAddress.md) | The wallet addresses of the destination. | [optional] 
**bank_accounts** | [**List[CreateDestinationBankAccount]**](CreateDestinationBankAccount.md) | The bank accounts of the destination. | [optional] 

## Example

```python
from cobo_waas2.models.create_destination_entry_request import CreateDestinationEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDestinationEntryRequest from a JSON string
create_destination_entry_request_instance = CreateDestinationEntryRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDestinationEntryRequest.to_json())

# convert the object into a dict
create_destination_entry_request_dict = create_destination_entry_request_instance.to_dict()
# create an instance of CreateDestinationEntryRequest from a dict
create_destination_entry_request_from_dict = CreateDestinationEntryRequest.from_dict(create_destination_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


