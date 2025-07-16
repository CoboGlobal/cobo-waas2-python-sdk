# TransactionRequestFILFee

The preset properties to limit transaction fee.  In the Filecoin fee model, the transaction fee is calculated using the minimum of your specified gas fee cap and the sum of the base fee and gas premium, then multiplied by the gas limit. This can be expressed as: Transaction fee = min(gas fee cap, base fee + gas premium) * gas limit. For more information about the Filecoin fee model, refer to [Fee models](https://www.cobo.com/developers/v2/guides/transactions/estimate-fees#fee-models).  You can specify the gas fee cap, gas premium, and gas limit to control fee behavior and prioritization.  Switch between the tabs to display the properties for different transaction fee models. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_premium** | **str** | An optional tip you can include to prioritize your transaction. The gas premium incentivizes miners to include your transaction sooner than those offering only the base fee. | 
**gas_fee_cap** | **str** | The maximum gas price you are willing to pay per unit of gas. | 
**gas_limit** | **str** | The maximum amount of gas your transaction is allowed to consume. | [optional] 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token used to pay the transaction fee. | 

## Example

```python
from cobo_waas2.models.transaction_request_fil_fee import TransactionRequestFILFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestFILFee from a JSON string
transaction_request_fil_fee_instance = TransactionRequestFILFee.from_json(json)
# print the JSON string representation of the object
print(TransactionRequestFILFee.to_json())

# convert the object into a dict
transaction_request_fil_fee_dict = transaction_request_fil_fee_instance.to_dict()
# create an instance of TransactionRequestFILFee from a dict
transaction_request_fil_fee_from_dict = TransactionRequestFILFee.from_dict(transaction_request_fil_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


