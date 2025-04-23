# FeeStationDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The destination address. | [optional] 
**memo** | **str** | The memo that identifies a transaction in order to credit the correct account. For transfers out of Cobo Portal, it is highly recommended to include a memo for the chains such as XRP, EOS, XLM, IOST, BNB_BNB, ATOM, LUNA, and TON. | [optional] 
**amount** | **str** | The transfer amount. For example, if you trade 1.5 BTC, then the value is &#x60;1.5&#x60;.  | 

## Example

```python
from cobo_waas2.models.fee_station_destination import FeeStationDestination

# TODO update the JSON string below
json = "{}"
# create an instance of FeeStationDestination from a JSON string
fee_station_destination_instance = FeeStationDestination.from_json(json)
# print the JSON string representation of the object
print(FeeStationDestination.to_json())

# convert the object into a dict
fee_station_destination_dict = fee_station_destination_instance.to_dict()
# create an instance of FeeStationDestination from a dict
fee_station_destination_from_dict = FeeStationDestination.from_dict(fee_station_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


