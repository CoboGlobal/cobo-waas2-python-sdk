# AddressesEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The payment address update event data. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The suspended token event data. - &#x60;ComplianceDisposition&#x60;: The compliance disposition event data. - &#x60;ComplianceKytScreenings&#x60;: The compliance KYT screenings event data. | 
**addresses** | [**List[AddressesEventDataAllOfAddresses]**](AddressesEventDataAllOfAddresses.md) | A list of addresses. | [optional] 

## Example

```python
from cobo_waas2.models.addresses_event_data import AddressesEventData

# TODO update the JSON string below
json = "{}"
# create an instance of AddressesEventData from a JSON string
addresses_event_data_instance = AddressesEventData.from_json(json)
# print the JSON string representation of the object
print(AddressesEventData.to_json())

# convert the object into a dict
addresses_event_data_dict = addresses_event_data_instance.to_dict()
# create an instance of AddressesEventData from a dict
addresses_event_data_from_dict = AddressesEventData.from_dict(addresses_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


