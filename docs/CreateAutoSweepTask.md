# CreateAutoSweepTask

The sweep to address information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The wallet ID. | 
**token_id** | **str** | The token ID of the swept token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 

## Example

```python
from cobo_waas2.models.create_auto_sweep_task import CreateAutoSweepTask

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAutoSweepTask from a JSON string
create_auto_sweep_task_instance = CreateAutoSweepTask.from_json(json)
# print the JSON string representation of the object
print(CreateAutoSweepTask.to_json())

# convert the object into a dict
create_auto_sweep_task_dict = create_auto_sweep_task_instance.to_dict()
# create an instance of CreateAutoSweepTask from a dict
create_auto_sweep_task_from_dict = CreateAutoSweepTask.from_dict(create_auto_sweep_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


