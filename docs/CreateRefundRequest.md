# CreateRefundRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a refund request. The request ID is provided by you and must be unique. | 
**merchant_id** | **str** | The merchant ID. | [optional] 
**payable_amount** | **str** | The amount to refund in cryptocurrency. | 
**to_address** | **str** | The address where the refunded cryptocurrency will be sent. | [optional] 
**token_id** | **str** | The ID of the cryptocurrency used for refund. Supported values:    - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDC&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC&#x60;, &#x60;BSC_USDC&#x60;   - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
**refund_type** | [**RefundType**](RefundType.md) |  | 
**order_id** | **str** | The ID of the original pay-in order associated with this refund. Use this to track refunds against specific payments. | [optional] 
**charge_merchant_fee** | **bool** | Indicates whether the merchant should bear the transaction fee for the refund.  If true, the fee will be deducted from merchant&#39;s account balance.  | [optional] 
**merchant_fee_amount** | **str** | The amount of the transaction fee that the merchant will bear for the refund.  This is only applicable if &#x60;charge_merchant_fee&#x60; is set to true.  | [optional] 
**merchant_fee_token_id** | **str** | The ID of the cryptocurrency used for the transaction fee.  This is only applicable if &#x60;charge_merchant_fee&#x60; is set to true.  | [optional] 

## Example

```python
from cobo_waas2.models.create_refund_request import CreateRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRefundRequest from a JSON string
create_refund_request_instance = CreateRefundRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRefundRequest.to_json())

# convert the object into a dict
create_refund_request_dict = create_refund_request_instance.to_dict()
# create an instance of CreateRefundRequest from a dict
create_refund_request_from_dict = CreateRefundRequest.from_dict(create_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


