# TransactionFILFee

The transaction fee actually charged by the chain that uses the FIL fee model.  In the Fil fee model, the calculation method for the fee is: fee = gas_fee_cap * gas_limit, refer to [Fee models](https://www.cobo.com/developers/v2/guides/transactions/estimate-fees#fee-models).  Switch between the tabs to display the properties for different transaction fee models. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_base** | **str** | This is the minimum fee required to include a transaction in a block. It is determined by the network&#39;s congestion level, which adjusts to maintain a target block utilization rate. The base fee is burned, reducing the total supply of Filecoin over time. | [optional] 
**gas_premium** | **str** | An optional additional fee that users can include to prioritize their transactions over others. It acts like a tip to incentivize miners to select and include your transaction over transactions with only the base fee. | [optional] 
**gas_fee_cap** | **str** | The gas_fee_cap is a user-defined limit on how much they are willing to pay per unit of gas. | [optional] 
**gas_limit** | **str** | This defines the maximum amount of computational effort that a transaction is allowed to consume. It&#39;s a way to cap the resources that a transaction can use, ensuring it doesn&#39;t consume excessive network resources. | [optional] 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | [optional] 
**fee_used** | **str** | The transaction fee. | [optional] 
**estimated_fee_used** | **str** | The estimated transaction fee. | [optional] 
**gas_used** | **str** | The gas units used in the transaction. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_fil_fee import TransactionFILFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionFILFee from a JSON string
transaction_fil_fee_instance = TransactionFILFee.from_json(json)
# print the JSON string representation of the object
print(TransactionFILFee.to_json())

# convert the object into a dict
transaction_fil_fee_dict = transaction_fil_fee_instance.to_dict()
# create an instance of TransactionFILFee from a dict
transaction_fil_fee_from_dict = TransactionFILFee.from_dict(transaction_fil_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


