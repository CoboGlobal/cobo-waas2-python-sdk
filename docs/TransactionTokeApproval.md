# TransactionTokeApproval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](/v2/api-references/wallets/list-enabled-tokens). | 
**chain_id** | **str** | The ID of the chain on which the token operates. | 
**asset_id** | **str** | (This concept applies to Exchange Wallets only) The asset ID. An asset ID is the unique identifier of the asset held within your linked exchange account. | [optional] 
**symbol** | **str** | The token symbol, which is the abbreviated name of a token. | [optional] 
**name** | **str** | The token name, which is the full name of a token. | [optional] 
**decimal** | **int** | The token decimal. | [optional] 
**icon_url** | **str** | The URL of the token icon. | [optional] 
**token_address** | **str** | The token address, if applicable. | [optional] 
**fee_token_id** | **str** | The fee token ID. A fee token is the token with which you pay transaction fees. | [optional] 
**can_deposit** | **bool** | Whether deposits are enabled for this token. | [optional] 
**can_withdraw** | **bool** | Whether withdrawals are enabled for this token. | [optional] 
**amount** | **float** | Transaction value (Note that this is an absolute value. If you trade 1.5 BTC, then the value is 1.5)  | [optional] 
**spender** | **str** | Spender address | [optional] 

## Example

```python
from cobo_waas2.models.transaction_toke_approval import TransactionTokeApproval

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTokeApproval from a JSON string
transaction_toke_approval_instance = TransactionTokeApproval.from_json(json)
# print the JSON string representation of the object
print(TransactionTokeApproval.to_json())

# convert the object into a dict
transaction_toke_approval_dict = transaction_toke_approval_instance.to_dict()
# create an instance of TransactionTokeApproval from a dict
transaction_toke_approval_from_dict = TransactionTokeApproval.from_dict(transaction_toke_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


