# QueryApprovalStatement200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | approval statement id. | [optional] 
**user_id** | **str** | approver user id. | [optional] 
**pubkey** | **str** | approver user pubkey. | [optional] 
**status** | [**ApprovalStatementStatus**](ApprovalStatementStatus.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.query_approval_statement200_response import QueryApprovalStatement200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QueryApprovalStatement200Response from a JSON string
query_approval_statement200_response_instance = QueryApprovalStatement200Response.from_json(json)
# print the JSON string representation of the object
print(QueryApprovalStatement200Response.to_json())

# convert the object into a dict
query_approval_statement200_response_dict = query_approval_statement200_response_instance.to_dict()
# create an instance of QueryApprovalStatement200Response from a dict
query_approval_statement200_response_from_dict = QueryApprovalStatement200Response.from_dict(query_approval_statement200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


