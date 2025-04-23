# CreateMerchantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The merchant name. | 
**wallet_id** | **str** | The ID of the wallet linked to the merchant. | 

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


