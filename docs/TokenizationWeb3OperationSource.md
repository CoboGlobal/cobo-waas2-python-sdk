# TokenizationWeb3OperationSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**TokenizationOperationSourceType**](TokenizationOperationSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address to interact with the token contract from. | 

## Example

```python
from cobo_waas2.models.tokenization_web3_operation_source import TokenizationWeb3OperationSource

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationWeb3OperationSource from a JSON string
tokenization_web3_operation_source_instance = TokenizationWeb3OperationSource.from_json(json)
# print the JSON string representation of the object
print(TokenizationWeb3OperationSource.to_json())

# convert the object into a dict
tokenization_web3_operation_source_dict = tokenization_web3_operation_source_instance.to_dict()
# create an instance of TokenizationWeb3OperationSource from a dict
tokenization_web3_operation_source_from_dict = TokenizationWeb3OperationSource.from_dict(tokenization_web3_operation_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


