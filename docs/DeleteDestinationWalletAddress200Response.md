# DeleteDestinationWalletAddress200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_address_id** | **str** | The wallet address ID under the destination. | 

## Example

```python
from cobo_waas2.models.delete_destination_wallet_address200_response import DeleteDestinationWalletAddress200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDestinationWalletAddress200Response from a JSON string
delete_destination_wallet_address200_response_instance = DeleteDestinationWalletAddress200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteDestinationWalletAddress200Response.to_json())

# convert the object into a dict
delete_destination_wallet_address200_response_dict = delete_destination_wallet_address200_response_instance.to_dict()
# create an instance of DeleteDestinationWalletAddress200Response from a dict
delete_destination_wallet_address200_response_from_dict = DeleteDestinationWalletAddress200Response.from_dict(delete_destination_wallet_address200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


