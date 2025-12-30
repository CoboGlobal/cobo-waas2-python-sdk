# MPCVaultEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The top-up address update event data. - &#x60;PaymentPayout&#x60;: The payment payout event data. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The token suspension event data. - &#x60;ComplianceDisposition&#x60;: The compliance disposition event data. - &#x60;ComplianceKytScreenings&#x60;: The compliance KYT screenings event data. - &#x60;ComplianceKyaScreenings&#x60;: The compliance KYA screenings event data. | 
**vault_id** | **str** | The vault ID. | [optional] 
**project_id** | **str** | The project ID. | [optional] 
**name** | **str** | The vault name. | [optional] 
**type** | [**MPCVaultType**](MPCVaultType.md) |  | [optional] 
**root_pubkeys** | [**List[RootPubkey]**](RootPubkey.md) |  | [optional] 
**created_timestamp** | **int** | The vault&#39;s creation time in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.mpc_vault_event_data import MPCVaultEventData

# TODO update the JSON string below
json = "{}"
# create an instance of MPCVaultEventData from a JSON string
mpc_vault_event_data_instance = MPCVaultEventData.from_json(json)
# print the JSON string representation of the object
print(MPCVaultEventData.to_json())

# convert the object into a dict
mpc_vault_event_data_dict = mpc_vault_event_data_instance.to_dict()
# create an instance of MPCVaultEventData from a dict
mpc_vault_event_data_from_dict = MPCVaultEventData.from_dict(mpc_vault_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


