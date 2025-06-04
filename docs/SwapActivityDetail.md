# SwapActivityDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | The unique identifier of the swap activity. | [optional] 
**swap_type** | [**SwapType**](SwapType.md) |  | [optional] 
**status** | [**SwapActivityStatus**](SwapActivityStatus.md) |  | [optional] 
**request_id** | **str** | The request id of the swap activity. | [optional] 
**wallet_id** | **str** | The unique identifier of the wallet. | [optional] 
**pay_token_id** | **str** | The token ID to pay. | [optional] 
**receive_token_id** | **str** | The token ID to receive. | [optional] 
**pay_amount** | **str** | The amount of tokens to bridge. | [optional] 
**receive_amount** | **str** | The amount of tokens to receive. | [optional] 
**fee_token_id** | **str** | The fee token ID. | [optional] 
**fee_amount** | **str** | The amount of fee. | [optional] 
**initiator** | **str** | The initiator of the swap activity. | [optional] 
**initiator_type** | [**TransactionInitiatorType**](TransactionInitiatorType.md) |  | [optional] 
**description** | **str** | The description of the swap activity. | [optional] 
**created_timestamp** | **int** | The time when the swap activity was created, in Unix timestamp format, measured in milliseconds. | [optional] 
**updated_timestamp** | **int** | The time when the swap activity was last updated, in Unix timestamp format, measured in milliseconds. | [optional] 
**timeline** | [**List[SwapActivityTimeline]**](SwapActivityTimeline.md) |  | [optional] 
**approvers** | [**List[SwapActivityApprovers]**](SwapActivityApprovers.md) |  | [optional] 
**signers** | [**List[SwapActivitySigners]**](SwapActivitySigners.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.swap_activity_detail import SwapActivityDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SwapActivityDetail from a JSON string
swap_activity_detail_instance = SwapActivityDetail.from_json(json)
# print the JSON string representation of the object
print(SwapActivityDetail.to_json())

# convert the object into a dict
swap_activity_detail_dict = swap_activity_detail_instance.to_dict()
# create an instance of SwapActivityDetail from a dict
swap_activity_detail_from_dict = SwapActivityDetail.from_dict(swap_activity_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


