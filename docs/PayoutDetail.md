# PayoutDetail


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
**updated_timestamp** | **int** | The updated time of the payout, represented as a UNIX timestamp in seconds. | [optional] 
**destinations** | [**List[PayoutDestinationDetail]**](PayoutDestinationDetail.md) | The destinations of the payout. | [optional] 

## Example

```python
from cobo_waas2.models.payout_detail import PayoutDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutDetail from a JSON string
payout_detail_instance = PayoutDetail.from_json(json)
# print the JSON string representation of the object
print(PayoutDetail.to_json())

# convert the object into a dict
payout_detail_dict = payout_detail_instance.to_dict()
# create an instance of PayoutDetail from a dict
payout_detail_from_dict = PayoutDetail.from_dict(payout_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


