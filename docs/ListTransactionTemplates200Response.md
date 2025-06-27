# ListTransactionTemplates200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApprovalTemplate]**](ApprovalTemplate.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_transaction_templates200_response import ListTransactionTemplates200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionTemplates200Response from a JSON string
list_transaction_templates200_response_instance = ListTransactionTemplates200Response.from_json(json)
# print the JSON string representation of the object
print(ListTransactionTemplates200Response.to_json())

# convert the object into a dict
list_transaction_templates200_response_dict = list_transaction_templates200_response_instance.to_dict()
# create an instance of ListTransactionTemplates200Response from a dict
list_transaction_templates200_response_from_dict = ListTransactionTemplates200Response.from_dict(list_transaction_templates200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


