# PaymentBulkSend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_send_id** | **str** | The bulk send ID. | 
**source_account** | **str** | The source account from which the bulk send will be made. - If the source account is a merchant account, provide the merchant&#39;s ID (e.g., \&quot;M1001\&quot;). - If the source account is the developer account, use the string &#x60;\&quot;developer\&quot;&#x60;.  | 
**description** | **str** | The description for the entire bulk send batch. | [optional] 
**execution_mode** | [**PaymentBulkSendExecutionMode**](PaymentBulkSendExecutionMode.md) |  | 
**status** | [**PaymentBulkSendStatus**](PaymentBulkSendStatus.md) |  | 
**created_timestamp** | **int** | The created time of the bulk send, represented as a UNIX timestamp in seconds. | 
**updated_timestamp** | **int** | The updated time of the bulk send, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.payment_bulk_send import PaymentBulkSend

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBulkSend from a JSON string
payment_bulk_send_instance = PaymentBulkSend.from_json(json)
# print the JSON string representation of the object
print(PaymentBulkSend.to_json())

# convert the object into a dict
payment_bulk_send_dict = payment_bulk_send_instance.to_dict()
# create an instance of PaymentBulkSend from a dict
payment_bulk_send_from_dict = PaymentBulkSend.from_dict(payment_bulk_send_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


