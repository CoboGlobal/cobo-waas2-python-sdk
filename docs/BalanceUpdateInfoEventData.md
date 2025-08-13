# BalanceUpdateInfoEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The top-up address update event data. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The token suspension event data. | 
**token_id** | **str** | The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 
**address** | **str** | The wallet address. | 
**wallet_uuid** | **str** | The wallet ID. | 
**updated_timestamp** | **int** | The time when the balance updated, in Unix timestamp format, measured in milliseconds.  | 
**balance** | [**Balance**](Balance.md) |  | 

## Example

```python
from cobo_waas2.models.balance_update_info_event_data import BalanceUpdateInfoEventData

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceUpdateInfoEventData from a JSON string
balance_update_info_event_data_instance = BalanceUpdateInfoEventData.from_json(json)
# print the JSON string representation of the object
print(BalanceUpdateInfoEventData.to_json())

# convert the object into a dict
balance_update_info_event_data_dict = balance_update_info_event_data_instance.to_dict()
# create an instance of BalanceUpdateInfoEventData from a dict
balance_update_info_event_data_from_dict = BalanceUpdateInfoEventData.from_dict(balance_update_info_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


