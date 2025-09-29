# TransactionEvmLegacyFee

The transaction fee actually charged by the chain that uses the legacy fee model.   The transaction fee is calculated by multiplying the gas price by the used gas. This can be expressed as: Transaction fee = gas price * used gas units.  Switch between the tabs to display the properties for different transaction fee models. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_price** | **str** | The gas price, in wei. The gas price represents the amount of ETH that must be paid to validators for processing transactions per gas unit used. | [optional] 
**gas_limit** | **str** | The gas limit. It represents the maximum number of gas units that you are willing to pay for the execution of a transaction or Ethereum Virtual Machine (EVM) operation. The gas unit cost of each operation varies. | [optional] 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | [optional] 
**fee_used** | **str** | The transaction fee. | [optional] 
**estimated_fee_used** | **str** | The estimated transaction fee. | [optional] 
**gas_used** | **str** | The gas units used in the transaction. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_evm_legacy_fee import TransactionEvmLegacyFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionEvmLegacyFee from a JSON string
transaction_evm_legacy_fee_instance = TransactionEvmLegacyFee.from_json(json)
# print the JSON string representation of the object
print(TransactionEvmLegacyFee.to_json())

# convert the object into a dict
transaction_evm_legacy_fee_dict = transaction_evm_legacy_fee_instance.to_dict()
# create an instance of TransactionEvmLegacyFee from a dict
transaction_evm_legacy_fee_from_dict = TransactionEvmLegacyFee.from_dict(transaction_evm_legacy_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


