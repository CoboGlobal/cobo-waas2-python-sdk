# UpdateDestinationBankAccount

The bank account details for updating a destination bank account.  For USD company bank accounts, optional prefixed fields may be required depending on `payment_method`: - When `payment_method` is `Swift`, `beneficiary_province` and `beneficiary_post_code` are required. - When `payment_method` is `Local` (HK only), `bank_branch_code` is required. 

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
**country** | **str** | The country, in ISO 3166-1 alpha-3 format. | [optional] 
**city** | **str** | Beneficiary&#39;s city. | [optional] 
**payment_method** | [**BankAccountPaymentMethod**](BankAccountPaymentMethod.md) |  | [optional] 
**holder_type** | [**BankAccountHolderType**](BankAccountHolderType.md) |  | [optional] 
**beneficiary_province** | **str** | The province or state of the beneficiary. Required when &#x60;payment_method&#x60; is &#x60;Swift&#x60;. Cannot be a pure number or contain Chinese characters.  | [optional] 
**beneficiary_post_code** | **str** | The postal code of the beneficiary. Required when &#x60;payment_method&#x60; is &#x60;Swift&#x60;.  | [optional] 
**bank_account_name** | **str** | The bank account name. Cannot contain Chinese characters.  | [optional] 
**bank_branch_code** | **str** | The branch code. Required when &#x60;payment_method&#x60; is &#x60;Local&#x60; (HK only).  | [optional] 
**bank_country** | **str** | The country, in ISO 3166-1 alpha-3 format. | [optional] 
**bank_province** | **str** | The province or state of the bank. Cannot be a pure number or contain Chinese characters.  | [optional] 
**contract_file_id** | **str** | The file ID of the contract document (e.g., cooperation agreement) that proves the business relationship between you and the beneficiary, which you can retrieve by calling [Upload file](https://www.cobo.com/developers/v2/api-references/payment/upload-file).  | [optional] 

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


