# CreateSwapQuote201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_amount** | **str** | The amount of tokens to pay. | 
**receive_amount** | **str** | The amount of tokens to receive. | 
**fee_amount** | **str** | The amount of tokens to pay for fee. | 
**min_pay_amount** | **str** | The minimum amount of tokens to pay. | [optional] 
**max_pay_amount** | **str** | The maximum amount of tokens to pay. | [optional] 
**min_receive_amount** | **str** | The minimum amount of tokens to receive. | [optional] 
**max_receive_amount** | **str** | The maximum amount of tokens to receive. | [optional] 
**quote_expired_timestamp** | **int** | The time when the quote will expire, in Unix timestamp format, measured in milliseconds. | 
**quote_id** | **str** | The unique identifier of this quote. | 

## Example

```python
from cobo_waas2.models.create_swap_quote201_response import CreateSwapQuote201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSwapQuote201Response from a JSON string
create_swap_quote201_response_instance = CreateSwapQuote201Response.from_json(json)
# print the JSON string representation of the object
print(CreateSwapQuote201Response.to_json())

# convert the object into a dict
create_swap_quote201_response_dict = create_swap_quote201_response_instance.to_dict()
# create an instance of CreateSwapQuote201Response from a dict
create_swap_quote201_response_from_dict = CreateSwapQuote201Response.from_dict(create_swap_quote201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


