# PaymentSubscriptionPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** | The plan id in cobo. | 
**developer_plan_id** | **str** | The developer plan id. | 
**period_type** | [**PaymentSubscriptionPeriodType**](PaymentSubscriptionPeriodType.md) |  | 
**periods** | **int** |  | 
**interval** | **int** |  | 
**trial_period** | **int** | probation period | [optional] 
**amount** | **str** | The subscription plan amount.  - If &#x60;currency&#x60; is set, this represents the subscription amount in the specified fiat currency. - If &#x60;currency&#x60; isn&#39;t set, this represents the settlement amount in the specified cryptocurrency.  | 
**token_id** | **str** | The ID of the cryptocurrency you want to subscription. Supported values:  - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDCOIN&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC2&#x60;, &#x60;BSC_USDC&#x60; - USDT: &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | [optional] 
**currency** | **str** | The fiat currency for settling the cryptocurrency. Currently, only &#x60;USD&#x60; is supported. Specify this field when &#x60;payout_channel&#x60; is set to &#x60;OffRamp&#x60;. | [optional] 

## Example

```python
from cobo_waas2.models.payment_subscription_plan import PaymentSubscriptionPlan

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSubscriptionPlan from a JSON string
payment_subscription_plan_instance = PaymentSubscriptionPlan.from_json(json)
# print the JSON string representation of the object
print(PaymentSubscriptionPlan.to_json())

# convert the object into a dict
payment_subscription_plan_dict = payment_subscription_plan_instance.to_dict()
# create an instance of PaymentSubscriptionPlan from a dict
payment_subscription_plan_from_dict = PaymentSubscriptionPlan.from_dict(payment_subscription_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


