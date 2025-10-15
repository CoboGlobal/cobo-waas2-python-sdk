# FeeStationCheckFeeStationUsage

The information for evaluating Fee Station usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | 
**amount** | **str** | The amount of tokens to be transferred in this request. | 
**token_id** | **str** | The token ID of the transferred token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 
**estimated_fee_amount** | **str** | The estimated transaction fee required for this transfer, before applying any Fee Station rules. | 
**from_address** | **str** | The blockchain address that initiates the transfer. | 
**from_wallet_id** | **str** | The wallet ID. | 

## Example

```python
from cobo_waas2.models.fee_station_check_fee_station_usage import FeeStationCheckFeeStationUsage

# TODO update the JSON string below
json = "{}"
# create an instance of FeeStationCheckFeeStationUsage from a JSON string
fee_station_check_fee_station_usage_instance = FeeStationCheckFeeStationUsage.from_json(json)
# print the JSON string representation of the object
print(FeeStationCheckFeeStationUsage.to_json())

# convert the object into a dict
fee_station_check_fee_station_usage_dict = fee_station_check_fee_station_usage_instance.to_dict()
# create an instance of FeeStationCheckFeeStationUsage from a dict
fee_station_check_fee_station_usage_from_dict = FeeStationCheckFeeStationUsage.from_dict(fee_station_check_fee_station_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


