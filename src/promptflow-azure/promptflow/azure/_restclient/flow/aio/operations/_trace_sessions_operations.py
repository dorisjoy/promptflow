# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.8.0, generator: @autorest/python@5.12.2)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._trace_sessions_operations import build_attach_cosmos_account_request, build_cleanup_trace_session_async_request, build_get_cosmos_resource_token_request, build_get_trace_session_metadata_async_request, build_init_trace_session_async_request, build_poll_trace_session_status_request, build_setup_trace_session_async_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class TraceSessionsOperations:
    """TraceSessionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~flow.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def setup_trace_session_async(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        body: Optional["_models.TraceDbSetupRequest"] = None,
        **kwargs: Any
    ) -> Union["_models.TraceCosmosResourceDtos", Any]:
        """setup_trace_session_async.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param body:
        :type body: ~flow.models.TraceDbSetupRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TraceCosmosResourceDtos or any, or the result of cls(response)
        :rtype: ~flow.models.TraceCosmosResourceDtos or any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Union["_models.TraceCosmosResourceDtos", Any]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'TraceDbSetupRequest')
        else:
            _json = None

        request = build_setup_trace_session_async_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            content_type=content_type,
            json=_json,
            template_url=self.setup_trace_session_async.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('TraceCosmosResourceDtos', pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize('object', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    setup_trace_session_async.metadata = {'url': '/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/TraceSessions/setup'}  # type: ignore


    @distributed_trace_async
    async def init_trace_session_async(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        overwrite: Optional[bool] = False,
        **kwargs: Any
    ) -> Union["_models.TraceCosmosResourceDtos", Any]:
        """init_trace_session_async.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param overwrite:
        :type overwrite: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TraceCosmosResourceDtos or any, or the result of cls(response)
        :rtype: ~flow.models.TraceCosmosResourceDtos or any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Union["_models.TraceCosmosResourceDtos", Any]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_init_trace_session_async_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            overwrite=overwrite,
            template_url=self.init_trace_session_async.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('TraceCosmosResourceDtos', pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize('object', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    init_trace_session_async.metadata = {'url': '/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/TraceSessions/initialize'}  # type: ignore


    @distributed_trace_async
    async def get_trace_session_metadata_async(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        **kwargs: Any
    ) -> "_models.TraceCosmosMetaDto":
        """get_trace_session_metadata_async.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TraceCosmosMetaDto, or the result of cls(response)
        :rtype: ~flow.models.TraceCosmosMetaDto
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TraceCosmosMetaDto"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_trace_session_metadata_async_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            template_url=self.get_trace_session_metadata_async.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('TraceCosmosMetaDto', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_trace_session_metadata_async.metadata = {'url': '/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/TraceSessions'}  # type: ignore


    @distributed_trace_async
    async def cleanup_trace_session_async(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        **kwargs: Any
    ) -> Any:
        """cleanup_trace_session_async.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: any, or the result of cls(response)
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_cleanup_trace_session_async_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            template_url=self.cleanup_trace_session_async.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('object', pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize('object', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    cleanup_trace_session_async.metadata = {'url': '/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/TraceSessions/cleanup'}  # type: ignore


    @distributed_trace_async
    async def poll_trace_session_status(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        operation_id: str,
        operation_type: str,
        **kwargs: Any
    ) -> str:
        """poll_trace_session_status.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param operation_id:
        :type operation_id: str
        :param operation_type:
        :type operation_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[str]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_poll_trace_session_status_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            operation_id=operation_id,
            operation_type=operation_type,
            template_url=self.poll_trace_session_status.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('str', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    poll_trace_session_status.metadata = {'url': '/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/TraceSessions/operation/{operationType}/{operationId}'}  # type: ignore


    @distributed_trace_async
    async def attach_cosmos_account(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        overwrite: Optional[bool] = False,
        body: Optional["_models.AttachCosmosRequest"] = None,
        **kwargs: Any
    ) -> Any:
        """attach_cosmos_account.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param overwrite:
        :type overwrite: bool
        :param body:
        :type body: ~flow.models.AttachCosmosRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: any, or the result of cls(response)
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'AttachCosmosRequest')
        else:
            _json = None

        request = build_attach_cosmos_account_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            content_type=content_type,
            json=_json,
            overwrite=overwrite,
            template_url=self.attach_cosmos_account.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('object', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    attach_cosmos_account.metadata = {'url': '/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/TraceSessions/attachDb'}  # type: ignore


    @distributed_trace_async
    async def get_cosmos_resource_token(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        container_name: str,
        acquire_write: Optional[bool] = False,
        **kwargs: Any
    ) -> str:
        """get_cosmos_resource_token.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param container_name:
        :type container_name: str
        :param acquire_write:
        :type acquire_write: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[str]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_cosmos_resource_token_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            container_name=container_name,
            acquire_write=acquire_write,
            template_url=self.get_cosmos_resource_token.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('str', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_cosmos_resource_token.metadata = {'url': '/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/TraceSessions/container/{containerName}/resourceToken'}  # type: ignore

