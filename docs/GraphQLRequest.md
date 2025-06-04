# GraphQLRequest

The request body for a GraphQL query or mutation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The GraphQL query or mutation as a string. | 
**variables** | **Dict[str, object]** | Variables to use in the GraphQL operation. Can include dynamic values required for the query or mutation. | [optional] 
**operation_name** | **str** | The operation name in case of multiple operations in the same query or mutation. | [optional] 

## Example

```python
from cobo_waas2.models.graph_ql_request import GraphQLRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GraphQLRequest from a JSON string
graph_ql_request_instance = GraphQLRequest.from_json(json)
# print the JSON string representation of the object
print(GraphQLRequest.to_json())

# convert the object into a dict
graph_ql_request_dict = graph_ql_request_instance.to_dict()
# create an instance of GraphQLRequest from a dict
graph_ql_request_from_dict = GraphQLRequest.from_dict(graph_ql_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


