# Activity

The staking activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The activity ID. | [optional] 
**initiator** | **str** | The initiator of the activity. | [optional] 
**initiator_type** | [**TransactionInitiatorType**](TransactionInitiatorType.md) |  | [optional] 
**type** | [**ActivityType**](ActivityType.md) |  | [optional] 
**wallet_id** | **str** | The staker&#39;s wallet ID. | [optional] 
**address** | **str** | The staker&#39;s wallet address. | [optional] 
**pool_id** | **str** | The ID of the staking pool. | 
**token_id** | **str** | The token ID. | 
**staking_id** | **str** | The ID of the corresponding staking position. | [optional] 
**amount** | **str** | The staking amount. | 
**transaction_ids** | **List[str]** | The IDs of the corresponding transactions of the activity. | [optional] 
**timeline** | [**List[ActivityTimeline]**](ActivityTimeline.md) | The timeline of the activity. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | [optional] 
**status** | [**ActivityStatus**](ActivityStatus.md) |  | 
**created_timestamp** | **int** | The time when the activity was created. | [optional] 
**updated_timestamp** | **int** | The time when the activity was last updated. | [optional] 

## Example

```python
from cobo_waas2.models.activity import Activity

# TODO update the JSON string below
json = "{}"
# create an instance of Activity from a JSON string
activity_instance = Activity.from_json(json)
# print the JSON string representation of the object
print(Activity.to_json())

# convert the object into a dict
activity_dict = activity_instance.to_dict()
# create an instance of Activity from a dict
activity_from_dict = Activity.from_dict(activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


