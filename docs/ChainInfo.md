# ChainInfo

The chain information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. | 
**symbol** | **str** | The chain symbol for display purposes, which is the abbreviated name of a chain. | [optional] 
**icon_url** | **str** | The URL of the chain icon. | [optional] 
**chain_identifier** | **str** | A functional identifier used to group blockchains with similar execution logic. For example, &#x60;ETH&#x60; for all EVM-compatible chains (Ethereum, BNB Smart Chain, Polygon). | [optional] 
**explorer_tx_url** | **str** | The transaction URL pattern on the blockchain explorer. You can use it to concatenate the transaction URLs. | [optional] 
**explorer_address_url** | **str** | The address URL pattern on the blockchain explorer. You can use it to concatenate the address URLs. | [optional] 
**require_memo** | **bool** | Whether the chain requires a memo. | [optional] 
**confirming_threshold** | **int** | The number of confirmations required for an on-chain transaction, such as 64 for Ethereum. | [optional] 
**coinbase_maturity** | **int** | The number of confirmations required before a coinbase transaction is considered mature and can be spent, for example, 100 confirmations for BTC. | [optional] 

## Example

```python
from cobo_waas2.models.chain_info import ChainInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ChainInfo from a JSON string
chain_info_instance = ChainInfo.from_json(json)
# print the JSON string representation of the object
print(ChainInfo.to_json())

# convert the object into a dict
chain_info_dict = chain_info_instance.to_dict()
# create an instance of ChainInfo from a dict
chain_info_from_dict = ChainInfo.from_dict(chain_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


