# CreateCounterpartyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_name** | **str** | The counterparty name. | 
**counterparty_type** | [**CounterpartyType**](CounterpartyType.md) |  | 
**wallet_addresses** | [**List[CreateWalletAddress]**](CreateWalletAddress.md) | The wallet addresses of the counterparty. | 
**country** | **str** | The country of the counterparty, in ISO 3166-1 alpha-3 format. | [optional] 
**email** | **str** | The email of the counterparty. | [optional] 
**contact_address** | **str** | The contact address of the counterparty. | [optional] 

## Example

```python
from cobo_waas2.models.create_counterparty_request import CreateCounterpartyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCounterpartyRequest from a JSON string
create_counterparty_request_instance = CreateCounterpartyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCounterpartyRequest.to_json())

# convert the object into a dict
create_counterparty_request_dict = create_counterparty_request_instance.to_dict()
# create an instance of CreateCounterpartyRequest from a dict
create_counterparty_request_from_dict = CreateCounterpartyRequest.from_dict(create_counterparty_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


