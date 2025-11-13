# CounterpartyDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_id** | **str** | The counterparty ID. | [optional] 
**counterparty_type** | [**CounterpartyType**](CounterpartyType.md) |  | 
**counterparty_name** | **str** | The counterparty name. | 
**country** | **str** | The country of the counterparty, in ISO 3166-1 alpha-3 format. | [optional] 
**email** | **str** | The email of the counterparty. | [optional] 
**contact_address** | **str** | The contact address of the counterparty. | [optional] 
**wallet_addresses** | [**List[WalletAddress]**](WalletAddress.md) | The wallet addresses of the counterparty. | 
**created_timestamp** | **int** | The created time of the counterparty, represented as a UNIX timestamp in seconds. | 
**updated_timestamp** | **int** | The updated time of the counterparty, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.counterparty_detail import CounterpartyDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CounterpartyDetail from a JSON string
counterparty_detail_instance = CounterpartyDetail.from_json(json)
# print the JSON string representation of the object
print(CounterpartyDetail.to_json())

# convert the object into a dict
counterparty_detail_dict = counterparty_detail_instance.to_dict()
# create an instance of CounterpartyDetail from a dict
counterparty_detail_from_dict = CounterpartyDetail.from_dict(counterparty_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


