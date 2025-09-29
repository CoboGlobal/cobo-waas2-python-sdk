# FILPrice

The transaction gas price based on the FIL fee model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_premium** | **str** | An optional additional fee that users can include to prioritize their transactions over others. It acts like a tip to incentivize miners to select and include your transaction over transactions with only the base fee. | [optional] 
**gas_fee_cap** | **str** | The gas_fee_cap is a user-defined limit on how much they are willing to pay per unit of gas. | [optional] 
**gas_limit** | **str** | This defines the maximum amount of computational effort that a transaction is allowed to consume. It&#39;s a way to cap the resources that a transaction can use, ensuring it doesn&#39;t consume excessive network resources. | [optional] 

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


