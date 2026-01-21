# CreateBulkSendRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_account** | **str** | The source account from which the bulk send will be made. - If the source account is a merchant account, provide the merchant&#39;s ID (e.g., \&quot;M1001\&quot;). - If the source account is the developer account, use the string &#x60;\&quot;developer\&quot;&#x60;.  | 
**execution_mode** | [**PaymentBulkSendExecutionMode**](PaymentBulkSendExecutionMode.md) |  | 
**description** | **str** | The description for the entire bulk send batch. | [optional] 
**payout_params** | [**List[CreateBulkSendRequestPayoutParamsInner]**](CreateBulkSendRequestPayoutParamsInner.md) | The bulk send items. | 

## Example

```python
from cobo_waas2.models.create_bulk_send_request import CreateBulkSendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBulkSendRequest from a JSON string
create_bulk_send_request_instance = CreateBulkSendRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBulkSendRequest.to_json())

# convert the object into a dict
create_bulk_send_request_dict = create_bulk_send_request_instance.to_dict()
# create an instance of CreateBulkSendRequest from a dict
create_bulk_send_request_from_dict = CreateBulkSendRequest.from_dict(create_bulk_send_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


