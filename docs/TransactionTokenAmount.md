# TransactionTokenAmount

The data for transaction asset information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | [optional] 
**asset_id** | **str** | (This concept applies to Exchange Wallets only) The asset ID. An asset ID is the unique identifier of the asset held within your linked exchange account. | 
**amount** | **float** | Transaction value (Note that this is an absolute value. If you trade 1.5 BTC, then the value is 1.5)  | 

## Example

```python
from cobo_waas2.models.transaction_token_amount import TransactionTokenAmount

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTokenAmount from a JSON string
transaction_token_amount_instance = TransactionTokenAmount.from_json(json)
# print the JSON string representation of the object
print(TransactionTokenAmount.to_json())

# convert the object into a dict
transaction_token_amount_dict = transaction_token_amount_instance.to_dict()
# create an instance of TransactionTokenAmount from a dict
transaction_token_amount_from_dict = TransactionTokenAmount.from_dict(transaction_token_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


