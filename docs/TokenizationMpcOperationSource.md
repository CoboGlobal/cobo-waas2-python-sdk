# TokenizationMpcOperationSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**TokenizationOperationSourceType**](TokenizationOperationSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address used to interact with the token contract. | 

## Example

```python
from cobo_waas2.models.tokenization_mpc_operation_source import TokenizationMpcOperationSource

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationMpcOperationSource from a JSON string
tokenization_mpc_operation_source_instance = TokenizationMpcOperationSource.from_json(json)
# print the JSON string representation of the object
print(TokenizationMpcOperationSource.to_json())

# convert the object into a dict
tokenization_mpc_operation_source_dict = tokenization_mpc_operation_source_instance.to_dict()
# create an instance of TokenizationMpcOperationSource from a dict
tokenization_mpc_operation_source_from_dict = TokenizationMpcOperationSource.from_dict(tokenization_mpc_operation_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


