# CreateOrderLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_info** | [**OrderLinkBusinessInfo**](OrderLinkBusinessInfo.md) |  | 
**display_info** | [**LinkDisplayInfo**](LinkDisplayInfo.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_order_link_request import CreateOrderLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderLinkRequest from a JSON string
create_order_link_request_instance = CreateOrderLinkRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrderLinkRequest.to_json())

# convert the object into a dict
create_order_link_request_dict = create_order_link_request_instance.to_dict()
# create an instance of CreateOrderLinkRequest from a dict
create_order_link_request_from_dict = CreateOrderLinkRequest.from_dict(create_order_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


