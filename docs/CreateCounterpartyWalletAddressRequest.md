# CreateCounterpartyWalletAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_id** | **str** | The counterparty ID. | 
**address** | **str** | The wallet address. | 
**chain_id** | **str** | The chain ID of the cryptocurrency. | 

## Example

```python
from cobo_waas2.models.create_counterparty_wallet_address_request import CreateCounterpartyWalletAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCounterpartyWalletAddressRequest from a JSON string
create_counterparty_wallet_address_request_instance = CreateCounterpartyWalletAddressRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCounterpartyWalletAddressRequest.to_json())

# convert the object into a dict
create_counterparty_wallet_address_request_dict = create_counterparty_wallet_address_request_instance.to_dict()
# create an instance of CreateCounterpartyWalletAddressRequest from a dict
create_counterparty_wallet_address_request_from_dict = CreateCounterpartyWalletAddressRequest.from_dict(create_counterparty_wallet_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


