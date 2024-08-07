# CreateKeyShareHolderGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_share_holder_group_type** | [**KeyShareHolderGroupType**](KeyShareHolderGroupType.md) |  | 
**participants** | **int** | The number of key share holders in this key share holder group.  **Notes:** 1. Currently, the available [Threshold Signature Schemes (TSS)](https://manuals.cobo.com/en/portal/mpc-wallets/introduction#threshold-signature-scheme-tss) are 2-2, 2-3, and 3-3 schemes (in the \&quot;threshold - participants\&quot; format), so you can only set &#x60;participants&#x60; to 2 or 3.   2. &#x60;threshold&#x60; must be less than or equal to &#x60;participants&#x60;.  | 
**threshold** | **int** | The number of key share holders required to sign an operation.  **Notes:** 1. Currently, the available [Threshold Signature Schemes (TSS)](https://manuals.cobo.com/en/portal/mpc-wallets/introduction#threshold-signature-scheme-tss) are 2-2, 2-3, and 3-3 schemes (in the \&quot;threshold - participants\&quot; format), so you can only set &#x60;threshold&#x60; to 2 or 3.   2. &#x60;threshold&#x60; must be less than or equal to &#x60;participants&#x60;.  | 
**key_share_holders** | [**List[CreateKeyShareHolder]**](CreateKeyShareHolder.md) |  | 

## Example

```python
from cobo_waas2.models.create_key_share_holder_group_request import CreateKeyShareHolderGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKeyShareHolderGroupRequest from a JSON string
create_key_share_holder_group_request_instance = CreateKeyShareHolderGroupRequest.from_json(json)
# print the JSON string representation of the object
print(CreateKeyShareHolderGroupRequest.to_json())

# convert the object into a dict
create_key_share_holder_group_request_dict = create_key_share_holder_group_request_instance.to_dict()
# create an instance of CreateKeyShareHolderGroupRequest from a dict
create_key_share_holder_group_request_from_dict = CreateKeyShareHolderGroupRequest.from_dict(create_key_share_holder_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


