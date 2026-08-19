# BalanceAtBlock

The balance of an address at a specific block.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The wallet address. | [optional] 
**token_id** | **str** | The token ID, which is the unique identifier of a token. | [optional] 
**balance** | **str** | The token balance of the address. | [optional] 
**block_number** | **int** | The block number (block height) at which the balance was retrieved. | [optional] 

## Example

```python
from cobo_waas2.models.balance_at_block import BalanceAtBlock

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceAtBlock from a JSON string
balance_at_block_instance = BalanceAtBlock.from_json(json)
# print the JSON string representation of the object
print(BalanceAtBlock.to_json())

# convert the object into a dict
balance_at_block_dict = balance_at_block_instance.to_dict()
# create an instance of BalanceAtBlock from a dict
balance_at_block_from_dict = BalanceAtBlock.from_dict(balance_at_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


