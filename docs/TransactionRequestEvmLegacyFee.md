# TransactionRequestEvmLegacyFee

The preset properties to limit transaction fee.  In the legacy fee model, the transaction fee is calculated by multiplying the gas price by the gas units used by the transaction. This can be expressed as: Transaction fee =  (gas price * gas units used).   You can specify the gas limit to limit the gas units used in the transaction.  Switch between the tabs to display the properties for different transaction fee models. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_price** | **str** | The gas price, in wei. The gas price represents the amount of ETH that must be paid to validators for processing transactions per gas unit used. | 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | 
**gas_limit** | **str** | The gas limit. It represents the maximum number of gas units that you are willing to pay for the execution of a transaction or Ethereum Virtual Machine (EVM) operation. The gas unit cost of each operation varies. | [optional] [default to '21000']

## Example

```python
from cobo_waas2.models.transaction_request_evm_legacy_fee import TransactionRequestEvmLegacyFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestEvmLegacyFee from a JSON string
transaction_request_evm_legacy_fee_instance = TransactionRequestEvmLegacyFee.from_json(json)
# print the JSON string representation of the object
print(TransactionRequestEvmLegacyFee.to_json())

# convert the object into a dict
transaction_request_evm_legacy_fee_dict = transaction_request_evm_legacy_fee_instance.to_dict()
# create an instance of TransactionRequestEvmLegacyFee from a dict
transaction_request_evm_legacy_fee_from_dict = TransactionRequestEvmLegacyFee.from_dict(transaction_request_evm_legacy_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


