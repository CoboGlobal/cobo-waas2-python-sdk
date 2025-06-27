# TransactionEvmCalldataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** | The ID of the chain on which the smart contract is issued. | [optional] 
**address** | **str** | The address of the smart contract. | [optional] 
**name** | **str** | The name of the smart contract. | [optional] 
**impl_address** | **str** | The address of the implementation smart contract. This property is applicable only when the specified smart contract is a proxy contract. | [optional] 
**impl_name** | **str** | The name of the implementation smart contract. This property is applicable only when the specified smart contract is a proxy contract. | [optional] 
**proxy** | **bool** | Whether the specified smart contract address is a proxy contract. - &#x60;true&#x60;: The specified smart contract address is a proxy contract. - &#x60;false&#x60;: The specified smart contract address is not a proxy contract.  | [optional] 
**method** | [**TransactionEvmContractMethod**](TransactionEvmContractMethod.md) |  | [optional] 
**params** | **str** | The parameters of the contract method are represented as a JSON array of arrays. Each element in the outer array is itself an array containing three elements that provide detailed information about a specific parameter: - Parameter name: The unique identifier of the parameter, such as &#x60;kind&#x60;, &#x60;swaps&#x60;, and &#x60;to&#x60;. - Parameter type: The Solidity data type of the parameter, such as &#x60;uint8&#x60;, &#x60;tuple[]&#x60;, &#x60;address[]&#x60;, and &#x60;int256[]&#x60;. - Parameter value: The actual value of the parameter. If the parameter type is a basic type such as &#x60;uint256&#x60; or &#x60;address&#x60;, this value is a single element. If the parameter type is a complex type such as &#x60;tuple[]&#x60; or &#x60;address[]&#x60;, the value is a nested array, with each inner array containing parameter names, types, and values.  | [optional] 

## Example

```python
from cobo_waas2.models.transaction_evm_calldata_info import TransactionEvmCalldataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionEvmCalldataInfo from a JSON string
transaction_evm_calldata_info_instance = TransactionEvmCalldataInfo.from_json(json)
# print the JSON string representation of the object
print(TransactionEvmCalldataInfo.to_json())

# convert the object into a dict
transaction_evm_calldata_info_dict = transaction_evm_calldata_info_instance.to_dict()
# create an instance of TransactionEvmCalldataInfo from a dict
transaction_evm_calldata_info_from_dict = TransactionEvmCalldataInfo.from_dict(transaction_evm_calldata_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


