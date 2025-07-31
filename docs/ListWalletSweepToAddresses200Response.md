# ListWalletSweepToAddresses200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SweepToAddress]**](SweepToAddress.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_wallet_sweep_to_addresses200_response import ListWalletSweepToAddresses200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListWalletSweepToAddresses200Response from a JSON string
list_wallet_sweep_to_addresses200_response_instance = ListWalletSweepToAddresses200Response.from_json(json)
# print the JSON string representation of the object
print(ListWalletSweepToAddresses200Response.to_json())

# convert the object into a dict
list_wallet_sweep_to_addresses200_response_dict = list_wallet_sweep_to_addresses200_response_instance.to_dict()
# create an instance of ListWalletSweepToAddresses200Response from a dict
list_wallet_sweep_to_addresses200_response_from_dict = ListWalletSweepToAddresses200Response.from_dict(list_wallet_sweep_to_addresses200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


