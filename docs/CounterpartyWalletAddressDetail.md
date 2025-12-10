# CounterpartyWalletAddressDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_id** | **str** | The counterparty ID. | 
**counterparty_name** | **str** | The name of the counterparty. | 
**counterparty_type** | [**CounterpartyType**](CounterpartyType.md) |  | 
**wallet_address_id** | **str** | The wallet address ID. | 
**address** | **str** | The wallet address. | 
**chain_id** | **str** | The chain ID of the cryptocurrency. | 
**updated_timestamp** | **int** | The updated time of the wallet address, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.counterparty_wallet_address_detail import CounterpartyWalletAddressDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CounterpartyWalletAddressDetail from a JSON string
counterparty_wallet_address_detail_instance = CounterpartyWalletAddressDetail.from_json(json)
# print the JSON string representation of the object
print(CounterpartyWalletAddressDetail.to_json())

# convert the object into a dict
counterparty_wallet_address_detail_dict = counterparty_wallet_address_detail_instance.to_dict()
# create an instance of CounterpartyWalletAddressDetail from a dict
counterparty_wallet_address_detail_from_dict = CounterpartyWalletAddressDetail.from_dict(counterparty_wallet_address_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


