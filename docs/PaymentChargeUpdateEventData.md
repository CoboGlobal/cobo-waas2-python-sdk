# PaymentChargeUpdateEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The payment address update event data. - &#x60;PaymentPayout&#x60;: The payment payout event data. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The suspended token event data. - &#x60;ComplianceDisposition&#x60;: The compliance disposition event data. - &#x60;ComplianceKytScreenings&#x60;: The compliance KYT screenings event data. - &#x60;ComplianceKyaScreenings&#x60;: The compliance KYA screenings event data. | 
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

## Example

```python
from cobo_waas2.models.payment_charge_update_event_data import PaymentChargeUpdateEventData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentChargeUpdateEventData from a JSON string
payment_charge_update_event_data_instance = PaymentChargeUpdateEventData.from_json(json)
# print the JSON string representation of the object
print(PaymentChargeUpdateEventData.to_json())

# convert the object into a dict
payment_charge_update_event_data_dict = payment_charge_update_event_data_instance.to_dict()
# create an instance of PaymentChargeUpdateEventData from a dict
payment_charge_update_event_data_from_dict = PaymentChargeUpdateEventData.from_dict(payment_charge_update_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


