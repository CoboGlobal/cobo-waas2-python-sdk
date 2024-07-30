# CustodialWalletInfo

The basic information of a wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The wallet ID. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**name** | **str** | The wallet name. | 
**org_id** | **str** | The ID of the owning organization. | 

## Example

```python
from cobo_waas2.models.custodial_wallet_info import CustodialWalletInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CustodialWalletInfo from a JSON string
custodial_wallet_info_instance = CustodialWalletInfo.from_json(json)
# print the JSON string representation of the object
print(CustodialWalletInfo.to_json())

# convert the object into a dict
custodial_wallet_info_dict = custodial_wallet_info_instance.to_dict()
# create an instance of CustodialWalletInfo from a dict
custodial_wallet_info_from_dict = CustodialWalletInfo.from_dict(custodial_wallet_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


