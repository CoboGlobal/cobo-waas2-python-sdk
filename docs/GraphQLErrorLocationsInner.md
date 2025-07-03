# GraphQLErrorLocationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | **int** | The line number in the query where the error occurred. | [optional] 
**column** | **int** | The column number in the query where the error occurred. | [optional] 

## Example

```python
from cobo_waas2.models.graph_ql_error_locations_inner import GraphQLErrorLocationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GraphQLErrorLocationsInner from a JSON string
graph_ql_error_locations_inner_instance = GraphQLErrorLocationsInner.from_json(json)
# print the JSON string representation of the object
print(GraphQLErrorLocationsInner.to_json())

# convert the object into a dict
graph_ql_error_locations_inner_dict = graph_ql_error_locations_inner_instance.to_dict()
# create an instance of GraphQLErrorLocationsInner from a dict
graph_ql_error_locations_inner_from_dict = GraphQLErrorLocationsInner.from_dict(graph_ql_error_locations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


