# ListSupportedCountries200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**en** | **str** | The English name of the country. | 
**zh_hans** | **str** | The simplified Chinese name of the country. | 
**code2** | **str** | The 2-letter country code (ISO 3166-1 alpha-2). | 

## Example

```python
from cobo_waas2.models.list_supported_countries200_response_inner import ListSupportedCountries200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListSupportedCountries200ResponseInner from a JSON string
list_supported_countries200_response_inner_instance = ListSupportedCountries200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListSupportedCountries200ResponseInner.to_json())

# convert the object into a dict
list_supported_countries200_response_inner_dict = list_supported_countries200_response_inner_instance.to_dict()
# create an instance of ListSupportedCountries200ResponseInner from a dict
list_supported_countries200_response_inner_from_dict = ListSupportedCountries200ResponseInner.from_dict(list_supported_countries200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


