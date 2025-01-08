# Pagination

The pagination information of the returned data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before** | **str** | An object ID used to retrieve records before the specified object, indicating earlier or smaller records relative to the current dataset. You can use it to paginate backwards.   If empty, it means you have reached the start of the data.    Most API endpoints sort by object ID, but some use other fields depending on the endpoint.  | 
**after** | **str** | An object ID used to retrieve records after the specified object, indicating newer or larger records relative to the current dataset. You can use it to paginate forwards.    If empty, it means you have reached the end of the data.    Most API endpoints sort by object ID, but some use other fields depending on the endpoint.  | 
**total_count** | **int** | The total number of records that match the query criteria, unaffected by the pagination parameters (&#x60;before&#x60; , &#x60;after&#x60;, and &#x60;limit&#x60;). | 

## Example

```python
from cobo_waas2.models.pagination import Pagination

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination from a JSON string
pagination_instance = Pagination.from_json(json)
# print the JSON string representation of the object
print(Pagination.to_json())

# convert the object into a dict
pagination_dict = pagination_instance.to_dict()
# create an instance of Pagination from a dict
pagination_from_dict = Pagination.from_dict(pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


