# FeeStationTransfer

The information about a Fee Station top-up transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID of the transferred token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 
**destination** | [**FeeStationDestination**](FeeStationDestination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.fee_station_transfer import FeeStationTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of FeeStationTransfer from a JSON string
fee_station_transfer_instance = FeeStationTransfer.from_json(json)
# print the JSON string representation of the object
print(FeeStationTransfer.to_json())

# convert the object into a dict
fee_station_transfer_dict = fee_station_transfer_instance.to_dict()
# create an instance of FeeStationTransfer from a dict
fee_station_transfer_from_dict = FeeStationTransfer.from_dict(fee_station_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


