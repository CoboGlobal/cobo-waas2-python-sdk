# CreateMpcProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The project name. | 
**participants** | **int** | The number of key share holders in the project.  **Notes:** 1. Currently, the available [Threshold Signature Schemes (TSS)](https://manuals.cobo.com/en/portal/mpc-wallets/introduction#threshold-signature-scheme-tss) are 2-2, 2-3, and 3-3 schemes (in the \&quot;threshold - participants\&quot; format), so you can only set &#x60;participants&#x60; to 2 or 3.   2. &#x60;threshold&#x60; must be less than or equal to &#x60;participants&#x60;.  | 
**threshold** | **int** | The number of key share holders required to sign an operation in the project.  **Notes:** 1. Currently, the available [Threshold Signature Schemes (TSS)](https://manuals.cobo.com/en/portal/mpc-wallets/introduction#threshold-signature-scheme-tss) are 2-2, 2-3, and 3-3 schemes (in the \&quot;threshold - participants\&quot; format), so you can only set &#x60;threshold&#x60; to 2 or 3.   2. &#x60;threshold&#x60; must be less than or equal to &#x60;participants&#x60;.  | 

## Example

```python
from cobo_waas2.models.create_mpc_project_request import CreateMpcProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMpcProjectRequest from a JSON string
create_mpc_project_request_instance = CreateMpcProjectRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMpcProjectRequest.to_json())

# convert the object into a dict
create_mpc_project_request_dict = create_mpc_project_request_instance.to_dict()
# create an instance of CreateMpcProjectRequest from a dict
create_mpc_project_request_from_dict = CreateMpcProjectRequest.from_dict(create_mpc_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


