# ListTopUpPayerAccounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PayerAccount]**](PayerAccount.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_top_up_payer_accounts200_response import ListTopUpPayerAccounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListTopUpPayerAccounts200Response from a JSON string
list_top_up_payer_accounts200_response_instance = ListTopUpPayerAccounts200Response.from_json(json)
# print the JSON string representation of the object
print(ListTopUpPayerAccounts200Response.to_json())

# convert the object into a dict
list_top_up_payer_accounts200_response_dict = list_top_up_payer_accounts200_response_instance.to_dict()
# create an instance of ListTopUpPayerAccounts200Response from a dict
list_top_up_payer_accounts200_response_from_dict = ListTopUpPayerAccounts200Response.from_dict(list_top_up_payer_accounts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


