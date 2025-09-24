# PaymentCreateSubscriptionAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The subscription action request id. | 
**plan_id** | **str** | The subscription plan id in cobo. | 
**merchant_id** | **str** | The merchant id in cobo. | 
**data** | [**PaymentSubscriptionActionData**](PaymentSubscriptionActionData.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.payment_create_subscription_action import PaymentCreateSubscriptionAction

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCreateSubscriptionAction from a JSON string
payment_create_subscription_action_instance = PaymentCreateSubscriptionAction.from_json(json)
# print the JSON string representation of the object
print(PaymentCreateSubscriptionAction.to_json())

# convert the object into a dict
payment_create_subscription_action_dict = payment_create_subscription_action_instance.to_dict()
# create an instance of PaymentCreateSubscriptionAction from a dict
payment_create_subscription_action_from_dict = PaymentCreateSubscriptionAction.from_dict(payment_create_subscription_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


