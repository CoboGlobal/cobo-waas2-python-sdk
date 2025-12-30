# CreateDestinationEntry201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_id** | **str** | The destination ID. | 
**wallet_addresses** | [**List[WalletAddress]**](WalletAddress.md) | The wallet addresses of the destination. | [optional] 
**bank_accounts** | [**List[DestinationBankAccount]**](DestinationBankAccount.md) | The bank accounts of the destination. | [optional] 

## Example

```python
from cobo_waas2.models.create_destination_entry201_response import CreateDestinationEntry201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDestinationEntry201Response from a JSON string
create_destination_entry201_response_instance = CreateDestinationEntry201Response.from_json(json)
# print the JSON string representation of the object
print(CreateDestinationEntry201Response.to_json())

# convert the object into a dict
create_destination_entry201_response_dict = create_destination_entry201_response_instance.to_dict()
# create an instance of CreateDestinationEntry201Response from a dict
create_destination_entry201_response_from_dict = CreateDestinationEntry201Response.from_dict(create_destination_entry201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


