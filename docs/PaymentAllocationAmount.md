# PaymentAllocationAmount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The ID of the cryptocurrency. | 
**allocation_amount** | **str** | The allocation amount. | 

## Example

```python
from cobo_waas2.models.payment_allocation_amount import PaymentAllocationAmount

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAllocationAmount from a JSON string
payment_allocation_amount_instance = PaymentAllocationAmount.from_json(json)
# print the JSON string representation of the object
print(PaymentAllocationAmount.to_json())

# convert the object into a dict
payment_allocation_amount_dict = payment_allocation_amount_instance.to_dict()
# create an instance of PaymentAllocationAmount from a dict
payment_allocation_amount_from_dict = PaymentAllocationAmount.from_dict(payment_allocation_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


