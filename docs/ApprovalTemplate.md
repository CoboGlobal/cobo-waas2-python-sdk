# ApprovalTemplate

The template for transaction approval details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_key** | **str** | The business key that is used to identify the transaction. | [optional] 
**template_text** | **str** | The template text that is used for the transaction approval. | [optional] 
**template_version** | **str** | The version of the template used for the transaction approval. | [optional] 

## Example

```python
from cobo_waas2.models.approval_template import ApprovalTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalTemplate from a JSON string
approval_template_instance = ApprovalTemplate.from_json(json)
# print the JSON string representation of the object
print(ApprovalTemplate.to_json())

# convert the object into a dict
approval_template_dict = approval_template_instance.to_dict()
# create an instance of ApprovalTemplate from a dict
approval_template_from_dict = ApprovalTemplate.from_dict(approval_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


