# TokenBalanceBalance

The balance details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** | The total balance, which is the sum of the available, pending, and locked balances. | 
**available** | **str** | The balance free to use. | 
**pending** | **str** | The balance that is currently pending confirmation. | [optional] [default to '0']
**locked** | **str** | The balance that is currently not accessible to transactions. | [optional] [default to '0']

## Example

```python
from cobo_waas2.models.token_balance_balance import TokenBalanceBalance

# TODO update the JSON string below
json = "{}"
# create an instance of TokenBalanceBalance from a JSON string
token_balance_balance_instance = TokenBalanceBalance.from_json(json)
# print the JSON string representation of the object
print(TokenBalanceBalance.to_json())

# convert the object into a dict
token_balance_balance_dict = token_balance_balance_instance.to_dict()
# create an instance of TokenBalanceBalance from a dict
token_balance_balance_from_dict = TokenBalanceBalance.from_dict(token_balance_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


