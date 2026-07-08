# CreateCustodialWalletParams

The information of Custodial Wallets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The wallet name. This field is required and cannot be empty. Letters, numbers, and spaces are supported (for example, &#x60;My WaaS 2.0 Wallet&#x60;).  &lt;Note&gt;Some special characters are not accepted. For example, the at sign (&#x60;@&#x60;) is rejected. If the name is empty or contains unsupported characters, the request fails with a &#x60;400 Bad Request&#x60; error.&lt;/Note&gt;  | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**enable_auto_sweep** | **bool** | Enable the auto-sweep feature for the wallet. This parameter only applies to MPC Wallets and Custodial Wallets (Web3 Wallets). | [optional] 

## Example

```python
from cobo_waas2.models.create_custodial_wallet_params import CreateCustodialWalletParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustodialWalletParams from a JSON string
create_custodial_wallet_params_instance = CreateCustodialWalletParams.from_json(json)
# print the JSON string representation of the object
print(CreateCustodialWalletParams.to_json())

# convert the object into a dict
create_custodial_wallet_params_dict = create_custodial_wallet_params_instance.to_dict()
# create an instance of CreateCustodialWalletParams from a dict
create_custodial_wallet_params_from_dict = CreateCustodialWalletParams.from_dict(create_custodial_wallet_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


