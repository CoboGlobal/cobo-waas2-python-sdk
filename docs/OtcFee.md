# OtcFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_rate** | **str** | The exchange rate used to convert cryptos to fiat currencies during off-ramp. The final fiat amount is calculated using the following formula:  Final Fiat Amount &#x3D; (Token Amount - Bridging Fee) × Exchange Rate  Note: The actual fiat amount received may be lower due to additional bank transfer fees.  | 
**token_id** | **str** | The ID of the token you want to off-ramp. | [optional] 

## Example

```python
from cobo_waas2.models.otc_fee import OtcFee

# TODO update the JSON string below
json = "{}"
# create an instance of OtcFee from a JSON string
otc_fee_instance = OtcFee.from_json(json)
# print the JSON string representation of the object
print(OtcFee.to_json())

# convert the object into a dict
otc_fee_dict = otc_fee_instance.to_dict()
# create an instance of OtcFee from a dict
otc_fee_from_dict = OtcFee.from_dict(otc_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


