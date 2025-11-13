# PaymentSubscriptionActionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**PaymentSubscriptionActionType**](PaymentSubscriptionActionType.md) |  | 
**user_address** | **str** | The subscription user address. | 
**token_id** | **str** | The ID of the cryptocurrency you want to subscription. Supported values:  - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDCOIN&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC2&#x60;, &#x60;BSC_USDC&#x60; - USDT: &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
**charge_amount** | **str** | The subscription plan crypto amount with input token_id.  | 
**subscription_id** | **str** | The subscription id in cobo. | 
**signature** | **str** | The signature for transaction. charge action is not required. | 
**deadline** | **int** | The signature deadline for transaction. charge action is not required. | 
**periods** | **int** | The periods needed updated. | 
**new_plan_id** | **str** | The new plan id in cobo. | 

## Example

```python
from cobo_waas2.models.payment_subscription_action_data import PaymentSubscriptionActionData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSubscriptionActionData from a JSON string
payment_subscription_action_data_instance = PaymentSubscriptionActionData.from_json(json)
# print the JSON string representation of the object
print(PaymentSubscriptionActionData.to_json())

# convert the object into a dict
payment_subscription_action_data_dict = payment_subscription_action_data_instance.to_dict()
# create an instance of PaymentSubscriptionActionData from a dict
payment_subscription_action_data_from_dict = PaymentSubscriptionActionData.from_dict(payment_subscription_action_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


