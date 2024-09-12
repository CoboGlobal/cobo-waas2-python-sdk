# CreateStakeActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a request. The request ID is provided by you and must be unique within your organization. | [optional] 
**source** | [**StakingSource**](StakingSource.md) |  | [optional] 
**pool_id** | **str** | The ID of the staking pool. | 
**amount** | **str** | The amount to stake. | 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | 
**extra** | [**CreateStakeActivityExtra**](CreateStakeActivityExtra.md) |  | 

## Example

```python
from cobo_waas2.models.create_stake_activity import CreateStakeActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStakeActivity from a JSON string
create_stake_activity_instance = CreateStakeActivity.from_json(json)
# print the JSON string representation of the object
print(CreateStakeActivity.to_json())

# convert the object into a dict
create_stake_activity_dict = create_stake_activity_instance.to_dict()
# create an instance of CreateStakeActivity from a dict
create_stake_activity_from_dict = CreateStakeActivity.from_dict(create_stake_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


