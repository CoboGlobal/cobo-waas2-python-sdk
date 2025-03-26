# SafeTxSubTransaction

The information about the sub-transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | Type of operation in the sub-transaction | [optional] 
**to** | **str** | Address the transaction is sent to | [optional] 
**value** | **str** | Readable transaction value (e.g., 1 ETH) | [optional] 
**wei** | **str** | Transaction amount in Wei | [optional] 
**data** | **str** | Encoded transaction data | [optional] 
**data_decoded** | [**SafeTxDecodedData**](SafeTxDecodedData.md) |  | [optional] 
**to_contract_name** | **str** | Name of the recipient contract (if available) | [optional] 

## Example

```python
from cobo_waas2.models.safe_tx_sub_transaction import SafeTxSubTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of SafeTxSubTransaction from a JSON string
safe_tx_sub_transaction_instance = SafeTxSubTransaction.from_json(json)
# print the JSON string representation of the object
print(SafeTxSubTransaction.to_json())

# convert the object into a dict
safe_tx_sub_transaction_dict = safe_tx_sub_transaction_instance.to_dict()
# create an instance of SafeTxSubTransaction from a dict
safe_tx_sub_transaction_from_dict = SafeTxSubTransaction.from_dict(safe_tx_sub_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


