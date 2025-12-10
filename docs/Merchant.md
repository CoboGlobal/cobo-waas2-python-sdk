# Merchant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. | 
**name** | **str** | The merchant name. | 
**wallet_id** | **str** | The ID of the linked wallet. | 
**developer_fee_rate** | **str** | Developer fee rate for this token. For example, 0.01 represents a 1% fee.  | [optional] 
**subscription_developer_fee_rate** | **str** | The fee rate applied when subscribe the merchant account. Represented as a string percentage (e.g., \&quot;0.1\&quot; means 10%). | [optional] 
**wallet_setup** | [**WalletSetup**](WalletSetup.md) |  | [optional] 
**created_timestamp** | **int** | The created time of the merchant, represented as a UNIX timestamp in seconds. | [optional] 
**updated_timestamp** | **int** | The updated time of the merchant, represented as a UNIX timestamp in seconds. | [optional] 

## Example

```python
from cobo_waas2.models.merchant import Merchant

# TODO update the JSON string below
json = "{}"
# create an instance of Merchant from a JSON string
merchant_instance = Merchant.from_json(json)
# print the JSON string representation of the object
print(Merchant.to_json())

# convert the object into a dict
merchant_dict = merchant_instance.to_dict()
# create an instance of Merchant from a dict
merchant_from_dict = Merchant.from_dict(merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


