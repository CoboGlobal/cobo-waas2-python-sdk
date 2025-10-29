# CreateMerchantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The merchant name. | 
**wallet_id** | **str** | This field has been deprecated. | [optional] 
**developer_fee_rate** | **str** | The developer fee rate applied to this merchant. Expressed as a string in decimal format where \&quot;0.1\&quot; represents 10%. For more information on developer fee rate, please refer to [Amounts and balances](https://www.cobo.com/developers/v2/payments/amounts-and-balances). | [optional] 
**wallet_setup** | [**WalletSetup**](WalletSetup.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_merchant_request import CreateMerchantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMerchantRequest from a JSON string
create_merchant_request_instance = CreateMerchantRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMerchantRequest.to_json())

# convert the object into a dict
create_merchant_request_dict = create_merchant_request_instance.to_dict()
# create an instance of CreateMerchantRequest from a dict
create_merchant_request_from_dict = CreateMerchantRequest.from_dict(create_merchant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


