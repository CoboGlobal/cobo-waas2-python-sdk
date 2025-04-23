# ListTokenBalancesForFeeStation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ListTokenBalancesForFeeStation200ResponseDataInner]**](ListTokenBalancesForFeeStation200ResponseDataInner.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_token_balances_for_fee_station200_response import ListTokenBalancesForFeeStation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListTokenBalancesForFeeStation200Response from a JSON string
list_token_balances_for_fee_station200_response_instance = ListTokenBalancesForFeeStation200Response.from_json(json)
# print the JSON string representation of the object
print(ListTokenBalancesForFeeStation200Response.to_json())

# convert the object into a dict
list_token_balances_for_fee_station200_response_dict = list_token_balances_for_fee_station200_response_instance.to_dict()
# create an instance of ListTokenBalancesForFeeStation200Response from a dict
list_token_balances_for_fee_station200_response_from_dict = ListTokenBalancesForFeeStation200Response.from_dict(list_token_balances_for_fee_station200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


