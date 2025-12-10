# PaymentSubscribeAndChargeSubscriptionActionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**PaymentSubscriptionActionType**](PaymentSubscriptionActionType.md) |  | 
**subscription_id** | **str** | The subscription id in cobo. | 
**charge_amount** | **str** | The subscription crypto amount, less than subscription plan amount.  | 
**signature** | **str** | The signature for transaction. charge action is not required. | 
**deadline** | **int** | The signature deadline for transaction. charge action is not required. | 

## Example

```python
from cobo_waas2.models.payment_subscribe_and_charge_subscription_action_data import PaymentSubscribeAndChargeSubscriptionActionData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSubscribeAndChargeSubscriptionActionData from a JSON string
payment_subscribe_and_charge_subscription_action_data_instance = PaymentSubscribeAndChargeSubscriptionActionData.from_json(json)
# print the JSON string representation of the object
print(PaymentSubscribeAndChargeSubscriptionActionData.to_json())

# convert the object into a dict
payment_subscribe_and_charge_subscription_action_data_dict = payment_subscribe_and_charge_subscription_action_data_instance.to_dict()
# create an instance of PaymentSubscribeAndChargeSubscriptionActionData from a dict
payment_subscribe_and_charge_subscription_action_data_from_dict = PaymentSubscribeAndChargeSubscriptionActionData.from_dict(payment_subscribe_and_charge_subscription_action_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


