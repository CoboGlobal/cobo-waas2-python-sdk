# LinkDisplayInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**developer_name** | **str** | The brand name to display to end users during the payment process.  | [optional] 
**logo** | **str** | The URL of your logo image to display to end users during the payment process.  | [optional] 

## Example

```python
from cobo_waas2.models.link_display_info import LinkDisplayInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LinkDisplayInfo from a JSON string
link_display_info_instance = LinkDisplayInfo.from_json(json)
# print the JSON string representation of the object
print(LinkDisplayInfo.to_json())

# convert the object into a dict
link_display_info_dict = link_display_info_instance.to_dict()
# create an instance of LinkDisplayInfo from a dict
link_display_info_from_dict = LinkDisplayInfo.from_dict(link_display_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


