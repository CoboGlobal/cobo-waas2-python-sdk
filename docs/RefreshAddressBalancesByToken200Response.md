# RefreshAddressBalancesByToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submitted** | **bool** | Whether the request to refresh address balances has been successfully submitted. - &#x60;true&#x60;: The request to refresh address balances has been successfully submitted. - &#x60;false&#x60;: The request to  refresh address balances has not been submitted.  | 

## Example

```python
from cobo_waas2.models.refresh_address_balances_by_token200_response import RefreshAddressBalancesByToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshAddressBalancesByToken200Response from a JSON string
refresh_address_balances_by_token200_response_instance = RefreshAddressBalancesByToken200Response.from_json(json)
# print the JSON string representation of the object
print(RefreshAddressBalancesByToken200Response.to_json())

# convert the object into a dict
refresh_address_balances_by_token200_response_dict = refresh_address_balances_by_token200_response_instance.to_dict()
# create an instance of RefreshAddressBalancesByToken200Response from a dict
refresh_address_balances_by_token200_response_from_dict = RefreshAddressBalancesByToken200Response.from_dict(refresh_address_balances_by_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


