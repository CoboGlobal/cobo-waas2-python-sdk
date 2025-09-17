# DispositionResponse

The response for a disposition request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The UUID of the transaction being processed for disposition. | 
**status** | [**DispositionStatus**](DispositionStatus.md) |  | 

## Example

```python
from cobo_waas2.models.disposition_response import DispositionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DispositionResponse from a JSON string
disposition_response_instance = DispositionResponse.from_json(json)
# print the JSON string representation of the object
print(DispositionResponse.to_json())

# convert the object into a dict
disposition_response_dict = disposition_response_instance.to_dict()
# create an instance of DispositionResponse from a dict
disposition_response_from_dict = DispositionResponse.from_dict(disposition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


