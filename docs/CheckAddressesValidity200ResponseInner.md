# CheckAddressesValidity200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The wallet address. | 
**validity** | **bool** | Whether the address is valid.  - &#x60;true&#x60;: The address is valid.  - &#x60;false&#x60;: The address is invalid.  | 

## Example

```python
from cobo_waas2.models.check_addresses_validity200_response_inner import CheckAddressesValidity200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CheckAddressesValidity200ResponseInner from a JSON string
check_addresses_validity200_response_inner_instance = CheckAddressesValidity200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(CheckAddressesValidity200ResponseInner.to_json())

# convert the object into a dict
check_addresses_validity200_response_inner_dict = check_addresses_validity200_response_inner_instance.to_dict()
# create an instance of CheckAddressesValidity200ResponseInner from a dict
check_addresses_validity200_response_inner_from_dict = CheckAddressesValidity200ResponseInner.from_dict(check_addresses_validity200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


