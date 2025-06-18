# PolicyActionContent

The definition of the quorum action. This property is applicable only when `action_type` is `Quorum`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The quorum type. Possible values include:    - &#x60;FULL_APPROVAL&#x60;: Requires approval from all participants.   - &#x60;PART_APPROVAL&#x60;: Requires approval from a specified number of participants.  | 
**roles** | **List[str]** | The roles included in the quorum. Possible values include &#x60;admin&#x60;, &#x60;spender&#x60;, &#x60;operator&#x60;, and &#x60;approver&#x60;. | [optional] 
**user_ids** | **List[str]** | The ID of the users included in the quorum. | [optional] 
**threshold** | **int** | The number of approvers required to meet the quorum. | [optional] 

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


