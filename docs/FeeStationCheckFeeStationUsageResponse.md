# FeeStationCheckFeeStationUsageResponse

The fee station evaluation result for the transfer request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token used to pay the gas fee for this specific transaction. You can retrieve the IDs of all supported tokens by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 
**balance** | **str** | The current token balance available in the fee station. | 
**gas_station_type** | [**FeeStationGasStationType**](FeeStationGasStationType.md) |  | 
**is_fee_station_applicable** | **bool** | Indicates whether the fee station is applied for this transfer request. | 
**is_balance_sufficient** | **bool** | If the fee station is used, indicates whether its balance is sufficient to cover the required gas fee. | 
**total_fee_amount** | **str** | The total gas amount required for this transfer request. | 
**is_sponsor_applicable** | **bool** | Indicates whether USDT (U) sponsorship is applied when the fee station balance is insufficient. | 
**sponsored_fee_amount** | **str** | The amount of gas fee sponsored by USDT (U) when applicable. | 
**sponsored_token_id** | **str** | The token ID used to sponsor the gas fee. | [optional] 

## Example

```python
from cobo_waas2.models.fee_station_check_fee_station_usage_response import FeeStationCheckFeeStationUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeeStationCheckFeeStationUsageResponse from a JSON string
fee_station_check_fee_station_usage_response_instance = FeeStationCheckFeeStationUsageResponse.from_json(json)
# print the JSON string representation of the object
print(FeeStationCheckFeeStationUsageResponse.to_json())

# convert the object into a dict
fee_station_check_fee_station_usage_response_dict = fee_station_check_fee_station_usage_response_instance.to_dict()
# create an instance of FeeStationCheckFeeStationUsageResponse from a dict
fee_station_check_fee_station_usage_response_from_dict = FeeStationCheckFeeStationUsageResponse.from_dict(fee_station_check_fee_station_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


