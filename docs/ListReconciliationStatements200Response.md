# ListReconciliationStatements200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReconDailyStatement]**](ReconDailyStatement.md) | The list of daily reconciliation statements. | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from cobo_waas2.models.list_reconciliation_statements200_response import ListReconciliationStatements200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListReconciliationStatements200Response from a JSON string
list_reconciliation_statements200_response_instance = ListReconciliationStatements200Response.from_json(json)
# print the JSON string representation of the object
print(ListReconciliationStatements200Response.to_json())

# convert the object into a dict
list_reconciliation_statements200_response_dict = list_reconciliation_statements200_response_instance.to_dict()
# create an instance of ListReconciliationStatements200Response from a dict
list_reconciliation_statements200_response_from_dict = ListReconciliationStatements200Response.from_dict(list_reconciliation_statements200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


