# EstimatedSOLFeeSlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_unit_price** | **str** | The cost per compute unit. Transactions consume computational resources measured in compute units, and this price helps determine the cost of executing transactions, especially complex ones involving smart contracts. | 
**compute_unit_limit** | **str** | The maximum number of compute units allowed for a transaction. This limits the resources any single transaction can consume, preventing excessive resource usage that could impact network performance negatively. | 
**base_fee** | **str** | The fundamental fee required for each transaction. It is charged to prevent spam transactions and network congestion, ensuring that only meaningful transactions consume network resources. | 
**rent_amount** | **str** | The fee charged as rent for maintaining the state of accounts on the blockchain. This rent ensures accounts are stored on-chain over the long term and that there&#39;s sufficient balance to sustain the account state. | [optional] 

## Example

```python
from cobo_waas2.models.estimated_sol_fee_slow import EstimatedSOLFeeSlow

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedSOLFeeSlow from a JSON string
estimated_sol_fee_slow_instance = EstimatedSOLFeeSlow.from_json(json)
# print the JSON string representation of the object
print(EstimatedSOLFeeSlow.to_json())

# convert the object into a dict
estimated_sol_fee_slow_dict = estimated_sol_fee_slow_instance.to_dict()
# create an instance of EstimatedSOLFeeSlow from a dict
estimated_sol_fee_slow_from_dict = EstimatedSOLFeeSlow.from_dict(estimated_sol_fee_slow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


