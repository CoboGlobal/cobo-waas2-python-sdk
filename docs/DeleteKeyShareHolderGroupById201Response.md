# DeleteKeyShareHolderGroupById201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submitted** | **bool** | Whether the request to delete the key share holder group has been successfully submitted. - &#x60;true&#x60;: The request to delete the key share holder group has been successfully submitted. - &#x60;false&#x60;: The request to delete the key share holder group has not been submitted.  | 

## Example

```python
from cobo_waas2.models.delete_key_share_holder_group_by_id201_response import DeleteKeyShareHolderGroupById201Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteKeyShareHolderGroupById201Response from a JSON string
delete_key_share_holder_group_by_id201_response_instance = DeleteKeyShareHolderGroupById201Response.from_json(json)
# print the JSON string representation of the object
print(DeleteKeyShareHolderGroupById201Response.to_json())

# convert the object into a dict
delete_key_share_holder_group_by_id201_response_dict = delete_key_share_holder_group_by_id201_response_instance.to_dict()
# create an instance of DeleteKeyShareHolderGroupById201Response from a dict
delete_key_share_holder_group_by_id201_response_from_dict = DeleteKeyShareHolderGroupById201Response.from_dict(delete_key_share_holder_group_by_id201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


