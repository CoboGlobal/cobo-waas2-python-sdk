# KyaRiskDetail

Individual risk category assessment detail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The risk category (e.g., sanctions, fraud, theft, etc.). | 
**exposure** | **str** | The exposure level for this risk category (e.g., high, medium, low, none, indirect). | 

## Example

```python
from cobo_waas2.models.kya_risk_detail import KyaRiskDetail

# TODO update the JSON string below
json = "{}"
# create an instance of KyaRiskDetail from a JSON string
kya_risk_detail_instance = KyaRiskDetail.from_json(json)
# print the JSON string representation of the object
print(KyaRiskDetail.to_json())

# convert the object into a dict
kya_risk_detail_dict = kya_risk_detail_instance.to_dict()
# create an instance of KyaRiskDetail from a dict
kya_risk_detail_from_dict = KyaRiskDetail.from_dict(kya_risk_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


