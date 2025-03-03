# CreateSwapQuoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The unique identifier of the wallet. | 
**pay_token_id** | **str** | Unique id of the token to pay. | 
**receive_token_id** | **str** | Unique id of the token to receive. | 
**pay_amount** | **str** | Amount of tokens to pay. For example \&quot;0.5 BTC\&quot;. Note: Either pay_amount or receive_amount must be provided, but not both.  | [optional] 
**receive_amount** | **str** | Amount of tokens to receive. For example \&quot;0.5 ETH_WBTC\&quot;. Note: Either pay_amount or receive_amount must be provided, but not both.  | [optional] 

## Example

```python
from cobo_waas2.models.create_swap_quote_request import CreateSwapQuoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSwapQuoteRequest from a JSON string
create_swap_quote_request_instance = CreateSwapQuoteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSwapQuoteRequest.to_json())

# convert the object into a dict
create_swap_quote_request_dict = create_swap_quote_request_instance.to_dict()
# create an instance of CreateSwapQuoteRequest from a dict
create_swap_quote_request_from_dict = CreateSwapQuoteRequest.from_dict(create_swap_quote_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


