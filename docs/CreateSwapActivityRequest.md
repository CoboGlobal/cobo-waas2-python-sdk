# CreateSwapActivityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The ID of the wallet used to pay. | 
**address** | **str** | The address of the wallet used to pay. | [optional] 
**quote_id** | **str** | The unique identifier of the swap quote. | 
**app_initiator** | **str** | The initiator of the swap activity. It is optional and defaults to your API key if not specified. | [optional] 
**request_id** | **str** | The request ID of the swap activity. | [optional] 
**receiver_address** | **str** | The destination address of the swap activity. This property is required only when the swap type is &#x60;Bridge&#x60; and the wallet is not a Custodial Wallet (Asset Wallet). | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_swap_activity_request import CreateSwapActivityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSwapActivityRequest from a JSON string
create_swap_activity_request_instance = CreateSwapActivityRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSwapActivityRequest.to_json())

# convert the object into a dict
create_swap_activity_request_dict = create_swap_activity_request_instance.to_dict()
# create an instance of CreateSwapActivityRequest from a dict
create_swap_activity_request_from_dict = CreateSwapActivityRequest.from_dict(create_swap_activity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


