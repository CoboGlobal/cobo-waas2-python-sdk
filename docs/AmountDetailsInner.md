# AmountDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**AmountStatus**](AmountStatus.md) |  | 
**amount** | **str** | The staking amount. | 

## Example

```python
from cobo_waas2.models.amount_details_inner import AmountDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AmountDetailsInner from a JSON string
amount_details_inner_instance = AmountDetailsInner.from_json(json)
# print the JSON string representation of the object
print(AmountDetailsInner.to_json())

# convert the object into a dict
amount_details_inner_dict = amount_details_inner_instance.to_dict()
# create an instance of AmountDetailsInner from a dict
amount_details_inner_from_dict = AmountDetailsInner.from_dict(amount_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


