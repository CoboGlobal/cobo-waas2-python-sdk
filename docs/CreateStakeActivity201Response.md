# CreateStakeActivity201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | The activity ID. | 
**staking_id** | **str** | The ID of the staking position. | [optional] 

## Example

```python
from cobo_waas2.models.create_stake_activity201_response import CreateStakeActivity201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStakeActivity201Response from a JSON string
create_stake_activity201_response_instance = CreateStakeActivity201Response.from_json(json)
# print the JSON string representation of the object
print(CreateStakeActivity201Response.to_json())

# convert the object into a dict
create_stake_activity201_response_dict = create_stake_activity201_response_instance.to_dict()
# create an instance of CreateStakeActivity201Response from a dict
create_stake_activity201_response_from_dict = CreateStakeActivity201Response.from_dict(create_stake_activity201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


