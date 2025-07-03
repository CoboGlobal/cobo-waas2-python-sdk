# GraphQLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** | The response data for the GraphQL operation. | [optional] 
**errors** | [**List[GraphQLError]**](GraphQLError.md) | Any errors that occurred during the GraphQL operation. | [optional] 

## Example

```python
from cobo_waas2.models.graph_ql_response import GraphQLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GraphQLResponse from a JSON string
graph_ql_response_instance = GraphQLResponse.from_json(json)
# print the JSON string representation of the object
print(GraphQLResponse.to_json())

# convert the object into a dict
graph_ql_response_dict = graph_ql_response_instance.to_dict()
# create an instance of GraphQLResponse from a dict
graph_ql_response_from_dict = GraphQLResponse.from_dict(graph_ql_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


