# PoolSummary

The summary of the staking pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique protocol id. | 
**chain_id** | **str** | The unique chain id. | 
**protocol** | **str** | The name of the protocol. | 
**protocol_icon_url** | **str** | The URL of the protocol&#39;s icon. | 
**supported_wallet_types** | [**List[WalletType]**](WalletType.md) | The list of available wallet types. | 
**supported_wallet_subtypes** | [**List[WalletSubtype]**](WalletSubtype.md) | The list of available wallet types. | 
**token_id** | **str** | The unique token id. | 
**est_apr** | **float** | The estimated APR. | 

## Example

```python
from cobo_waas2.models.pool_summary import PoolSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PoolSummary from a JSON string
pool_summary_instance = PoolSummary.from_json(json)
# print the JSON string representation of the object
print(PoolSummary.to_json())

# convert the object into a dict
pool_summary_dict = pool_summary_instance.to_dict()
# create an instance of PoolSummary from a dict
pool_summary_from_dict = PoolSummary.from_dict(pool_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


