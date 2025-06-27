# UpdateRefundByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_address** | **str** | The address where the refunded cryptocurrency will be sent. | 

## Example

```python
from cobo_waas2.models.update_refund_by_id_request import UpdateRefundByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRefundByIdRequest from a JSON string
update_refund_by_id_request_instance = UpdateRefundByIdRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRefundByIdRequest.to_json())

# convert the object into a dict
update_refund_by_id_request_dict = update_refund_by_id_request_instance.to_dict()
# create an instance of UpdateRefundByIdRequest from a dict
update_refund_by_id_request_from_dict = UpdateRefundByIdRequest.from_dict(update_refund_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


