# CreateUnstakeActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a request. The request ID is provided by you and must be unique within your organization. | [optional] 
**staking_id** | **str** | The ID of the corresponding staking position. | 
**amount** | **str** | The amount to unstake. For the Babylon protocol, this property is ignored. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_unstake_activity import CreateUnstakeActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUnstakeActivity from a JSON string
create_unstake_activity_instance = CreateUnstakeActivity.from_json(json)
# print the JSON string representation of the object
print(CreateUnstakeActivity.to_json())

# convert the object into a dict
create_unstake_activity_dict = create_unstake_activity_instance.to_dict()
# create an instance of CreateUnstakeActivity from a dict
create_unstake_activity_from_dict = CreateUnstakeActivity.from_dict(create_unstake_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


