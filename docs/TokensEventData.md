# TokensEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The top-up address update event data. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The token suspension event data. - &#x60;ComplianceDisposition&#x60;: The compliance disposition event data. - &#x60;ComplianceKytScreenings&#x60;: The compliance KYT screenings event data. | 
**tokens** | [**List[TokenInfo]**](TokenInfo.md) | The enabled tokens. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | [optional] 
**wallet_subtypes** | [**List[WalletSubtype]**](WalletSubtype.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.tokens_event_data import TokensEventData

# TODO update the JSON string below
json = "{}"
# create an instance of TokensEventData from a JSON string
tokens_event_data_instance = TokensEventData.from_json(json)
# print the JSON string representation of the object
print(TokensEventData.to_json())

# convert the object into a dict
tokens_event_data_dict = tokens_event_data_instance.to_dict()
# create an instance of TokensEventData from a dict
tokens_event_data_from_dict = TokensEventData.from_dict(tokens_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


