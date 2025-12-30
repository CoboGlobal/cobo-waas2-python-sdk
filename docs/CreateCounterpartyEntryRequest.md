# CreateCounterpartyEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_id** | **str** | The counterparty ID. | 
**wallet_addresses** | [**List[CreateWalletAddress]**](CreateWalletAddress.md) | The wallet addresses of the counterparty. | [optional] 

## Example

```python
from cobo_waas2.models.create_counterparty_entry_request import CreateCounterpartyEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCounterpartyEntryRequest from a JSON string
create_counterparty_entry_request_instance = CreateCounterpartyEntryRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCounterpartyEntryRequest.to_json())

# convert the object into a dict
create_counterparty_entry_request_dict = create_counterparty_entry_request_instance.to_dict()
# create an instance of CreateCounterpartyEntryRequest from a dict
create_counterparty_entry_request_from_dict = CreateCounterpartyEntryRequest.from_dict(create_counterparty_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


