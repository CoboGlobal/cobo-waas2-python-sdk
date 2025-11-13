# GetDestinationBankAccountDetailById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_id** | **str** | The destination ID. | 
**destination_name** | **str** | The name of the destination. | 
**destination_type** | [**DestinationType**](DestinationType.md) |  | 
**destination_email** | **str** | The email of the destination. | [optional] 
**destination_country** | **str** | The country of the destination, in ISO 3166-1 alpha-3 format. | [optional] 
**destination_contact_address** | **str** | The contact address of the destination. | [optional] 
**destination_merchant_id** | **str** | The ID of the merchant linked to the destination. | [optional] 
**bank_account_id** | **str** | The destination bank account ID. | 
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
**bank_account_status** | [**BankAccountStatus**](BankAccountStatus.md) |  | 
**created_timestamp** | **int** | The created time of the bank account, represented as a UNIX timestamp in seconds. | [optional] 
**updated_timestamp** | **int** | The updated time of the bank account, represented as a UNIX timestamp in seconds. | [optional] 

## Example

```python
from cobo_waas2.models.get_destination_bank_account_detail_by_id200_response import GetDestinationBankAccountDetailById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDestinationBankAccountDetailById200Response from a JSON string
get_destination_bank_account_detail_by_id200_response_instance = GetDestinationBankAccountDetailById200Response.from_json(json)
# print the JSON string representation of the object
print(GetDestinationBankAccountDetailById200Response.to_json())

# convert the object into a dict
get_destination_bank_account_detail_by_id200_response_dict = get_destination_bank_account_detail_by_id200_response_instance.to_dict()
# create an instance of GetDestinationBankAccountDetailById200Response from a dict
get_destination_bank_account_detail_by_id200_response_from_dict = GetDestinationBankAccountDetailById200Response.from_dict(get_destination_bank_account_detail_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


