# CreateAutoSweepTask

Wallet and token information required to create an auto-sweep task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | ID of the wallet where the token will be swept. | 
**token_id** | **str** | ID of the token to be swept. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 

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


