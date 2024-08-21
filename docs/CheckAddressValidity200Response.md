# CheckAddressValidity200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validity** | **bool** | Whether the address is valid. - &#x60;true&#x60;: The address is valid. - &#x60;false&#x60;: The address is invalid.  | 

## Example

```python
from cobo_waas2.models.check_address_validity200_response import CheckAddressValidity200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CheckAddressValidity200Response from a JSON string
check_address_validity200_response_instance = CheckAddressValidity200Response.from_json(json)
# print the JSON string representation of the object
print(CheckAddressValidity200Response.to_json())

# convert the object into a dict
check_address_validity200_response_dict = check_address_validity200_response_instance.to_dict()
# create an instance of CheckAddressValidity200Response from a dict
check_address_validity200_response_from_dict = CheckAddressValidity200Response.from_dict(check_address_validity200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


