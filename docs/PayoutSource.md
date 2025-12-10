# PayoutSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The source address. | [optional] 

## Example

```python
from cobo_waas2.models.payout_source import PayoutSource

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutSource from a JSON string
payout_source_instance = PayoutSource.from_json(json)
# print the JSON string representation of the object
print(PayoutSource.to_json())

# convert the object into a dict
payout_source_dict = payout_source_instance.to_dict()
# create an instance of PayoutSource from a dict
payout_source_from_dict = PayoutSource.from_dict(payout_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


