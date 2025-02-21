# CreateSwapActivityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The unique identifier of the wallet. | 
**quote_id** | **str** | The unique identifier of the quote. | 
**slippage_tolerance** | **str** | The slippage tolerance for the swap. | 
**app_initiator** | **str** | The initiator of the app activity. If you do not specify this property, the WaaS service will automatically designate the API key as the initiator. | [optional] 

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


