# CreateBankAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, object]** | JSON-formatted bank account details. The object should include the following fields: - beneficiary_name: Name of the account holder - beneficiary_address: Address of the account holder - account_number: Bank account number - bank_name: Name of the bank - bank_address: Address of the bank - iban: (Optional) International Bank Account Number - swift_or_bic: SWIFT or BIC code of the bank  | 

## Example

```python
from cobo_waas2.models.create_bank_account_request import CreateBankAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBankAccountRequest from a JSON string
create_bank_account_request_instance = CreateBankAccountRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBankAccountRequest.to_json())

# convert the object into a dict
create_bank_account_request_dict = create_bank_account_request_instance.to_dict()
# create an instance of CreateBankAccountRequest from a dict
create_bank_account_request_from_dict = CreateBankAccountRequest.from_dict(create_bank_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


