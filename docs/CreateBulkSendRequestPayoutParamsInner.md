# CreateBulkSendRequestPayoutParamsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID of the cryptocurrency to be sent to the recipient. | 
**receiving_address** | **str** | The receiving address. | 
**amount** | **str** | The amount of the cryptocurrency to be sent to the recipient. | 
**description** | **str** | A note or comment about the bulk send item. | [optional] 

## Example

```python
from cobo_waas2.models.create_bulk_send_request_payout_params_inner import CreateBulkSendRequestPayoutParamsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBulkSendRequestPayoutParamsInner from a JSON string
create_bulk_send_request_payout_params_inner_instance = CreateBulkSendRequestPayoutParamsInner.from_json(json)
# print the JSON string representation of the object
print(CreateBulkSendRequestPayoutParamsInner.to_json())

# convert the object into a dict
create_bulk_send_request_payout_params_inner_dict = create_bulk_send_request_payout_params_inner_instance.to_dict()
# create an instance of CreateBulkSendRequestPayoutParamsInner from a dict
create_bulk_send_request_payout_params_inner_from_dict = CreateBulkSendRequestPayoutParamsInner.from_dict(create_bulk_send_request_payout_params_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


