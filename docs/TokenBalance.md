# TokenBalance

The balance information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](/v2/api-references/wallets/list-enabled-tokens). | 
**balance** | [**TokenBalanceBalance**](TokenBalanceBalance.md) |  | 

## Example

```python
from cobo_waas2.models.token_balance import TokenBalance

# TODO update the JSON string below
json = "{}"
# create an instance of TokenBalance from a JSON string
token_balance_instance = TokenBalance.from_json(json)
# print the JSON string representation of the object
print(TokenBalance.to_json())

# convert the object into a dict
token_balance_dict = token_balance_instance.to_dict()
# create an instance of TokenBalance from a dict
token_balance_from_dict = TokenBalance.from_dict(token_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


