# KyaScreeningResult

Complete address screening result including risk assessment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The idempotency identifier from the request, unique within your organization, used for tracking and troubleshooting. Only present in create response. | 
**screening_id** | **str** | The unique system-generated identifier for this screening request (UUID format, fixed 36 characters). | 
**address** | **str** | The screened blockchain address. | 
**chain_id** | **str** | The chain identifier. | 
**note** | **str** | Optional note for this address screening. | [optional] 
**created_timestamp** | **int** | The time when the screening request was created, in Unix timestamp format, measured in milliseconds. | 
**requested_by** | **str** | The identifier of the user or application that created this screening request. | 
**status** | [**KyaScreeningStatus**](KyaScreeningStatus.md) |  | 
**risk_assessment** | [**KyaScreeningResultRiskAssessment**](KyaScreeningResultRiskAssessment.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.kya_screening_result import KyaScreeningResult

# TODO update the JSON string below
json = "{}"
# create an instance of KyaScreeningResult from a JSON string
kya_screening_result_instance = KyaScreeningResult.from_json(json)
# print the JSON string representation of the object
print(KyaScreeningResult.to_json())

# convert the object into a dict
kya_screening_result_dict = kya_screening_result_instance.to_dict()
# create an instance of KyaScreeningResult from a dict
kya_screening_result_from_dict = KyaScreeningResult.from_dict(kya_screening_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


