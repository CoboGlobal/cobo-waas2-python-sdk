# FeeReserved


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reserved_fee** | **str** | The estimated fee required for submitting the transaction data to L1 (Layer 1), measured in wei. | [optional] 

## Example

```python
from cobo_waas2.models.fee_reserved import FeeReserved

# TODO update the JSON string below
json = "{}"
# create an instance of FeeReserved from a JSON string
fee_reserved_instance = FeeReserved.from_json(json)
# print the JSON string representation of the object
print(FeeReserved.to_json())

# convert the object into a dict
fee_reserved_dict = fee_reserved_instance.to_dict()
# create an instance of FeeReserved from a dict
fee_reserved_from_dict = FeeReserved.from_dict(fee_reserved_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


