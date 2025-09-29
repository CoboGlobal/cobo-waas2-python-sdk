# SwapEstimateFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The unique identifier of the wallet to pay. | 
**address** | **str** | The wallet address, required when the wallet is not a custodial wallet. | [optional] 
**quote_id** | **str** | The unique identifier of the quote. | 
**fee_type** | [**FeeType**](FeeType.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.swap_estimate_fee import SwapEstimateFee

# TODO update the JSON string below
json = "{}"
# create an instance of SwapEstimateFee from a JSON string
swap_estimate_fee_instance = SwapEstimateFee.from_json(json)
# print the JSON string representation of the object
print(SwapEstimateFee.to_json())

# convert the object into a dict
swap_estimate_fee_dict = swap_estimate_fee_instance.to_dict()
# create an instance of SwapEstimateFee from a dict
swap_estimate_fee_from_dict = SwapEstimateFee.from_dict(swap_estimate_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


