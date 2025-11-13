# RefundLinkBusinessInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The transaction ID. | 
**amount** | **str** | The amount to refund in cryptocurrency. | 
**refund_source** | [**RefundType**](RefundType.md) |  | 
**merchant_id** | **str** | The merchant ID, required if the refund amount source is &#x60;Merchant&#x60;. | [optional] 
**fee_amount** | **str** | The amount of the transaction fee that the merchant will bear for the refund.  | [optional] 

## Example

```python
from cobo_waas2.models.refund_link_business_info import RefundLinkBusinessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RefundLinkBusinessInfo from a JSON string
refund_link_business_info_instance = RefundLinkBusinessInfo.from_json(json)
# print the JSON string representation of the object
print(RefundLinkBusinessInfo.to_json())

# convert the object into a dict
refund_link_business_info_dict = refund_link_business_info_instance.to_dict()
# create an instance of RefundLinkBusinessInfo from a dict
refund_link_business_info_from_dict = RefundLinkBusinessInfo.from_dict(refund_link_business_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


