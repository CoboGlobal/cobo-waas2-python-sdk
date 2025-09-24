# AutoSweepTask

The auto sweep task information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | The auto sweep task ID. | 
**wallet_id** | **str** | The wallet ID. | 
**token_id** | **str** | The token ID of the swept token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 
**status** | [**AutoSweepTaskStatus**](AutoSweepTaskStatus.md) |  | 
**transaction_ids** | **List[str]** | The IDs of the corresponding transactions of the auto sweep task. | [optional] 
**failed_reasons** | **List[str]** | Failed reason of create auto sweep transaction. | [optional] 
**created_timestamp** | **int** | The time when the task was created, in Unix timestamp format, measured in milliseconds. | 
**updated_timestamp** | **int** | The time when the task was updated, in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.auto_sweep_task import AutoSweepTask

# TODO update the JSON string below
json = "{}"
# create an instance of AutoSweepTask from a JSON string
auto_sweep_task_instance = AutoSweepTask.from_json(json)
# print the JSON string representation of the object
print(AutoSweepTask.to_json())

# convert the object into a dict
auto_sweep_task_dict = auto_sweep_task_instance.to_dict()
# create an instance of AutoSweepTask from a dict
auto_sweep_task_from_dict = AutoSweepTask.from_dict(auto_sweep_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


