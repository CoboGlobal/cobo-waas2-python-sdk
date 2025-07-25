# BankAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_account_id** | **str** | The bank account ID. | 
**info** | **Dict[str, object]** | JSON-formatted bank account details. | 
**created_timestamp** | **int** | The creation time of the bank account, represented as a UNIX timestamp in seconds. | [optional] 
**updated_timestamp** | **int** | The last update time of the bank account, represented as a UNIX timestamp in seconds. | [optional] 

## Example

```python
from cobo_waas2.models.bank_account import BankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccount from a JSON string
bank_account_instance = BankAccount.from_json(json)
# print the JSON string representation of the object
print(BankAccount.to_json())

# convert the object into a dict
bank_account_dict = bank_account_instance.to_dict()
# create an instance of BankAccount from a dict
bank_account_from_dict = BankAccount.from_dict(bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


