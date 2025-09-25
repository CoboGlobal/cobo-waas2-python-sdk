# PaymentApproveSubscriptionActionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**PaymentSubscriptionActionType**](PaymentSubscriptionActionType.md) |  | 
**subscription_id** | **str** | The subscription id in cobo. | 
**permit_data** | **str** | The signature of permit. | [optional] 

## Example

```python
from cobo_waas2.models.payment_approve_subscription_action_data import PaymentApproveSubscriptionActionData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentApproveSubscriptionActionData from a JSON string
payment_approve_subscription_action_data_instance = PaymentApproveSubscriptionActionData.from_json(json)
# print the JSON string representation of the object
print(PaymentApproveSubscriptionActionData.to_json())

# convert the object into a dict
payment_approve_subscription_action_data_dict = payment_approve_subscription_action_data_instance.to_dict()
# create an instance of PaymentApproveSubscriptionActionData from a dict
payment_approve_subscription_action_data_from_dict = PaymentApproveSubscriptionActionData.from_dict(payment_approve_subscription_action_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


