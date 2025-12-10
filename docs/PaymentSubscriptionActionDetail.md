# PaymentSubscriptionActionDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The action request id. | 
**action_id** | **str** | The action id. | 
**plan_id** | **str** | The plan id in cobo. | 
**subscription_id** | **str** | The subscription id in cobo. | 
**merchant_id** | **str** | The merchant id in cobo. | 
**merchant_address** | **str** | The merchant address in cobo. | 
**data** | [**PaymentSubscriptionActionData**](PaymentSubscriptionActionData.md) |  | 
**transaction_ids** | **List[str]** |  | [optional] 
**status** | [**PaymentSubscriptionActionStatus**](PaymentSubscriptionActionStatus.md) |  | 
**created_timestamp** | **int** | The created time of the subscription action, represented as a UNIX timestamp in seconds. | [optional] 
**updated_timestamp** | **int** | The updated time of the subscription action, represented as a UNIX timestamp in seconds. | [optional] 
**subscription** | [**PaymentSubscription**](PaymentSubscription.md) |  | [optional] 
**transactions** | [**List[Transaction]**](Transaction.md) | An array of subscription transactions. | [optional] 

## Example

```python
from cobo_waas2.models.payment_subscription_action_detail import PaymentSubscriptionActionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSubscriptionActionDetail from a JSON string
payment_subscription_action_detail_instance = PaymentSubscriptionActionDetail.from_json(json)
# print the JSON string representation of the object
print(PaymentSubscriptionActionDetail.to_json())

# convert the object into a dict
payment_subscription_action_detail_dict = payment_subscription_action_detail_instance.to_dict()
# create an instance of PaymentSubscriptionActionDetail from a dict
payment_subscription_action_detail_from_dict = PaymentSubscriptionActionDetail.from_dict(payment_subscription_action_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


