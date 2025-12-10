# PayoutRbfBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_fee** | [**PayoutFeeData**](PayoutFeeData.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.payout_rbf_body import PayoutRbfBody

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutRbfBody from a JSON string
payout_rbf_body_instance = PayoutRbfBody.from_json(json)
# print the JSON string representation of the object
print(PayoutRbfBody.to_json())

# convert the object into a dict
payout_rbf_body_dict = payout_rbf_body_instance.to_dict()
# create an instance of PayoutRbfBody from a dict
payout_rbf_body_from_dict = PayoutRbfBody.from_dict(payout_rbf_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


