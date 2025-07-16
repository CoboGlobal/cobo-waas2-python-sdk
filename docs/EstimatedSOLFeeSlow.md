# EstimatedSOLFeeSlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_unit_price** | **str** | The price paid per compute unit. This value determines the priority fee for the transaction, allowing you to increase inclusion probability in congested conditions. | 
**compute_unit_limit** | **str** | The maximum number of compute units your transaction is allowed to consume. It sets an upper bound on computational resource usage to prevent overload. | 
**base_fee** | **str** | A fixed fee charged per signature. The default is 5,000 lamports per signature. | 
**rent_amount** | **str** | The rent fee charged by the network to store non–rent-exempt accounts on-chain. It is deducted periodically until the account maintains the minimum balance required for rent exemption. | [optional] 

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


