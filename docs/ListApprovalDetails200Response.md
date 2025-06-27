# ListApprovalDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApprovalDetail]**](ApprovalDetail.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_approval_details200_response import ListApprovalDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListApprovalDetails200Response from a JSON string
list_approval_details200_response_instance = ListApprovalDetails200Response.from_json(json)
# print the JSON string representation of the object
print(ListApprovalDetails200Response.to_json())

# convert the object into a dict
list_approval_details200_response_dict = list_approval_details200_response_instance.to_dict()
# create an instance of ListApprovalDetails200Response from a dict
list_approval_details200_response_from_dict = ListApprovalDetails200Response.from_dict(list_approval_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


