# cobo_waas2.TravelRuleApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_satoshi_test_challenge**](TravelRuleApi.md#cancel_satoshi_test_challenge) | **POST** /travel_rule/satoshi_test/challenge/cancel | Cancel Satoshi Test challenge
[**create_satoshi_test_challenge**](TravelRuleApi.md#create_satoshi_test_challenge) | **POST** /travel_rule/satoshi_test/challenge | Create Satoshi Test challenge
[**get_address_verification**](TravelRuleApi.md#get_address_verification) | **GET** /travel_rule/address_verifications/{verification_id} | Get address verification
[**get_satoshi_test_challenge**](TravelRuleApi.md#get_satoshi_test_challenge) | **GET** /travel_rule/satoshi_test/challenge/status | Get Satoshi Test challenge
[**get_signature_challenge**](TravelRuleApi.md#get_signature_challenge) | **GET** /travel_rule/signature_challenge | Get self-custody signature challenge
[**get_transaction_limitation**](TravelRuleApi.md#get_transaction_limitation) | **GET** /travel_rule/transaction/limitation | Retrieve transaction limitations
[**list_address_verifications**](TravelRuleApi.md#list_address_verifications) | **GET** /travel_rule/address_verifications | List address verifications
[**list_supported_countries**](TravelRuleApi.md#list_supported_countries) | **GET** /travel_rule/transaction/countries | List supported countries
[**submit_deposit_travel_rule_info**](TravelRuleApi.md#submit_deposit_travel_rule_info) | **POST** /travel_rule/transaction/deposit/travel_rule_info | Submit Travel Rule information for deposits
[**submit_withdraw_travel_rule_info**](TravelRuleApi.md#submit_withdraw_travel_rule_info) | **POST** /travel_rule/transaction/withdraw/travel_rule_info | Submit Travel Rule information for withdrawals


# **cancel_satoshi_test_challenge**
> SatoshiTestCancelResult cancel_satoshi_test_challenge(cancel_satoshi_test_challenge_request=cancel_satoshi_test_challenge_request)

Cancel Satoshi Test challenge

This operation cancels a Satoshi Test challenge that is currently in `PREPARE` or `PENDING` status. Typical use case: the counterparty decides to switch verification methods before transferring.  Once cancelled, the challenge status becomes `DELETED` and the on-chain match will no longer be observed. Challenges already in `MATCHED`, `VERIFIED`, `EXPIRED`, or `DELETED` state cannot be cancelled. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.cancel_satoshi_test_challenge_request import CancelSatoshiTestChallengeRequest
from cobo_waas2.models.satoshi_test_cancel_result import SatoshiTestCancelResult
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
    cancel_satoshi_test_challenge_request = cobo_waas2.CancelSatoshiTestChallengeRequest()

    try:
        # Cancel Satoshi Test challenge
        api_response = api_instance.cancel_satoshi_test_challenge(cancel_satoshi_test_challenge_request=cancel_satoshi_test_challenge_request)
        print("The response of TravelRuleApi->cancel_satoshi_test_challenge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->cancel_satoshi_test_challenge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_satoshi_test_challenge_request** | [**CancelSatoshiTestChallengeRequest**](CancelSatoshiTestChallengeRequest.md)|  | [optional] 

### Return type

[**SatoshiTestCancelResult**](SatoshiTestCancelResult.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The challenge has been cancelled. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_satoshi_test_challenge**
> SatoshiTestChallenge create_satoshi_test_challenge(create_satoshi_test_challenge_request=create_satoshi_test_challenge_request)

Create Satoshi Test challenge

This operation creates a Satoshi Test challenge for self-custody address verification. Satoshi Test verifies address ownership by having the counterparty transfer a small, uniquely-generated amount from their wallet to a Cobo-controlled verification address.  A single endpoint covers both flows via the `action` parameter: - **Two-step flow** (`action=PREPARE` then `action=SUBMIT`): Preview the verification details first, then activate. The 180-minute countdown only starts on `SUBMIT`. The server uses `(chain_id, from_address)` as the idempotency key, so the second call automatically targets the prepared challenge. For extra safety, pass the `challenge_id` returned by `PREPARE` in the subsequent `SUBMIT` call — it pins the activation to that specific challenge. - **One-shot flow** (`action=SUBMIT` directly, without `challenge_id`): Prepare and submit in a single call. The challenge is created directly in `PENDING` state with the countdown started.  If the counterparty address has already been verified, the operation returns HTTP 400 `ADDRESS_ALREADY_VERIFIED`. Call [List address verifications](#operation/list_address_verifications) with `chain_id`, `address`, and `status=VERIFIED` first to pre-check.  Supported chains: `BTC`, `ETH`, `BASE_ETH`, `BSC_BNB`, `TRON`. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_satoshi_test_challenge_request import CreateSatoshiTestChallengeRequest
from cobo_waas2.models.satoshi_test_challenge import SatoshiTestChallenge
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
    create_satoshi_test_challenge_request = cobo_waas2.CreateSatoshiTestChallengeRequest()

    try:
        # Create Satoshi Test challenge
        api_response = api_instance.create_satoshi_test_challenge(create_satoshi_test_challenge_request=create_satoshi_test_challenge_request)
        print("The response of TravelRuleApi->create_satoshi_test_challenge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->create_satoshi_test_challenge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_satoshi_test_challenge_request** | [**CreateSatoshiTestChallengeRequest**](CreateSatoshiTestChallengeRequest.md)|  | [optional] 

### Return type

[**SatoshiTestChallenge**](SatoshiTestChallenge.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Satoshi Test challenge was created.  - &#x60;action&#x3D;PREPARE&#x60;: returned challenge has &#x60;status&#x3D;PREPARE&#x60;; the 180-minute countdown is not started yet. - &#x60;action&#x3D;SUBMIT&#x60;: returned challenge has &#x60;status&#x3D;PENDING&#x60;; &#x60;started_at&#x60; and &#x60;expires_at&#x60; are set.  If the counterparty address has already been verified (by signature or a prior Satoshi Test), this operation returns HTTP 400 &#x60;ADDRESS_ALREADY_VERIFIED&#x60; instead — call [List address verifications](#operation/list_address_verifications) with &#x60;chain_id&#x60;, &#x60;address&#x60;, and &#x60;status&#x3D;VERIFIED&#x60; first to pre-check.  |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_verification**
> AddressVerificationDetail get_address_verification(verification_id)

Get address verification

Retrieve a single self-custody address verification record by its `verification_id`, including method-specific provenance:  - `verification_method=SIGNATURE` → `signature_detail` is populated. - `verification_method=SATOSHI_TEST` → `satoshi_test_detail` carries the latest challenge state (`status`, `remaining_seconds`, `matched_txid`).  Use [List address verifications](#operation/list_address_verifications) to discover `verification_id` values. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.address_verification_detail import AddressVerificationDetail
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
    verification_id = 'fb377ea5-a97a-49b4-955d-23f8fdd5177a'

    try:
        # Get address verification
        api_response = api_instance.get_address_verification(verification_id)
        print("The response of TravelRuleApi->get_address_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->get_address_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verification_id** | **str**| The unique identifier of the address verification record. | 

### Return type

[**AddressVerificationDetail**](AddressVerificationDetail.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The address verification record. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_satoshi_test_challenge**
> SatoshiTestChallenge get_satoshi_test_challenge(challenge_id)

Get Satoshi Test challenge

This operation returns the current state of a Satoshi Test challenge — useful for polling after submission. The response contains the challenge `status` and `remaining_seconds`.  Recommended polling interval: 10–30 seconds. The challenge will transition through `PENDING` → `MATCHED` → `VERIFIED` once the counterparty's transfer is observed and confirmed on chain. If the challenge is not matched within 180 minutes, the status becomes `EXPIRED`. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.satoshi_test_challenge import SatoshiTestChallenge
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
    challenge_id = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'

    try:
        # Get Satoshi Test challenge
        api_response = api_instance.get_satoshi_test_challenge(challenge_id)
        print("The response of TravelRuleApi->get_satoshi_test_challenge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->get_satoshi_test_challenge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **str**| The Satoshi Test challenge ID returned by the &#x60;prepare&#x60; or &#x60;submit&#x60; operation. | 

### Return type

[**SatoshiTestChallenge**](SatoshiTestChallenge.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Satoshi Test challenge information (after submit or for status polling). |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signature_challenge**
> SignatureChallenge get_signature_challenge(transaction_type, transaction_id)

Get self-custody signature challenge

This operation issues a one-time, time-bounded message for a self-custody wallet address to sign, in order to prove wallet ownership. The signature is then submitted via [Submit Travel Rule information for deposits](#operation/submit_deposit_travel_rule_info) or [withdrawals](#operation/submit_withdraw_travel_rule_info).  Use this endpoint when you want to verify the counterparty's self-custody address via off-chain signature. For address verification via on-chain micro-deposit, use the Satoshi Test endpoints (`/travel_rule/satoshi_test/...`) instead.  The challenge is valid for a short window (returned as `expires_in`, currently 30 seconds). Calling this endpoint again for the same transaction rotates the challenge — only the latest issued value will verify. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.signature_challenge import SignatureChallenge
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
        # Get self-custody signature challenge
        api_response = api_instance.get_signature_challenge(transaction_type, transaction_id)
        print("The response of TravelRuleApi->get_signature_challenge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->get_signature_challenge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_type** | **str**| The transaction type. Possible values include:    - &#x60;DEPOSIT&#x60;: A deposit transaction.   - &#x60;WITHDRAW&#x60;: A withdrawal transaction.  | 
 **transaction_id** | **str**| The transaction ID. | 

### Return type

[**SignatureChallenge**](SignatureChallenge.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The signature challenge was issued successfully. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_limitation**
> GetTransactionLimitation200Response get_transaction_limitation(transaction_type, transaction_id)

Retrieve transaction limitations

<Note>The `self_custody_wallet_challenge` field in the response is deprecated. To obtain a signature challenge, call [Get self-custody signature challenge](#operation/get_signature_challenge) instead. This operation itself is not deprecated and continues to return the VASP list, threshold info, connect wallet list, and Satoshi Test support.</Note>  This operation retrieves Travel Rule requirements and available options for a transaction based on its transaction type and ID.  Use this endpoint before submitting Travel Rule information to understand the requirements and available options for your transaction. 

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

# **list_address_verifications**
> ListAddressVerifications200Response list_address_verifications(status=status, chain_id=chain_id, address=address, limit=limit, before=before, after=after)

List address verifications

List self-custody address verification records under the current organization with optional filters and cursor-based pagination.  Records are sorted by creation time descending (most recent first). Use `limit` plus `before` / `after` cursors from the previous page's `pagination` block to traverse pages.  Each record's `status` is one of `PENDING`, `VERIFIED`, or `FAILED`. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.address_verification_status import AddressVerificationStatus
from cobo_waas2.models.list_address_verifications200_response import ListAddressVerifications200Response
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
    status = cobo_waas2.AddressVerificationStatus()
    chain_id = 'ETH'
    address = '0x1234567890abcdef1234567890abcdef12345678'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List address verifications
        api_response = api_instance.list_address_verifications(status=status, chain_id=chain_id, address=address, limit=limit, before=before, after=after)
        print("The response of TravelRuleApi->list_address_verifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->list_address_verifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**AddressVerificationStatus**](.md)| Filter by verification status. Allowed values: - &#x60;PENDING&#x60;: A Satoshi Test challenge is in progress (countdown active or awaiting confirmation). - &#x60;VERIFIED&#x60;: The address ownership has been confirmed (by signature or by a matched Satoshi Test transfer). - &#x60;FAILED&#x60;: The verification attempt did not succeed (Satoshi Test expired without match, or signature verification rejected).  Omit this parameter to return records of all three statuses.  | [optional] 
 **chain_id** | **str**| Filter by chain ID (e.g. &#x60;BTC&#x60;, &#x60;ETH&#x60;, &#x60;BASE_ETH&#x60;, &#x60;BSC_BNB&#x60;, &#x60;TRON&#x60;). | [optional] 
 **address** | **str**| Filter by counterparty (self-custody) wallet address. | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 

### Return type

[**ListAddressVerifications200Response**](ListAddressVerifications200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of address verification records. |  -  |
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

