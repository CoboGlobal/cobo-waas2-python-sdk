# CancelPayoutBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_fee** | [**PayoutFeeData**](PayoutFeeData.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.cancel_payout_body import CancelPayoutBody

# TODO update the JSON string below
json = "{}"
# create an instance of CancelPayoutBody from a JSON string
cancel_payout_body_instance = CancelPayoutBody.from_json(json)
# print the JSON string representation of the object
print(CancelPayoutBody.to_json())

# convert the object into a dict
cancel_payout_body_dict = cancel_payout_body_instance.to_dict()
# create an instance of CancelPayoutBody from a dict
cancel_payout_body_from_dict = CancelPayoutBody.from_dict(cancel_payout_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


