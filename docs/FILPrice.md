# FILPrice

The transaction gas price configuration based on the Filecoin fee model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_premium** | **str** | An optional tip you can include to prioritize your transaction. The gas premium incentivizes miners to include your transaction sooner than those offering only the base fee. | [optional] 
**gas_fee_cap** | **str** | The maximum gas price you are willing to pay per unit of gas. | [optional] 
**gas_limit** | **str** | The maximum amount of gas your transaction is allowed to consume. | [optional] 

## Example

```python
from cobo_waas2.models.fil_price import FILPrice

# TODO update the JSON string below
json = "{}"
# create an instance of FILPrice from a JSON string
fil_price_instance = FILPrice.from_json(json)
# print the JSON string representation of the object
print(FILPrice.to_json())

# convert the object into a dict
fil_price_dict = fil_price_instance.to_dict()
# create an instance of FILPrice from a dict
fil_price_from_dict = FILPrice.from_dict(fil_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


