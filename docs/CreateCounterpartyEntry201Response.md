# CreateCounterpartyEntry201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_id** | **str** | The counterparty ID. | 
**wallet_addresses** | [**List[WalletAddress]**](WalletAddress.md) | The wallet addresses of the counterparty. | 

## Example

```python
from cobo_waas2.models.create_counterparty_entry201_response import CreateCounterpartyEntry201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCounterpartyEntry201Response from a JSON string
create_counterparty_entry201_response_instance = CreateCounterpartyEntry201Response.from_json(json)
# print the JSON string representation of the object
print(CreateCounterpartyEntry201Response.to_json())

# convert the object into a dict
create_counterparty_entry201_response_dict = create_counterparty_entry201_response_instance.to_dict()
# create an instance of CreateCounterpartyEntry201Response from a dict
create_counterparty_entry201_response_from_dict = CreateCounterpartyEntry201Response.from_dict(create_counterparty_entry201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


