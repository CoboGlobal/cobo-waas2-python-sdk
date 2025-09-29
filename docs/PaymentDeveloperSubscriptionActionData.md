# PaymentDeveloperSubscriptionActionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**PaymentSubscriptionActionType**](PaymentSubscriptionActionType.md) |  | 
**subscription_id** | **str** | The subscription id in cobo. | 

## Example

```python
from cobo_waas2.models.payment_developer_subscription_action_data import PaymentDeveloperSubscriptionActionData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDeveloperSubscriptionActionData from a JSON string
payment_developer_subscription_action_data_instance = PaymentDeveloperSubscriptionActionData.from_json(json)
# print the JSON string representation of the object
print(PaymentDeveloperSubscriptionActionData.to_json())

# convert the object into a dict
payment_developer_subscription_action_data_dict = payment_developer_subscription_action_data_instance.to_dict()
# create an instance of PaymentDeveloperSubscriptionActionData from a dict
payment_developer_subscription_action_data_from_dict = PaymentDeveloperSubscriptionActionData.from_dict(payment_developer_subscription_action_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


