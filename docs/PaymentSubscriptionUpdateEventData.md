# PaymentSubscriptionUpdateEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The payment address update event data. - &#x60;PaymentPayout&#x60;: The payment payout event data. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The suspended token event data. - &#x60;ComplianceDisposition&#x60;: The compliance disposition event data. - &#x60;ComplianceKytScreenings&#x60;: The compliance KYT screenings event data. - &#x60;ComplianceKyaScreenings&#x60;: The compliance KYA screenings event data. | 
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
from cobo_waas2.models.payment_subscription_update_event_data import PaymentSubscriptionUpdateEventData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSubscriptionUpdateEventData from a JSON string
payment_subscription_update_event_data_instance = PaymentSubscriptionUpdateEventData.from_json(json)
# print the JSON string representation of the object
print(PaymentSubscriptionUpdateEventData.to_json())

# convert the object into a dict
payment_subscription_update_event_data_dict = payment_subscription_update_event_data_instance.to_dict()
# create an instance of PaymentSubscriptionUpdateEventData from a dict
payment_subscription_update_event_data_from_dict = PaymentSubscriptionUpdateEventData.from_dict(payment_subscription_update_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


