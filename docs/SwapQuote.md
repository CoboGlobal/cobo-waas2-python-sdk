# SwapQuote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | **str** | The unique id of quote. | 
**pay_token_id** | **str** | The token ID to pay. | 
**pay_amount** | **str** | The amount of tokens to pay. | 
**receive_token_id** | **str** | The token ID to receive. | 
**receive_amount** | **str** | The amount of tokens to receive. | 
**fee_token_id** | **str** | The token ID for the service fee. | 
**fee_amount** | **str** | The amount of tokens for the service fee. | 
**min_receive_amount** | **str** | The minimum amount of tokens to receive if the pay amount is specified. | [optional] 
**max_pay_amount** | **str** | The maximum amount of tokens to pay if the receive amount is specified. | [optional] 
**quote_expired_timestamp** | **int** | The time when the quote will expire, in Unix timestamp format, measured in milliseconds. | 

## Example

```python
from cobo_waas2.models.swap_quote import SwapQuote

# TODO update the JSON string below
json = "{}"
# create an instance of SwapQuote from a JSON string
swap_quote_instance = SwapQuote.from_json(json)
# print the JSON string representation of the object
print(SwapQuote.to_json())

# convert the object into a dict
swap_quote_dict = swap_quote_instance.to_dict()
# create an instance of SwapQuote from a dict
swap_quote_from_dict = SwapQuote.from_dict(swap_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


