# PaymentUpdateTokenIdSubscriptionActionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**PaymentSubscriptionActionType**](PaymentSubscriptionActionType.md) |  | 
**subscription_id** | **str** | The subscription id in cobo. | 
**token_id** | **str** | The ID of the cryptocurrency you want to subscription. Supported values:  - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDCOIN&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC2&#x60;, &#x60;BSC_USDC&#x60; - USDT: &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
**signature** | **str** | The signature for transaction. charge action is not required. | 
**deadline** | **int** | The signature deadline for transaction. charge action is not required. | 

## Example

```python
from cobo_waas2.models.payment_update_token_id_subscription_action_data import PaymentUpdateTokenIdSubscriptionActionData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentUpdateTokenIdSubscriptionActionData from a JSON string
payment_update_token_id_subscription_action_data_instance = PaymentUpdateTokenIdSubscriptionActionData.from_json(json)
# print the JSON string representation of the object
print(PaymentUpdateTokenIdSubscriptionActionData.to_json())

# convert the object into a dict
payment_update_token_id_subscription_action_data_dict = payment_update_token_id_subscription_action_data_instance.to_dict()
# create an instance of PaymentUpdateTokenIdSubscriptionActionData from a dict
payment_update_token_id_subscription_action_data_from_dict = PaymentUpdateTokenIdSubscriptionActionData.from_dict(payment_update_token_id_subscription_action_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


