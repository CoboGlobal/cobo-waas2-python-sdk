# ListKyaScreenings200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[KyaScreeningResult]**](KyaScreeningResult.md) |  | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from cobo_waas2.models.list_kya_screenings200_response import ListKyaScreenings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListKyaScreenings200Response from a JSON string
list_kya_screenings200_response_instance = ListKyaScreenings200Response.from_json(json)
# print the JSON string representation of the object
print(ListKyaScreenings200Response.to_json())

# convert the object into a dict
list_kya_screenings200_response_dict = list_kya_screenings200_response_instance.to_dict()
# create an instance of ListKyaScreenings200Response from a dict
list_kya_screenings200_response_from_dict = ListKyaScreenings200Response.from_dict(list_kya_screenings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


