# PolicyAction

The action to be executed when the policy conditions are satisfied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**PolicyActionType**](PolicyActionType.md) |  | 
**content** | [**PolicyActionContent**](PolicyActionContent.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.policy_action import PolicyAction

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyAction from a JSON string
policy_action_instance = PolicyAction.from_json(json)
# print the JSON string representation of the object
print(PolicyAction.to_json())

# convert the object into a dict
policy_action_dict = policy_action_instance.to_dict()
# create an instance of PolicyAction from a dict
policy_action_from_dict = PolicyAction.from_dict(policy_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


