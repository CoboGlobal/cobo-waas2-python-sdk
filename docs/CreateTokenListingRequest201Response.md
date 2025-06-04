# CreateTokenListingRequest201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Unique identifier for the token listing request | 

## Example

```python
from cobo_waas2.models.create_token_listing_request201_response import CreateTokenListingRequest201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTokenListingRequest201Response from a JSON string
create_token_listing_request201_response_instance = CreateTokenListingRequest201Response.from_json(json)
# print the JSON string representation of the object
print(CreateTokenListingRequest201Response.to_json())

# convert the object into a dict
create_token_listing_request201_response_dict = create_token_listing_request201_response_instance.to_dict()
# create an instance of CreateTokenListingRequest201Response from a dict
create_token_listing_request201_response_from_dict = CreateTokenListingRequest201Response.from_dict(create_token_listing_request201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


