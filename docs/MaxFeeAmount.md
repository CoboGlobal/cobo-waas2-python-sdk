# MaxFeeAmount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_fee_amount** | **str** | The maximum fee that you are willing to pay for the transaction. Provide the value without applying precision. The transaction will fail if the transaction fee exceeds the maximum fee. | [optional] 

## Example

```python
from cobo_waas2.models.max_fee_amount import MaxFeeAmount

# TODO update the JSON string below
json = "{}"
# create an instance of MaxFeeAmount from a JSON string
max_fee_amount_instance = MaxFeeAmount.from_json(json)
# print the JSON string representation of the object
print(MaxFeeAmount.to_json())

# convert the object into a dict
max_fee_amount_dict = max_fee_amount_instance.to_dict()
# create an instance of MaxFeeAmount from a dict
max_fee_amount_from_dict = MaxFeeAmount.from_dict(max_fee_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


