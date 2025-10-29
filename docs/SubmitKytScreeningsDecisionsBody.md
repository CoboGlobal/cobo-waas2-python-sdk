# SubmitKytScreeningsDecisionsBody

The KYT screening decision submission containing the transaction ID and the screening decision based on an external compliance review.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The UUID of the transaction for KYT result submission. This identifies the specific transaction that the external KYT result applies to. | 
**result** | [**KytScreeningsDecisionsType**](KytScreeningsDecisionsType.md) |  | 

## Example

```python
from cobo_waas2.models.submit_kyt_screenings_decisions_body import SubmitKytScreeningsDecisionsBody

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitKytScreeningsDecisionsBody from a JSON string
submit_kyt_screenings_decisions_body_instance = SubmitKytScreeningsDecisionsBody.from_json(json)
# print the JSON string representation of the object
print(SubmitKytScreeningsDecisionsBody.to_json())

# convert the object into a dict
submit_kyt_screenings_decisions_body_dict = submit_kyt_screenings_decisions_body_instance.to_dict()
# create an instance of SubmitKytScreeningsDecisionsBody from a dict
submit_kyt_screenings_decisions_body_from_dict = SubmitKytScreeningsDecisionsBody.from_dict(submit_kyt_screenings_decisions_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


