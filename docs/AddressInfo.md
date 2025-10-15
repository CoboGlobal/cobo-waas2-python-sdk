# AddressInfo

The address information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The wallet address. | 
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | 
**memo** | **str** | The memo code. | [optional] 
**path** | **str** | The derivation path of the address. This property applies to MPC Wallets only. To learn the meaning of each level in the path, see [Path levels](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki#path-levels). | [optional] 
**encoding** | [**AddressEncoding**](AddressEncoding.md) |  | [optional] 
**pubkey** | **str** | The public key of the address. This property applies to MPC Wallets only. | [optional] 
**x_only_pubkey** | **str** | The 32-byte x-only public key in hexadecimal format after tweaking. | [optional] 
**root_pubkey** | **str** | The root public key of the address. This property applies to MPC Wallets only. | [optional] 
**taproot_script_tree_hash** | **str** | The information about the new address. | [optional] 
**taproot_internal_address** | **str** | The Taproot address before tweaking. | [optional] 
**stellar_trusted_token_ids** | **List[str]** | The list of token IDs for which this address has already established trustlines on the Stellar network. | [optional] 

## Example

```python
from cobo_waas2.models.address_info import AddressInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AddressInfo from a JSON string
address_info_instance = AddressInfo.from_json(json)
# print the JSON string representation of the object
print(AddressInfo.to_json())

# convert the object into a dict
address_info_dict = address_info_instance.to_dict()
# create an instance of AddressInfo from a dict
address_info_from_dict = AddressInfo.from_dict(address_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


