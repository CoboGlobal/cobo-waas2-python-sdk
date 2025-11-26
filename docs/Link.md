# Link


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The base URL of the page. This URL should be combined with the &#x60;token&#x60; parameter to form the complete link.  | 
**token** | **str** | The token appended to the URL as a query parameter. This token identifies and authenticates a specific payment or refund session.  The complete link should be constructed as: &#x60;[url]?token&#x3D;[token]&#x60;  | 

## Example

```python
from cobo_waas2.models.link import Link

# TODO update the JSON string below
json = "{}"
# create an instance of Link from a JSON string
link_instance = Link.from_json(json)
# print the JSON string representation of the object
print(Link.to_json())

# convert the object into a dict
link_dict = link_instance.to_dict()
# create an instance of Link from a dict
link_from_dict = Link.from_dict(link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


