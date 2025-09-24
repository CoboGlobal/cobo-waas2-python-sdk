# BridgingFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_amount** | **str** | The bridging fee amount. | 
**received_token_id** | **str** | The received token id after bridge. | [optional] 
**received_amount** | **str** | The received amount after bridge. | [optional] 

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


