# ApprovalUserDetail

Details about a user involved in a transaction approval workflow. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the user who approved the transaction. | [optional] 
**email** | **str** | Email of the user. | [optional] 
**pubkey** | **str** | Public key of the user. | [optional] 
**signature** | **str** | Signature produced by the user for this approval. | [optional] 
**statement_uuid** | **str** | UUID of the statement associated with this approval. | [optional] 
**result** | [**ApprovalResult**](ApprovalResult.md) |  | [optional] 
**approval_result_code** | **int** | Integer value representing the result of the approval. | [optional] 
**created_time** | **int** | Timestamp when the approval was created. | [optional] 
**template_version** | **str** | Version of the template used for the transaction approval. | [optional] 
**header_title** | **str** | Display title used in the transaction approval. | [optional] 
**is_for_sign** | **bool** | Indicates whether this approval requires signing: - &#x60;true&#x60;: The user must sign the transaction. - &#x60;false&#x60;: The user only needs to approve or reject without signing.  | [optional] 
**show_info** | **str** | Additional information to show for the transaction approval. | [optional] 
**language** | **str** | Language used for the transaction approval. | [optional] 
**message_version** | **str** | Version of the message format used for the transaction approval. | [optional] 
**message** | **str** | Message associated with the transaction approval. | [optional] 
**extra_message** | **str** | Any additional message or information related to the transaction approval. | [optional] 

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


