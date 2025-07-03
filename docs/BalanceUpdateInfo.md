# BalanceUpdateInfo

The balance information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 
**address** | **str** | The wallet address. | 
**wallet_uuid** | **str** | The wallet ID. | 
**updated_timestamp** | **int** | The time when the balance updated, in Unix timestamp format, measured in milliseconds.  | 
**balance** | [**Balance**](Balance.md) |  | 

## Example

```python
from cobo_waas2.models.balance_update_info import BalanceUpdateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceUpdateInfo from a JSON string
balance_update_info_instance = BalanceUpdateInfo.from_json(json)
# print the JSON string representation of the object
print(BalanceUpdateInfo.to_json())

# convert the object into a dict
balance_update_info_dict = balance_update_info_instance.to_dict()
# create an instance of BalanceUpdateInfo from a dict
balance_update_info_from_dict = BalanceUpdateInfo.from_dict(balance_update_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


