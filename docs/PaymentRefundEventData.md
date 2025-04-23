# PaymentRefundEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. | 
**request_id** | **str** | The request ID provided by you when creating the refund request. | [optional] 
**refund_id** | **str** | The refund order ID. | 
**merchant_id** | **str** | The merchant ID. | [optional] 
**token_id** | **str** | The ID of the cryptocurrency used for refund. | 
**chain_id** | **str** | The ID of the blockchain network on which the refund transaction occurs. | 
**amount** | **str** | The amount in cryptocurrency to be returned for this refund order. | 
**to_address** | **str** | The recipient&#39;s wallet address where the refund will be sent. | 
**status** | [**RefundStatus**](RefundStatus.md) |  | 
**transactions** | [**List[PaymentTransaction]**](PaymentTransaction.md) | An array of transactions associated with this refund order. Each transaction represents a separate blockchain operation related to the refund process. | [optional] 

## Example

```python
from cobo_waas2.models.payment_refund_event_data import PaymentRefundEventData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRefundEventData from a JSON string
payment_refund_event_data_instance = PaymentRefundEventData.from_json(json)
# print the JSON string representation of the object
print(PaymentRefundEventData.to_json())

# convert the object into a dict
payment_refund_event_data_dict = payment_refund_event_data_instance.to_dict()
# create an instance of PaymentRefundEventData from a dict
payment_refund_event_data_from_dict = PaymentRefundEventData.from_dict(payment_refund_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


