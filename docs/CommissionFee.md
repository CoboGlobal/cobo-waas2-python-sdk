# CommissionFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_amount** | **str** | The amount of the commission fee charged by Cobo for pay-ins and payouts, in USD. | 

## Example

```python
from cobo_waas2.models.commission_fee import CommissionFee

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionFee from a JSON string
commission_fee_instance = CommissionFee.from_json(json)
# print the JSON string representation of the object
print(CommissionFee.to_json())

# convert the object into a dict
commission_fee_dict = commission_fee_instance.to_dict()
# create an instance of CommissionFee from a dict
commission_fee_from_dict = CommissionFee.from_dict(commission_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


