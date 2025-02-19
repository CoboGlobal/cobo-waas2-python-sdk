# QueryGuardPubkey200ResponseAddressesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The wallet address. | 
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](/v2/api-references/wallets/list-enabled-chains). | 

## Example

```python
from cobo_waas2.models.query_guard_pubkey200_response_addresses_inner import QueryGuardPubkey200ResponseAddressesInner

# TODO update the JSON string below
json = "{}"
# create an instance of QueryGuardPubkey200ResponseAddressesInner from a JSON string
query_guard_pubkey200_response_addresses_inner_instance = QueryGuardPubkey200ResponseAddressesInner.from_json(json)
# print the JSON string representation of the object
print(QueryGuardPubkey200ResponseAddressesInner.to_json())

# convert the object into a dict
query_guard_pubkey200_response_addresses_inner_dict = query_guard_pubkey200_response_addresses_inner_instance.to_dict()
# create an instance of QueryGuardPubkey200ResponseAddressesInner from a dict
query_guard_pubkey200_response_addresses_inner_from_dict = QueryGuardPubkey200ResponseAddressesInner.from_dict(query_guard_pubkey200_response_addresses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


