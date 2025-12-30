# RefundLinkBusinessInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The transaction ID of the original order payment or top-up.  On the refund page, the from address of this transaction will be pre-filled as the default refund address.  The refund will be processed in the same token and on the same blockchain as this transaction.  | 
**amount** | **str** | The amount to refund, denominated in the cryptocurrency of the original payment transaction. The amount must be a positive number and can have up to two decimal places. | 
**refund_source** | [**RefundType**](RefundType.md) |  | 
**merchant_id** | **str** | The merchant ID, required if &#x60;refund_source&#x60; is &#x60;Merchant&#x60;. The fund will be deducted from the specified merchant&#39;s balance. | [optional] 
**fee_amount** | **str** | The developer fee amount to charge the merchant, denominated in the cryptocurrency of the original payment transaction. This field is only valid when &#x60;refund_source&#x60; is &#x60;Merchant&#x60;. For more information, please refer to [Accounts and fund allocation](https://www.cobo.com/payments/en/guides/amounts-and-balances). Must be:   - A positive integer with up to two decimal places.   - Less than the refund amount  | [optional] 

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


