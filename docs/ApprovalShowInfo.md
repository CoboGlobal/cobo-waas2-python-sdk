# ApprovalShowInfo

Extra information for transaction approval details. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_name** | **str** | The name of the organization that the transaction belongs to. | [optional] 
**wallet_name** | **str** | The name of the wallet that the transaction belongs to. | [optional] 
**environment** | **str** | The environment in which the transaction is processed. | [optional] 
**from_address_label** | **str** | The label of the address from which the transaction is initiated. | [optional] 
**to_address_label** | **str** | The label of the address to which the transaction is sent. | [optional] 

## Example

```python
from cobo_waas2.models.approval_show_info import ApprovalShowInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalShowInfo from a JSON string
approval_show_info_instance = ApprovalShowInfo.from_json(json)
# print the JSON string representation of the object
print(ApprovalShowInfo.to_json())

# convert the object into a dict
approval_show_info_dict = approval_show_info_instance.to_dict()
# create an instance of ApprovalShowInfo from a dict
approval_show_info_from_dict = ApprovalShowInfo.from_dict(approval_show_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


