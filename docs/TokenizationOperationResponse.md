# TokenizationOperationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | The ID of the activity related to the tokenization operation. | 

## Example

```python
from cobo_waas2.models.tokenization_operation_response import TokenizationOperationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationOperationResponse from a JSON string
tokenization_operation_response_instance = TokenizationOperationResponse.from_json(json)
# print the JSON string representation of the object
print(TokenizationOperationResponse.to_json())

# convert the object into a dict
tokenization_operation_response_dict = tokenization_operation_response_instance.to_dict()
# create an instance of TokenizationOperationResponse from a dict
tokenization_operation_response_from_dict = TokenizationOperationResponse.from_dict(tokenization_operation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


