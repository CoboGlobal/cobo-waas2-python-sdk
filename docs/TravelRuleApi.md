# cobo_waas2.TravelRuleApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_limitation**](TravelRuleApi.md#get_transaction_limitation) | **GET** /travel_rule/transaction/limitation | Retrieve transaction limitations
[**list_supported_countries**](TravelRuleApi.md#list_supported_countries) | **GET** /travel_rule/transaction/countries | List supported countries
[**submit_deposit_travel_rule_info**](TravelRuleApi.md#submit_deposit_travel_rule_info) | **POST** /travel_rule/transaction/deposit/travel_rule_info | Submit Deposit Transaction Travel Rule information
[**submit_withdraw_travel_rule_info**](TravelRuleApi.md#submit_withdraw_travel_rule_info) | **POST** /travel_rule/transaction/withdraw/travel_rule_info | Submit Withdraw Transaction Travel Rule information


# **get_transaction_limitation**
> GetTransactionLimitation200Response get_transaction_limitation(transaction_type, transaction_id)

Retrieve transaction limitations

This endpoint retrieves transaction-related limitations based on the provided `transaction_type` and `transaction_id`.  The response includes the following information: - **`vasp_list`**: A list of Virtual Asset Service Providers (VASPs) associated with the transaction token. - **`is_threshold_reached`**: Indicates whether the transaction amount has exceeded the predefined threshold.    - If `true`: Additional Travel Rule information may be required for processing. - **`self_custody_wallet_challenge`**: A challenge string for verifying ownership of self-custody wallets. - **`connect_wallet_list`**: A list of supported wallet integrations for the transaction, such as MetaMask or WalletConnect.  Use this endpoint to ensure compliance with Travel Rule requirements and to retrieve supported options for completing the transaction. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.get_transaction_limitation200_response import GetTransactionLimitation200Response
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TravelRuleApi(api_client)
    transaction_type = 'DEPOSIT'
    transaction_id = '123e4567-e89b-12d3-a456-426614174000'

    try:
        # Retrieve transaction limitations
        api_response = api_instance.get_transaction_limitation(transaction_type, transaction_id)
        print("The response of TravelRuleApi->get_transaction_limitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->get_transaction_limitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_type** | **str**| The transaction type. Possible values include:    - &#x60;DEPOSIT&#x60;: A deposit transaction.   - &#x60;WITHDRAW&#x60;: A withdrawal transaction.  | 
 **transaction_id** | **str**| The transaction ID | 

### Return type

[**GetTransactionLimitation200Response**](GetTransactionLimitation200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supported_countries**
> List[ListSupportedCountries200ResponseInner] list_supported_countries()

List supported countries

This operation retrieves all countries supported.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_supported_countries200_response_inner import ListSupportedCountries200ResponseInner
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TravelRuleApi(api_client)

    try:
        # List supported countries
        api_response = api_instance.list_supported_countries()
        print("The response of TravelRuleApi->list_supported_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->list_supported_countries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ListSupportedCountries200ResponseInner]**](ListSupportedCountries200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of countries supported. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_deposit_travel_rule_info**
> SubmitDepositTravelRuleInfo201Response submit_deposit_travel_rule_info(travel_rule_deposit_request=travel_rule_deposit_request)

Submit Deposit Transaction Travel Rule information

This operation allows you to submit the required Travel Rule information based on the transaction details. It supports both self-custody wallets and exchanges/VASPs, ensuring compliance with Travel Rule requirements.   - **Destination Wallet Type (`destination_wallet_type`)**:   - `SELF_CUSTODY_WALLET`: A self-custodial wallet (e.g., plugin wallet). Requires `self_custody_wallet_sign`, `self_custody_wallet_address`, and `self_custody_wallet_challenge`.   - `EXCHANGES_OR_VASP`: A wallet associated with an exchange or VASP. Requires `vendor_vasp_id` and information depending on `selected_entity_type`.  - **Entity Types (`selected_entity_type`)**:   - `LEGAL`: For legal entities, provide `legal_name`, `date_of_incorporation`, and `place_of_incorporation`.   - `NATURAL`: For natural persons, provide `date_of_birth`, `place_of_birth`, `first_name`, and `last_name`. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.submit_deposit_travel_rule_info201_response import SubmitDepositTravelRuleInfo201Response
from cobo_waas2.models.travel_rule_deposit_request import TravelRuleDepositRequest
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TravelRuleApi(api_client)
    travel_rule_deposit_request = cobo_waas2.TravelRuleDepositRequest()

    try:
        # Submit Deposit Transaction Travel Rule information
        api_response = api_instance.submit_deposit_travel_rule_info(travel_rule_deposit_request=travel_rule_deposit_request)
        print("The response of TravelRuleApi->submit_deposit_travel_rule_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->submit_deposit_travel_rule_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **travel_rule_deposit_request** | [**TravelRuleDepositRequest**](TravelRuleDepositRequest.md)|  | [optional] 

### Return type

[**SubmitDepositTravelRuleInfo201Response**](SubmitDepositTravelRuleInfo201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully submitted Travel Rule information. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_withdraw_travel_rule_info**
> SubmitDepositTravelRuleInfo201Response submit_withdraw_travel_rule_info(travel_rule_withdraw_request=travel_rule_withdraw_request)

Submit Withdraw Transaction Travel Rule information

This operation allows you to submit the required Travel Rule information based on the transaction details. It supports both self-custody wallets and exchanges/VASPs, ensuring compliance with Travel Rule requirements.   - **Destination Wallet Type (`destination_wallet_type`)**:   - `SELF_CUSTODY_WALLET`: A self-custodial wallet (e.g., plugin wallet). Requires `self_custody_wallet_sign`, `self_custody_wallet_address`, and `self_custody_wallet_challenge`.   - `EXCHANGES_OR_VASP`: A wallet associated with an exchange or VASP. Requires `vendor_vasp_id` and information depending on `selected_entity_type`.  - **Entity Types (`selected_entity_type`)**:   - `LEGAL`: For legal entities, provide `legal_name`.   - `NATURAL`: For natural persons, provide `date_of_birth`, `place_of_birth`, `first_name`, and `last_name`. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.submit_deposit_travel_rule_info201_response import SubmitDepositTravelRuleInfo201Response
from cobo_waas2.models.travel_rule_withdraw_request import TravelRuleWithdrawRequest
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TravelRuleApi(api_client)
    travel_rule_withdraw_request = cobo_waas2.TravelRuleWithdrawRequest()

    try:
        # Submit Withdraw Transaction Travel Rule information
        api_response = api_instance.submit_withdraw_travel_rule_info(travel_rule_withdraw_request=travel_rule_withdraw_request)
        print("The response of TravelRuleApi->submit_withdraw_travel_rule_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->submit_withdraw_travel_rule_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **travel_rule_withdraw_request** | [**TravelRuleWithdrawRequest**](TravelRuleWithdrawRequest.md)|  | [optional] 

### Return type

[**SubmitDepositTravelRuleInfo201Response**](SubmitDepositTravelRuleInfo201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully submitted Travel Rule information. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

