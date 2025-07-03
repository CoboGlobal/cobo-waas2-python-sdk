# PayerAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. | 
**payer_id** | **str** | A unique identifier assigned by Cobo to track and identify individual payers. | 
**developer_fee_rate** | **str** | The developer fee rate applied to the top-up transactions made by the payer. Expressed as a decimal string where \&quot;0.1\&quot; represents 10%. | 
**created_timestamp** | **int** | The creation time of the payer, represented as a UNIX timestamp in seconds. | [optional] 
**updated_timestamp** | **int** | The last update time of the payer, represented as a UNIX timestamp in seconds. | [optional] 
**accounts** | [**List[Account]**](Account.md) | An array of accounts associated with this payer. | [optional] 

## Example

```python
from cobo_waas2.models.payer_account import PayerAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PayerAccount from a JSON string
payer_account_instance = PayerAccount.from_json(json)
# print the JSON string representation of the object
print(PayerAccount.to_json())

# convert the object into a dict
payer_account_dict = payer_account_instance.to_dict()
# create an instance of PayerAccount from a dict
payer_account_from_dict = PayerAccount.from_dict(payer_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


