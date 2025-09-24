# DispositionQueryResponse

The response for a disposition query request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The UUID of the transaction that was disposed. | 
**disposition_type** | [**DispositionType**](DispositionType.md) |  | 
**disposition_status** | [**DispositionStatus**](DispositionStatus.md) |  | 
**disposition_transaction_id** | **str** | The UUID of the generated disposition transaction (if available). | [optional] 

## Example

```python
from cobo_waas2.models.disposition_query_response import DispositionQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DispositionQueryResponse from a JSON string
disposition_query_response_instance = DispositionQueryResponse.from_json(json)
# print the JSON string representation of the object
print(DispositionQueryResponse.to_json())

# convert the object into a dict
disposition_query_response_dict = disposition_query_response_instance.to_dict()
# create an instance of DispositionQueryResponse from a dict
disposition_query_response_from_dict = DispositionQueryResponse.from_dict(disposition_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


