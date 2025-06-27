# EstimatedFILFeeSlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_premium** | **str** | An optional additional fee that users can include to prioritize their transactions over others. It acts like a tip to incentivize miners to select and include your transaction over transactions with only the base fee. | 
**gas_fee_cap** | **str** | The gas_fee_cap is a user-defined limit on how much they are willing to pay per unit of gas. | 
**gas_limit** | **str** | This defines the maximum amount of computational effort that a transaction is allowed to consume. It&#39;s a way to cap the resources that a transaction can use, ensuring it doesn&#39;t consume excessive network resources. | 
**gas_base** | **str** | This is the minimum fee required to include a transaction in a block. It is determined by the network&#39;s congestion level, which adjusts to maintain a target block utilization rate. The base fee is burned, reducing the total supply of Filecoin over time. | 

## Example

```python
from cobo_waas2.models.estimated_fil_fee_slow import EstimatedFILFeeSlow

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedFILFeeSlow from a JSON string
estimated_fil_fee_slow_instance = EstimatedFILFeeSlow.from_json(json)
# print the JSON string representation of the object
print(EstimatedFILFeeSlow.to_json())

# convert the object into a dict
estimated_fil_fee_slow_dict = estimated_fil_fee_slow_instance.to_dict()
# create an instance of EstimatedFILFeeSlow from a dict
estimated_fil_fee_slow_from_dict = EstimatedFILFeeSlow.from_dict(estimated_fil_fee_slow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


