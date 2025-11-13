# UpdateDestinationBankAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_alias** | **str** | The alias of the bank account. | 
**account_number** | **str** | The bank account number. | 
**swift_code** | **str** | The SWIFT or BIC code of the bank. | 
**currency** | **str** | The currency of the bank account. | 
**beneficiary_name** | **str** | The name of the account holder. | 
**beneficiary_address** | **str** | The address of the account holder. | 
**bank_name** | **str** | The name of the bank. | 
**bank_address** | **str** | The address of the bank. | 
**iban_code** | **str** | The IBAN code of the bank account. | [optional] 
**further_credit** | **str** | The further credit of the bank account. | [optional] 
**intermediary_bank_info** | [**IntermediaryBankInfo**](IntermediaryBankInfo.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.update_destination_bank_account import UpdateDestinationBankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDestinationBankAccount from a JSON string
update_destination_bank_account_instance = UpdateDestinationBankAccount.from_json(json)
# print the JSON string representation of the object
print(UpdateDestinationBankAccount.to_json())

# convert the object into a dict
update_destination_bank_account_dict = update_destination_bank_account_instance.to_dict()
# create an instance of UpdateDestinationBankAccount from a dict
update_destination_bank_account_from_dict = UpdateDestinationBankAccount.from_dict(update_destination_bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


