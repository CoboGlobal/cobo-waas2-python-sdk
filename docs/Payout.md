# Payout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_id** | **str** | The payout ID. | 
**source** | [**PayoutSource**](PayoutSource.md) |  | [optional] 
**destination_count** | **int** | The destination count. | 
**token_id** | **str** | The token ID. | 
**total_amount** | **str** | The total amount. | 
**status** | [**PayoutStatus**](PayoutStatus.md) |  | 
**description** | **str** | The description. | [optional] 
**created_timestamp** | **int** | The created time of the payout, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.payout import Payout

# TODO update the JSON string below
json = "{}"
# create an instance of Payout from a JSON string
payout_instance = Payout.from_json(json)
# print the JSON string representation of the object
print(Payout.to_json())

# convert the object into a dict
payout_dict = payout_instance.to_dict()
# create an instance of Payout from a dict
payout_from_dict = Payout.from_dict(payout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


