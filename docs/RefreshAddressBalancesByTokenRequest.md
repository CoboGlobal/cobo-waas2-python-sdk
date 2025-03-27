# RefreshAddressBalancesByTokenRequest

The request body to refresh the addresses balance by  specified token within a specified wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | A list of  address. | 

## Example

```python
from cobo_waas2.models.refresh_address_balances_by_token_request import RefreshAddressBalancesByTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshAddressBalancesByTokenRequest from a JSON string
refresh_address_balances_by_token_request_instance = RefreshAddressBalancesByTokenRequest.from_json(json)
# print the JSON string representation of the object
print(RefreshAddressBalancesByTokenRequest.to_json())

# convert the object into a dict
refresh_address_balances_by_token_request_dict = refresh_address_balances_by_token_request_instance.to_dict()
# create an instance of RefreshAddressBalancesByTokenRequest from a dict
refresh_address_balances_by_token_request_from_dict = RefreshAddressBalancesByTokenRequest.from_dict(refresh_address_balances_by_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


