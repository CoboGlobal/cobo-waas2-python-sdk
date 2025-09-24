# PaymentBaseSubscriptionActionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**PaymentSubscriptionAction**](PaymentSubscriptionAction.md) |  | 
**subscription_id** | **str** | The subscription id in cobo. | 
**signature** | **str** | The signature for transaction. | 

## Example

```python
from cobo_waas2.models.payment_base_subscription_action_data import PaymentBaseSubscriptionActionData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBaseSubscriptionActionData from a JSON string
payment_base_subscription_action_data_instance = PaymentBaseSubscriptionActionData.from_json(json)
# print the JSON string representation of the object
print(PaymentBaseSubscriptionActionData.to_json())

# convert the object into a dict
payment_base_subscription_action_data_dict = payment_base_subscription_action_data_instance.to_dict()
# create an instance of PaymentBaseSubscriptionActionData from a dict
payment_base_subscription_action_data_from_dict = PaymentBaseSubscriptionActionData.from_dict(payment_base_subscription_action_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


