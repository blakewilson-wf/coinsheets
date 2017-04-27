# \AuthenticationApi

All URIs are relative to *https://api.wk-dev.wdesk.org/v1beta1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Oauth2TokenPost**](AuthenticationApi.md#Oauth2TokenPost) | **Post** /oauth2/token | Create an OAuth bearer token.


# **Oauth2TokenPost**
> BearerToken Oauth2TokenPost($clientId, $clientSecret, $grantType, $xApiKey, $contentType, $accept)

Create an OAuth bearer token.

Given a valid client_id and client_secret, create a bearer token for the current user. 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientId** | **string**| The users client id. | 
 **clientSecret** | **string**| The users client secret. | 
 **grantType** | **string**| The grant type for the Bearer token. Must be client_credentials. | 
 **xApiKey** | **string**| API callers are identified by API keys. Throttling and request quota limits are set for each individual API key.   | 
 **contentType** | **string**| Mime type of request body. | [optional] [default to application/json]
 **accept** | **string**| The requested content type. For example, application/json. Per the HTTP guidelines, this is just a hint and responses MAY have a  different content type.  | [optional] [default to application/json]

### Return type

[**BearerToken**](BearerToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

