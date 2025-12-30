# KyaRiskAssessment

The risk assessment information for the screened address. Only returned when status is 'Screened'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | [**KyaRiskLevel**](KyaRiskLevel.md) |  | 
**summary** | **str** | A brief summary of the risk assessment. | [optional] 
**details** | [**List[KyaRiskDetail]**](KyaRiskDetail.md) | Detailed risk category assessments. | [optional] 

## Example

```python
from cobo_waas2.models.kya_risk_assessment import KyaRiskAssessment

# TODO update the JSON string below
json = "{}"
# create an instance of KyaRiskAssessment from a JSON string
kya_risk_assessment_instance = KyaRiskAssessment.from_json(json)
# print the JSON string representation of the object
print(KyaRiskAssessment.to_json())

# convert the object into a dict
kya_risk_assessment_dict = kya_risk_assessment_instance.to_dict()
# create an instance of KyaRiskAssessment from a dict
kya_risk_assessment_from_dict = KyaRiskAssessment.from_dict(kya_risk_assessment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


