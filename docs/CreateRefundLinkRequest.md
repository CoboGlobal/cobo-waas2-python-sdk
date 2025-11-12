# CreateRefundLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_info** | [**RefundLinkBusinessInfo**](RefundLinkBusinessInfo.md) |  | 
**display_info** | [**LinkDisplayInfo**](LinkDisplayInfo.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_refund_link_request import CreateRefundLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRefundLinkRequest from a JSON string
create_refund_link_request_instance = CreateRefundLinkRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRefundLinkRequest.to_json())

# convert the object into a dict
create_refund_link_request_dict = create_refund_link_request_instance.to_dict()
# create an instance of CreateRefundLinkRequest from a dict
create_refund_link_request_from_dict = CreateRefundLinkRequest.from_dict(create_refund_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


