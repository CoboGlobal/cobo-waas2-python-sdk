# PaymentSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** | The plan id in cobo. | 
**subscription_id** | **str** | The subscription id in cobo. | 
**merchant_id** | **str** | The merchant id in cobo. | 
**merchant_address** | **str** | The merchant address in cobo. | 
**user_address** | **str** | The user address in subscription. | 
**token_id** | **str** | The token_id in subscription. | 
**charge_amount** | **str** | The charge amount in subscription. | [optional] 
**start_time** | **int** | The subscription start timestamp. | 
**expiration_time** | **int** | The subscription expired timestamp. | 
**charges_made** | **int** | The subscription charge times. | 
**period_type** | [**PaymentSubscriptionPeriodType**](PaymentSubscriptionPeriodType.md) |  | 
**periods** | **int** |  | 
**interval** | **int** | The subscription charge interval. | 
**status** | [**PaymentSubscriptionStatus**](PaymentSubscriptionStatus.md) |  | 
**created_timestamp** | **int** | The created time of the subscription, represented as a UNIX timestamp in seconds. | 
**updated_timestamp** | **int** | The updated time of the subscription, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.payment_subscription import PaymentSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSubscription from a JSON string
payment_subscription_instance = PaymentSubscription.from_json(json)
# print the JSON string representation of the object
print(PaymentSubscription.to_json())

# convert the object into a dict
payment_subscription_dict = payment_subscription_instance.to_dict()
# create an instance of PaymentSubscription from a dict
payment_subscription_from_dict = PaymentSubscription.from_dict(payment_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


