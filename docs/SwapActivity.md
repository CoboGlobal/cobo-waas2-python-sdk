# SwapActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | The unique identifier of the swap activity. | [optional] 
**swap_type** | [**SwapType**](SwapType.md) |  | [optional] 
**status** | [**SwapActivityStatus**](SwapActivityStatus.md) |  | [optional] 
**request_id** | **str** | The request ID of the swap transaction. | [optional] 
**wallet_id** | **str** | The ID of the wallet used to pay. | [optional] 
**pay_token_id** | **str** | The ID of the token to pay. | [optional] 
**receive_token_id** | **str** | The ID of the token to receive. | [optional] 
**pay_amount** | **str** | The amount of the token to pay. | [optional] 
**receive_amount** | **str** | The amount of the token to receive. | [optional] 
**fee_token_id** | **str** | The ID of the token used for paying the service fee. | [optional] 
**fee_amount** | **str** | The amount of the service fee. | [optional] 
**initiator** | **str** | The initiator of the swap activity. | [optional] 
**initiator_type** | [**TransactionInitiatorType**](TransactionInitiatorType.md) |  | [optional] 
**description** | **str** | The description of the swap activity. | [optional] 
**created_timestamp** | **int** | The time when the swap activity was created, in Unix timestamp format, measured in milliseconds. | [optional] 
**updated_timestamp** | **int** | The time when the swap activity was last updated, in Unix timestamp format, measured in milliseconds. | [optional] 
**network_fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | [optional] 
**destination_address** | **str** | The address of an MPC Wallet or Web3 Wallet that receives the swapped or bridged assets. | [optional] 

## Example

```python
from cobo_waas2.models.swap_activity import SwapActivity

# TODO update the JSON string below
json = "{}"
# create an instance of SwapActivity from a JSON string
swap_activity_instance = SwapActivity.from_json(json)
# print the JSON string representation of the object
print(SwapActivity.to_json())

# convert the object into a dict
swap_activity_dict = swap_activity_instance.to_dict()
# create an instance of SwapActivity from a dict
swap_activity_from_dict = SwapActivity.from_dict(swap_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


