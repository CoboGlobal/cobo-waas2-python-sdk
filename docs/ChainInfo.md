# ChainInfo

The chain information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](/v2/api-references/wallets/list-enabled-chains). | 
**symbol** | **str** | The chain symbol, which is the abbreviated name of a chain. | [optional] 
**icon_url** | **str** | The URL of the chain icon. | [optional] 
**explorer_tx_url** | **str** | The transaction URL pattern on the blockchain explorer. You can use it to concatenate the transaction URLs. | [optional] 
**explorer_address_url** | **str** | The address URL pattern on the blockchain explorer. You can use it to concatenate the address URLs. | [optional] 
**require_memo** | **bool** | Whether the chain requires a memo. | [optional] 

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


