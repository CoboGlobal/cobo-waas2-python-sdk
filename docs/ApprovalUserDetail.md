# ApprovalUserDetail

The user detail for a transaction approval. This includes the user's email, public key, signature, statement UUID, result of the approval, creation time, template version, header title, whether it is for signing, and additional information to show. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_email** | **str** | The email address of the user who approved the transaction. | [optional] 
**pubkey** | **str** | The public key of the user who approved the transaction. | [optional] 
**signature** | **str** | The signature of the transaction approval. | [optional] 
**statement_uuid** | **str** | The UUID of the statement associated with the transaction approval. | [optional] 
**result** | [**ApprovalResult**](ApprovalResult.md) |  | [optional] 
**created_time** | **int** | The timestamp when the approval was created. | [optional] 
**template_version** | **str** | The version of the template used for the transaction approval. | [optional] 
**header_title** | **str** | The title of the header for the transaction approval. | [optional] 
**is_for_sign** | **bool** | Indicates whether the approval is for signing. | [optional] 
**show_info** | [**ApprovalShowInfo**](ApprovalShowInfo.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.approval_user_detail import ApprovalUserDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalUserDetail from a JSON string
approval_user_detail_instance = ApprovalUserDetail.from_json(json)
# print the JSON string representation of the object
print(ApprovalUserDetail.to_json())

# convert the object into a dict
approval_user_detail_dict = approval_user_detail_instance.to_dict()
# create an instance of ApprovalUserDetail from a dict
approval_user_detail_from_dict = ApprovalUserDetail.from_dict(approval_user_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


