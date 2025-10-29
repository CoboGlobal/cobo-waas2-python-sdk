# BridgingFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_amount** | **str** | The fee charged for bridging tokens to another blockchain during an off-ramp operation. Bridging fees apply when tokens are on a blockchain not directly supported by the off-ramp service.  | 
**received_token_id** | **str** | The ID of the destination token received after bridging. | [optional] 
**received_amount** | **str** | The final amount of destination tokens received after bridging. | [optional] 

## Example

```python
from cobo_waas2.models.bridging_fee import BridgingFee

# TODO update the JSON string below
json = "{}"
# create an instance of BridgingFee from a JSON string
bridging_fee_instance = BridgingFee.from_json(json)
# print the JSON string representation of the object
print(BridgingFee.to_json())

# convert the object into a dict
bridging_fee_dict = bridging_fee_instance.to_dict()
# create an instance of BridgingFee from a dict
bridging_fee_from_dict = BridgingFee.from_dict(bridging_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


