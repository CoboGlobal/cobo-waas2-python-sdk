# Account

Details of a payment account used for top-up operations, including address and balance metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The ID of the cryptocurrency that this account is configured to handle. | 
**address** | **str** | The top-up address corresponding to the account. | 
**merchant_balance** | **str** | The amount of merchant funds under this account. | 
**psp_balance** | **str** | The amount of developer funds under this account. | 
**created_timestamp** | **int** | The creation time of the account, in Unix timestamp format, measured in milliseconds. | [optional] 
**updated_timestamp** | **int** | The last update time of the account, in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


