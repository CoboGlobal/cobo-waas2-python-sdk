# PspBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The ID of the cryptocurrency. | 
**developer_fee_amount** | **str** | The psp developer fee amount. | [optional] 
**settled_amount** | **str** | The psp settled amount. | [optional] 
**refunded_amount** | **str** | The psp total refunded amount. | [optional] 
**total_balance** | **str** | The psp total balance. | [optional] 
**available_balance** | **str** | The psp available balance. | [optional] 

## Example

```python
from cobo_waas2.models.psp_balance import PspBalance

# TODO update the JSON string below
json = "{}"
# create an instance of PspBalance from a JSON string
psp_balance_instance = PspBalance.from_json(json)
# print the JSON string representation of the object
print(PspBalance.to_json())

# convert the object into a dict
psp_balance_dict = psp_balance_instance.to_dict()
# create an instance of PspBalance from a dict
psp_balance_from_dict = PspBalance.from_dict(psp_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


