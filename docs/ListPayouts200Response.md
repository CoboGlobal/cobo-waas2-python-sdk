# ListPayouts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PaymentPayout]**](PaymentPayout.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_payouts200_response import ListPayouts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPayouts200Response from a JSON string
list_payouts200_response_instance = ListPayouts200Response.from_json(json)
# print the JSON string representation of the object
print(ListPayouts200Response.to_json())

# convert the object into a dict
list_payouts200_response_dict = list_payouts200_response_instance.to_dict()
# create an instance of ListPayouts200Response from a dict
list_payouts200_response_from_dict = ListPayouts200Response.from_dict(list_payouts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


