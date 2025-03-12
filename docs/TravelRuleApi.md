# cobo_waas2.TravelRuleApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_limitation**](TravelRuleApi.md#get_transaction_limitation) | **GET** /travel_rule/transaction/limitation | Retrieve transaction limitations
[**list_supported_countries**](TravelRuleApi.md#list_supported_countries) | **GET** /travel_rule/transaction/countries | List supported countries
[**submit_deposit_travel_rule_info**](TravelRuleApi.md#submit_deposit_travel_rule_info) | **POST** /travel_rule/transaction/deposit/travel_rule_info | Submit Travel Rule information for deposits
[**submit_withdraw_travel_rule_info**](TravelRuleApi.md#submit_withdraw_travel_rule_info) | **POST** /travel_rule/transaction/withdraw/travel_rule_info | Submit Travel Rule information for withdrawals


# **get_transaction_limitation**
> GetTransactionLimitation200Response get_transaction_limitation(transaction_type, transaction_id)

Retrieve transaction limitations

This operation retrieves Travel Rule requirements and available options for a transaction based on its transaction type and ID.  Use this endpoint before submitting Travel Rule information to understand the requirements and available options for your transaction. 

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
 **transaction_id** | **str**| The transaction ID. | 

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

This operation retrieves a list of supported countries that can be used when submitting Travel Rule information.  Use this endpoint to obtain valid country values for:   - Place of incorporation of a legal entity   - Place of birth of a natural person 

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

Submit Travel Rule information for deposits

This operation submits Travel Rule information for a deposit transaction. 

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
        # Submit Travel Rule information for deposits
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
**201** | Successfully submitted the Travel Rule information. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_withdraw_travel_rule_info**
> SubmitDepositTravelRuleInfo201Response submit_withdraw_travel_rule_info(travel_rule_withdraw_request=travel_rule_withdraw_request)

Submit Travel Rule information for withdrawals

This operation submits Travel Rule information for a withdrawal transaction. 

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
        # Submit Travel Rule information for withdrawals
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
**201** | Successfully submitted the Travel Rule information. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

