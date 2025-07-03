# GraphQLError

Details of an error in the GraphQL operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The error message. | [optional] 
**locations** | [**List[GraphQLErrorLocationsInner]**](GraphQLErrorLocationsInner.md) | The locations in the query where the error occurred. | [optional] 
**path** | **List[str]** | The path in the response where the error occurred. | [optional] 

## Example

```python
from cobo_waas2.models.graph_ql_error import GraphQLError

# TODO update the JSON string below
json = "{}"
# create an instance of GraphQLError from a JSON string
graph_ql_error_instance = GraphQLError.from_json(json)
# print the JSON string representation of the object
print(GraphQLError.to_json())

# convert the object into a dict
graph_ql_error_dict = graph_ql_error_instance.to_dict()
# create an instance of GraphQLError from a dict
graph_ql_error_from_dict = GraphQLError.from_dict(graph_ql_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


