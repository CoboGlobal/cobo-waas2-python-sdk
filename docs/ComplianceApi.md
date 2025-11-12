# cobo_waas2.ComplianceApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_disposition_status**](ComplianceApi.md#get_disposition_status) | **GET** /compliance/funds/disposition | Get disposition status
[**get_kyt_screening_status**](ComplianceApi.md#get_kyt_screening_status) | **GET** /compliance/kyt/screenings/status | Get KYT screening status
[**isolate_funds**](ComplianceApi.md#isolate_funds) | **POST** /compliance/funds/disposition/isolate | Isolate funds
[**refund_funds**](ComplianceApi.md#refund_funds) | **POST** /compliance/funds/disposition/refund | Refund funds
[**submit_kyt_manual_review**](ComplianceApi.md#submit_kyt_manual_review) | **POST** /compliance/kyt/screenings/manual_review | Submit KYT manual review result
[**submit_kyt_screening_decisions**](ComplianceApi.md#submit_kyt_screening_decisions) | **POST** /compliance/kyt/screenings/decisions | Submit KYT screening decision
[**unfreeze_funds**](ComplianceApi.md#unfreeze_funds) | **POST** /compliance/funds/disposition/unfreeze | Unfreeze frozen funds


# **get_disposition_status**
> DispositionQueryResponse get_disposition_status(transaction_id)

Get disposition status

This operation retrieves the current status of a disposition request for a specific transaction.  You can use this endpoint to check the status of any disposition operation (Refund, Isolate, or Unfreeze)  that has been initiated for a transaction. The response includes the disposition type, current status,  and the disposition transaction ID if applicable.  <Note>Use this endpoint to monitor the progress of disposition operations and verify their completion.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.disposition_query_response import DispositionQueryResponse
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
    api_instance = cobo_waas2.ComplianceApi(api_client)
    transaction_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get disposition status
        api_response = api_instance.get_disposition_status(transaction_id)
        print("The response of ComplianceApi->get_disposition_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_disposition_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The unique identifier (UUID) of the transaction to retrieve KYT screening status information for. | 

### Return type

[**DispositionQueryResponse**](DispositionQueryResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved disposition information. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kyt_screening_status**
> KytScreeningsTransaction get_kyt_screening_status(transaction_id)

Get KYT screening status

This operation retrieves the current KYT (Know Your Transaction) screening status, including review status and fund disposition status, for a specific transaction.  Use this endpoint to monitor the real-time screening progress for transactions processed through the KYT compliance system.  <Note>This endpoint provides comprehensive compliance monitoring capabilities to help maintain AML (Anti-Money Laundering) regulatory compliance and audit trail requirements.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.kyt_screenings_transaction import KytScreeningsTransaction
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
    api_instance = cobo_waas2.ComplianceApi(api_client)
    transaction_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get KYT screening status
        api_response = api_instance.get_kyt_screening_status(transaction_id)
        print("The response of ComplianceApi->get_kyt_screening_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_kyt_screening_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The unique identifier (UUID) of the transaction to retrieve KYT screening status information for. | 

### Return type

[**KytScreeningsTransaction**](KytScreeningsTransaction.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved KYT screening information. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isolate_funds**
> DispositionResponse isolate_funds(isolate_disposition=isolate_disposition)

Isolate funds

This operation creates a request to isolate funds for a specific transaction. The funds will be sent to a designated isolation address for compliance purposes.  You need to specify the transaction ID to be isolated and the destination address.  Optional parameters include custom categories for tracking purposes.  <Note>The isolation will initiate a withdrawal transaction from the compliance-managed address to the specified isolation address.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.disposition_response import DispositionResponse
from cobo_waas2.models.isolate_disposition import IsolateDisposition
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
    api_instance = cobo_waas2.ComplianceApi(api_client)
    isolate_disposition = cobo_waas2.IsolateDisposition()

    try:
        # Isolate funds
        api_response = api_instance.isolate_funds(isolate_disposition=isolate_disposition)
        print("The response of ComplianceApi->isolate_funds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->isolate_funds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isolate_disposition** | [**IsolateDisposition**](IsolateDisposition.md)| The request body to isolate funds. | [optional] 

### Return type

[**DispositionResponse**](DispositionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a disposition request. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_funds**
> DispositionResponse refund_funds(refund_disposition=refund_disposition)

Refund funds

This operation creates a request to refund funds for a specific transaction. The funds will be sent to the specified destination address.  You need to specify the transaction ID to be refunded and the destination address.  Optional parameters include custom categories for tracking purposes.  <Note>The refund will initiate a withdrawal transaction from the compliance-managed address to the specified destination.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.disposition_response import DispositionResponse
from cobo_waas2.models.refund_disposition import RefundDisposition
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
    api_instance = cobo_waas2.ComplianceApi(api_client)
    refund_disposition = cobo_waas2.RefundDisposition()

    try:
        # Refund funds
        api_response = api_instance.refund_funds(refund_disposition=refund_disposition)
        print("The response of ComplianceApi->refund_funds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->refund_funds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_disposition** | [**RefundDisposition**](RefundDisposition.md)| The request body to refund funds. | [optional] 

### Return type

[**DispositionResponse**](DispositionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a disposition request. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_kyt_manual_review**
> SubmitKytResponse submit_kyt_manual_review(submit_kyt_screenings_review_body=submit_kyt_screenings_review_body)

Submit KYT manual review result

This operation submits a manual review result for a KYT (Know Your Transaction) screening case that requires human analysis.  Use this endpoint when transactions flagged for manual review have been analyzed by compliance officers and require submission of review outcomes with detailed comments and justifications.  This endpoint is specifically designed for submitting comprehensive manual review findings rather than automated screening decisions.  <Note>Submitting a manual review result will update the KYT screening status and initiate appropriate compliance workflow actions based on the review outcome.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.submit_kyt_response import SubmitKytResponse
from cobo_waas2.models.submit_kyt_screenings_review_body import SubmitKytScreeningsReviewBody
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
    api_instance = cobo_waas2.ComplianceApi(api_client)
    submit_kyt_screenings_review_body = cobo_waas2.SubmitKytScreeningsReviewBody()

    try:
        # Submit KYT manual review result
        api_response = api_instance.submit_kyt_manual_review(submit_kyt_screenings_review_body=submit_kyt_screenings_review_body)
        print("The response of ComplianceApi->submit_kyt_manual_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->submit_kyt_manual_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_kyt_screenings_review_body** | [**SubmitKytScreeningsReviewBody**](SubmitKytScreeningsReviewBody.md)| The request body to submit a manual review result for a KYT screening case that requires human analysis. | [optional] 

### Return type

[**SubmitKytResponse**](SubmitKytResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully submitted a manual review result for a KYT screening case that requires human analysis. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_kyt_screening_decisions**
> SubmitKytResponse submit_kyt_screening_decisions(submit_kyt_screenings_decisions_body=submit_kyt_screenings_decisions_body)

Submit KYT screening decision

This operation submits a KYT (Know Your Transaction) screening decision for a specific transaction based on an external compliance review.  Use this endpoint to provide a screening decision (Approval, ApprovalWithAlert, Rejection, or ManualReview) after completing the external KYT screening process.  The submitted decision will be recorded for compliance audit purposes and regulatory reporting requirements.  <Note>Submitting a screening decision will update the transaction's KYT status and may automatically trigger downstream compliance workflows or notifications depending on the decision type.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.submit_kyt_response import SubmitKytResponse
from cobo_waas2.models.submit_kyt_screenings_decisions_body import SubmitKytScreeningsDecisionsBody
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
    api_instance = cobo_waas2.ComplianceApi(api_client)
    submit_kyt_screenings_decisions_body = cobo_waas2.SubmitKytScreeningsDecisionsBody()

    try:
        # Submit KYT screening decision
        api_response = api_instance.submit_kyt_screening_decisions(submit_kyt_screenings_decisions_body=submit_kyt_screenings_decisions_body)
        print("The response of ComplianceApi->submit_kyt_screening_decisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->submit_kyt_screening_decisions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_kyt_screenings_decisions_body** | [**SubmitKytScreeningsDecisionsBody**](SubmitKytScreeningsDecisionsBody.md)| The request body to submit a KYT screening decision for a specific transaction based on external compliance review. | [optional] 

### Return type

[**SubmitKytResponse**](SubmitKytResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully submitted a KYT screening decision for a specific transaction tranaction based on external compliance review. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfreeze_funds**
> DispositionResponse unfreeze_funds(unfreeze_disposition=unfreeze_disposition)

Unfreeze frozen funds

This operation creates a request to unfreeze funds for a previously frozen transaction. It releases the frozen funds back to their original state.  You only need to specify the transaction ID to be unfrozen. Once unfrozen, the funds will be available for normal operations.  <Note>The unfreeze process will release the compliance hold on the transaction, allowing it to proceed normally.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.disposition_response import DispositionResponse
from cobo_waas2.models.unfreeze_disposition import UnfreezeDisposition
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
    api_instance = cobo_waas2.ComplianceApi(api_client)
    unfreeze_disposition = cobo_waas2.UnfreezeDisposition()

    try:
        # Unfreeze frozen funds
        api_response = api_instance.unfreeze_funds(unfreeze_disposition=unfreeze_disposition)
        print("The response of ComplianceApi->unfreeze_funds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->unfreeze_funds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unfreeze_disposition** | [**UnfreezeDisposition**](UnfreezeDisposition.md)| The request body to unfreeze funds. | [optional] 

### Return type

[**DispositionResponse**](DispositionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a disposition request. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

