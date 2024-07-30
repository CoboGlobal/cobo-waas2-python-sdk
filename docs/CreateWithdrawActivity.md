# CreateWithdrawActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staking_id** | **str** | The id of the related staking. | 
**amount** | **str** | The amount to stake | [optional] 
**address** | **str** | The withdraw to address. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | 

## Example

```python
from cobo_waas2.models.create_withdraw_activity import CreateWithdrawActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWithdrawActivity from a JSON string
create_withdraw_activity_instance = CreateWithdrawActivity.from_json(json)
# print the JSON string representation of the object
print(CreateWithdrawActivity.to_json())

# convert the object into a dict
create_withdraw_activity_dict = create_withdraw_activity_instance.to_dict()
# create an instance of CreateWithdrawActivity from a dict
create_withdraw_activity_from_dict = CreateWithdrawActivity.from_dict(create_withdraw_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


