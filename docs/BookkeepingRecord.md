# BookkeepingRecord

The bookkeeping item information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The wallet ID. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | [optional] 
**wallet_name** | **str** | The wallet name. | [optional] 
**transaction_timestamp** | **int** | The time when the bookkeeping was created, in Unix timestamp format, measured in milliseconds. | 
**token_id** | **str** | The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](/v2/api-references/wallets/list-enabled-tokens). | 
**type** | **str** | The bookkeeping type. | 
**amount** | **str** | The amount of the bookkeeping. | 
**balance** | **str** | The post-balance of the tx. | 
**from_address** | **str** | The from address. | [optional] 
**to_address** | **str** | The to address. | [optional] 
**transaction_hash** | **str** | The transaction hash. | [optional] 

## Example

```python
from cobo_waas2.models.bookkeeping_record import BookkeepingRecord

# TODO update the JSON string below
json = "{}"
# create an instance of BookkeepingRecord from a JSON string
bookkeeping_record_instance = BookkeepingRecord.from_json(json)
# print the JSON string representation of the object
print(BookkeepingRecord.to_json())

# convert the object into a dict
bookkeeping_record_dict = bookkeeping_record_instance.to_dict()
# create an instance of BookkeepingRecord from a dict
bookkeeping_record_from_dict = BookkeepingRecord.from_dict(bookkeeping_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


