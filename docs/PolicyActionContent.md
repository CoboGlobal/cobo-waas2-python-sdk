# PolicyActionContent

The information of an app workflow policy quorum action content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The quorum action content type. Possible values include:    - &#x60;FULL_APPROVAL&#x60;: The content type is approved by all persons.   - &#x60;PART_APPROVAL&#x60;: The content type is approved by some persons.  | 
**roles** | **List[str]** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 
**threshold** | **int** | The number of persons need approved, such as 2. | [optional] 

## Example

```python
from cobo_waas2.models.policy_action_content import PolicyActionContent

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyActionContent from a JSON string
policy_action_content_instance = PolicyActionContent.from_json(json)
# print the JSON string representation of the object
print(PolicyActionContent.to_json())

# convert the object into a dict
policy_action_content_dict = policy_action_content_instance.to_dict()
# create an instance of PolicyActionContent from a dict
policy_action_content_from_dict = PolicyActionContent.from_dict(policy_action_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


