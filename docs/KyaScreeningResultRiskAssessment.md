# KyaScreeningResultRiskAssessment

Risk assessment information. Only present when status is 'Screened'. Null for other statuses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | [**KyaRiskLevel**](KyaRiskLevel.md) |  | 
**summary** | **str** | A brief summary of the risk assessment. | [optional] 
**details** | [**List[KyaRiskDetail]**](KyaRiskDetail.md) | Detailed risk category assessments. | [optional] 

## Example

```python
from cobo_waas2.models.kya_screening_result_risk_assessment import KyaScreeningResultRiskAssessment

# TODO update the JSON string below
json = "{}"
# create an instance of KyaScreeningResultRiskAssessment from a JSON string
kya_screening_result_risk_assessment_instance = KyaScreeningResultRiskAssessment.from_json(json)
# print the JSON string representation of the object
print(KyaScreeningResultRiskAssessment.to_json())

# convert the object into a dict
kya_screening_result_risk_assessment_dict = kya_screening_result_risk_assessment_instance.to_dict()
# create an instance of KyaScreeningResultRiskAssessment from a dict
kya_screening_result_risk_assessment_from_dict = KyaScreeningResultRiskAssessment.from_dict(kya_screening_result_risk_assessment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


