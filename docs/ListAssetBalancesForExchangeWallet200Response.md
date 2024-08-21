# ListAssetBalancesForExchangeWallet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SubWalletAssetBalance]**](SubWalletAssetBalance.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_asset_balances_for_exchange_wallet200_response import ListAssetBalancesForExchangeWallet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAssetBalancesForExchangeWallet200Response from a JSON string
list_asset_balances_for_exchange_wallet200_response_instance = ListAssetBalancesForExchangeWallet200Response.from_json(json)
# print the JSON string representation of the object
print(ListAssetBalancesForExchangeWallet200Response.to_json())

# convert the object into a dict
list_asset_balances_for_exchange_wallet200_response_dict = list_asset_balances_for_exchange_wallet200_response_instance.to_dict()
# create an instance of ListAssetBalancesForExchangeWallet200Response from a dict
list_asset_balances_for_exchange_wallet200_response_from_dict = ListAssetBalancesForExchangeWallet200Response.from_dict(list_asset_balances_for_exchange_wallet200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


