# CreateKyaScreeningsBody

Request body for batch creating address screening requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screenings** | [**List[KyaScreeningRequest]**](KyaScreeningRequest.md) | List of address screening requests. Maximum 50 addresses per request. | 

## Example

```python
from cobo_waas2.models.create_kya_screenings_body import CreateKyaScreeningsBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKyaScreeningsBody from a JSON string
create_kya_screenings_body_instance = CreateKyaScreeningsBody.from_json(json)
# print the JSON string representation of the object
print(CreateKyaScreeningsBody.to_json())

# convert the object into a dict
create_kya_screenings_body_dict = create_kya_screenings_body_instance.to_dict()
# create an instance of CreateKyaScreeningsBody from a dict
create_kya_screenings_body_from_dict = CreateKyaScreeningsBody.from_dict(create_kya_screenings_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


