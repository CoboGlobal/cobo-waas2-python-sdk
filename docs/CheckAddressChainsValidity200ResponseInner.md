# CheckAddressChainsValidity200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. | 
**validity** | **bool** | Whether the address is valid for the specified chain.  - &#x60;true&#x60;: The address is valid.  - &#x60;false&#x60;: The address is invalid.  | 

## Example

```python
from cobo_waas2.models.check_address_chains_validity200_response_inner import CheckAddressChainsValidity200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CheckAddressChainsValidity200ResponseInner from a JSON string
check_address_chains_validity200_response_inner_instance = CheckAddressChainsValidity200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(CheckAddressChainsValidity200ResponseInner.to_json())

# convert the object into a dict
check_address_chains_validity200_response_inner_dict = check_address_chains_validity200_response_inner_instance.to_dict()
# create an instance of CheckAddressChainsValidity200ResponseInner from a dict
check_address_chains_validity200_response_inner_from_dict = CheckAddressChainsValidity200ResponseInner.from_dict(check_address_chains_validity200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


