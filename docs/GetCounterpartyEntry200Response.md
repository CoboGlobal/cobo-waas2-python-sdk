# GetCounterpartyEntry200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_address** | [**WalletAddress**](WalletAddress.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.get_counterparty_entry200_response import GetCounterpartyEntry200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCounterpartyEntry200Response from a JSON string
get_counterparty_entry200_response_instance = GetCounterpartyEntry200Response.from_json(json)
# print the JSON string representation of the object
print(GetCounterpartyEntry200Response.to_json())

# convert the object into a dict
get_counterparty_entry200_response_dict = get_counterparty_entry200_response_instance.to_dict()
# create an instance of GetCounterpartyEntry200Response from a dict
get_counterparty_entry200_response_from_dict = GetCounterpartyEntry200Response.from_dict(get_counterparty_entry200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


