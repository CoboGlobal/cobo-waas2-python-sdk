# TransactionBabylonBusinessInfo

The extra information related to Babylon business logic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_type** | [**TransactionExtraType**](TransactionExtraType.md) |  | 
**babylon_address_info** | [**AddressInfo**](AddressInfo.md) |  | [optional] 
**btc_address_info** | [**AddressInfo**](AddressInfo.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.transaction_babylon_business_info import TransactionBabylonBusinessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionBabylonBusinessInfo from a JSON string
transaction_babylon_business_info_instance = TransactionBabylonBusinessInfo.from_json(json)
# print the JSON string representation of the object
print(TransactionBabylonBusinessInfo.to_json())

# convert the object into a dict
transaction_babylon_business_info_dict = transaction_babylon_business_info_instance.to_dict()
# create an instance of TransactionBabylonBusinessInfo from a dict
transaction_babylon_business_info_from_dict = TransactionBabylonBusinessInfo.from_dict(transaction_babylon_business_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


