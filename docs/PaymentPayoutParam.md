# PaymentPayoutParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The ID of the cryptocurrency you want to pay out. Specify this field when &#x60;payout_channel&#x60; is set to &#x60;Crypto&#x60;. Supported values: - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDC&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC&#x60;, &#x60;BSC_USDC&#x60; - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
**amount** | **str** | The payout cryptocurrency amount.  | 

## Example

```python
from cobo_waas2.models.payment_payout_param import PaymentPayoutParam

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPayoutParam from a JSON string
payment_payout_param_instance = PaymentPayoutParam.from_json(json)
# print the JSON string representation of the object
print(PaymentPayoutParam.to_json())

# convert the object into a dict
payment_payout_param_dict = payment_payout_param_instance.to_dict()
# create an instance of PaymentPayoutParam from a dict
payment_payout_param_from_dict = PaymentPayoutParam.from_dict(payment_payout_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


