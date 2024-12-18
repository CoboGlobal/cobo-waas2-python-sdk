# FeeAmount

The transaction fee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_amount** | **str** | The transaction fee that you need to pay for the transaction. | [optional] 

## Example

```python
from cobo_waas2.models.fee_amount import FeeAmount

# TODO update the JSON string below
json = "{}"
# create an instance of FeeAmount from a JSON string
fee_amount_instance = FeeAmount.from_json(json)
# print the JSON string representation of the object
print(FeeAmount.to_json())

# convert the object into a dict
fee_amount_dict = fee_amount_instance.to_dict()
# create an instance of FeeAmount from a dict
fee_amount_from_dict = FeeAmount.from_dict(fee_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


