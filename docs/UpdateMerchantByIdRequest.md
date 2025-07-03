# UpdateMerchantByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The merchant name. | [optional] 
**developer_fee_rate** | **str** | The developer fee rate applied to this merchant. Expressed as a string in decimal format where \&quot;0.1\&quot; represents 10%. This fee is deducted from the payment amount and only applies to top-up transactions. | [optional] 

## Example

```python
from cobo_waas2.models.update_merchant_by_id_request import UpdateMerchantByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMerchantByIdRequest from a JSON string
update_merchant_by_id_request_instance = UpdateMerchantByIdRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMerchantByIdRequest.to_json())

# convert the object into a dict
update_merchant_by_id_request_dict = update_merchant_by_id_request_instance.to_dict()
# create an instance of UpdateMerchantByIdRequest from a dict
update_merchant_by_id_request_from_dict = UpdateMerchantByIdRequest.from_dict(update_merchant_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


