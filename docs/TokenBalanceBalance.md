# TokenBalanceBalance

The balance details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** | The current amount of tokens in an address, which is retrieved directly from the network. To learn more, see [Balances and transaction amounts for MPC Wallets](https://www.cobo.com/developers/v2/guides/mpc-wallets/balance-amounts) for more details. | 
**available** | **str** | The amount of tokens ready to be spent. To learn more, see [Balances and transaction amounts for MPC Wallets](https://www.cobo.com/developers/v2/guides/mpc-wallets/balance-amounts) for more details. | 
**pending** | **str** | The total amount being sent in a transaction, which is calculated as the withdrawal amount plus the transaction fee. To learn more, see [Balances and transaction amounts for MPC Wallets](https://www.cobo.com/developers/v2/guides/mpc-wallets/balance-amounts) for more details. | [optional] [default to '0']
**locked** | **str** | For UTXO chains, this is the combined value of the selected UTXOs for the transaction. For other chains, it is equal to the Pending amount. To learn more, see [Balances and transaction amounts for MPC Wallets](https://www.cobo.com/developers/v2/guides/mpc-wallets/balance-amounts) for more details. | [optional] [default to '0']

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


