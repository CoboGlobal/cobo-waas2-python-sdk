# ListMerchantBalances200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MerchantBalance]**](MerchantBalance.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_merchant_balances200_response import ListMerchantBalances200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMerchantBalances200Response from a JSON string
list_merchant_balances200_response_instance = ListMerchantBalances200Response.from_json(json)
# print the JSON string representation of the object
print(ListMerchantBalances200Response.to_json())

# convert the object into a dict
list_merchant_balances200_response_dict = list_merchant_balances200_response_instance.to_dict()
# create an instance of ListMerchantBalances200Response from a dict
list_merchant_balances200_response_from_dict = ListMerchantBalances200Response.from_dict(list_merchant_balances200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


