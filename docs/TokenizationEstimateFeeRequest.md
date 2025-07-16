# TokenizationEstimateFeeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_params** | [**TokenizationEstimateFeeRequestOperationParams**](TokenizationEstimateFeeRequestOperationParams.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_estimate_fee_request import TokenizationEstimateFeeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationEstimateFeeRequest from a JSON string
tokenization_estimate_fee_request_instance = TokenizationEstimateFeeRequest.from_json(json)
# print the JSON string representation of the object
print(TokenizationEstimateFeeRequest.to_json())

# convert the object into a dict
tokenization_estimate_fee_request_dict = tokenization_estimate_fee_request_instance.to_dict()
# create an instance of TokenizationEstimateFeeRequest from a dict
tokenization_estimate_fee_request_from_dict = TokenizationEstimateFeeRequest.from_dict(tokenization_estimate_fee_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


