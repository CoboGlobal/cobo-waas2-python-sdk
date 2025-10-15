# TransactionFILFee

The transaction fee actually charged by the chain that uses the Filecoin fee model.  For more details about the Filecoin fee model, see [Fee models](https://www.cobo.com/developers/v2/guides/transactions/estimate-fees#fee-models).  Switch between the tabs to display the properties for different transaction fee models. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_base** | **str** | The minimum fee required for a transaction to be included in a block. The base fee is dynamically adjusted based on network congestion to maintain target block utilization. It is burned rather than paid to miners, reducing the total Filecoin supply over time. | [optional] 
**gas_premium** | **str** | An optional tip you can include to prioritize your transaction. The gas premium incentivizes miners to include your transaction sooner than those offering only the base fee. | [optional] 
**gas_fee_cap** | **str** | The maximum gas price you are willing to pay per unit of gas. | [optional] 
**gas_limit** | **str** | The maximum amount of gas your transaction is allowed to consume. | [optional] 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token used to pay the transaction fee. | [optional] 
**fee_used** | **str** | The actually charged transaction fee. | [optional] 
**estimated_fee_used** | **str** | The estimated transaction fee. | [optional] 

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


