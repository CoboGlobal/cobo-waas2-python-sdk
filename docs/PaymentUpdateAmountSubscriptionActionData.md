# PaymentUpdateAmountSubscriptionActionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_plan_id** | **str** | The new plan id in cobo. | 
**action_type** | [**PaymentSubscriptionActionType**](PaymentSubscriptionActionType.md) |  | 
**subscription_id** | **str** | The subscription id in cobo. | 
**signature** | **str** | The signature for transaction. | 

## Example

```python
from cobo_waas2.models.payment_update_amount_subscription_action_data import PaymentUpdateAmountSubscriptionActionData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentUpdateAmountSubscriptionActionData from a JSON string
payment_update_amount_subscription_action_data_instance = PaymentUpdateAmountSubscriptionActionData.from_json(json)
# print the JSON string representation of the object
print(PaymentUpdateAmountSubscriptionActionData.to_json())

# convert the object into a dict
payment_update_amount_subscription_action_data_dict = payment_update_amount_subscription_action_data_instance.to_dict()
# create an instance of PaymentUpdateAmountSubscriptionActionData from a dict
payment_update_amount_subscription_action_data_from_dict = PaymentUpdateAmountSubscriptionActionData.from_dict(payment_update_amount_subscription_action_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


