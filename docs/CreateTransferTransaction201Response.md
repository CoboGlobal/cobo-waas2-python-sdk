# CreateTransferTransaction201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | 
**transaction_id** | **str** | The transaction ID. | 
**status** | [**TransactionStatus**](TransactionStatus.md) |  | 

## Example

```python
from cobo_waas2.models.create_transfer_transaction201_response import CreateTransferTransaction201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransferTransaction201Response from a JSON string
create_transfer_transaction201_response_instance = CreateTransferTransaction201Response.from_json(json)
# print the JSON string representation of the object
print(CreateTransferTransaction201Response.to_json())

# convert the object into a dict
create_transfer_transaction201_response_dict = create_transfer_transaction201_response_instance.to_dict()
# create an instance of CreateTransferTransaction201Response from a dict
create_transfer_transaction201_response_from_dict = CreateTransferTransaction201Response.from_dict(create_transfer_transaction201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


