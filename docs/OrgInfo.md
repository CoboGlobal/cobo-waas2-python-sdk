# OrgInfo

The information of an organization. To learn more about organizations, see [Introduction to Organization](https://manuals.cobo.com/en/portal/organization/introduction). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | The organization ID. | 
**biz_org_id** | **int** | An internal business ID assigned by Cobo. Used mainly by Cobo&#39;s customer support to locate the organization. | [optional] 
**name** | **str** | The organization name. | [optional] 
**created_timestamp** | **int** | The organization&#39;s creation time in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.org_info import OrgInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrgInfo from a JSON string
org_info_instance = OrgInfo.from_json(json)
# print the JSON string representation of the object
print(OrgInfo.to_json())

# convert the object into a dict
org_info_dict = org_info_instance.to_dict()
# create an instance of OrgInfo from a dict
org_info_from_dict = OrgInfo.from_dict(org_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


