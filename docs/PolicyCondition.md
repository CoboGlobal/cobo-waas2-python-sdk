# PolicyCondition

The information of an app workflow policy condition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The app workflow field name. | 
**value_type** | [**PolicyFieldValueType**](PolicyFieldValueType.md) |  | 
**value** | **str** | The app workflow field value. | 
**operator** | [**PolicyFieldOperator**](PolicyFieldOperator.md) |  | 

## Example

```python
from cobo_waas2.models.policy_condition import PolicyCondition

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyCondition from a JSON string
policy_condition_instance = PolicyCondition.from_json(json)
# print the JSON string representation of the object
print(PolicyCondition.to_json())

# convert the object into a dict
policy_condition_dict = policy_condition_instance.to_dict()
# create an instance of PolicyCondition from a dict
policy_condition_from_dict = PolicyCondition.from_dict(policy_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


