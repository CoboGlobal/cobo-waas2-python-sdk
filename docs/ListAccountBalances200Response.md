# ListAccountBalances200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BalanceAtBlock]**](BalanceAtBlock.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_account_balances200_response import ListAccountBalances200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAccountBalances200Response from a JSON string
list_account_balances200_response_instance = ListAccountBalances200Response.from_json(json)
# print the JSON string representation of the object
print(ListAccountBalances200Response.to_json())

# convert the object into a dict
list_account_balances200_response_dict = list_account_balances200_response_instance.to_dict()
# create an instance of ListAccountBalances200Response from a dict
list_account_balances200_response_from_dict = ListAccountBalances200Response.from_dict(list_account_balances200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


