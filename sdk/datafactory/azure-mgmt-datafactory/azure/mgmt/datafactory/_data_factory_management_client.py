# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING
from typing_extensions import Self

from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient
from azure.mgmt.core.policies import ARMAutoResourceProviderRegistrationPolicy

from . import models as _models
from ._configuration import DataFactoryManagementClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    ActivityRunsOperations,
    ChangeDataCaptureOperations,
    CredentialOperationsOperations,
    DataFlowDebugSessionOperations,
    DataFlowsOperations,
    DatasetsOperations,
    ExposureControlOperations,
    FactoriesOperations,
    GlobalParametersOperations,
    IntegrationRuntimeNodesOperations,
    IntegrationRuntimeObjectMetadataOperations,
    IntegrationRuntimesOperations,
    LinkedServicesOperations,
    ManagedPrivateEndpointsOperations,
    ManagedVirtualNetworksOperations,
    Operations,
    PipelineRunsOperations,
    PipelinesOperations,
    PrivateEndPointConnectionsOperations,
    PrivateEndpointConnectionOperations,
    PrivateLinkResourcesOperations,
    TriggerRunsOperations,
    TriggersOperations,
)

if TYPE_CHECKING:
    from azure.core.credentials import TokenCredential


class DataFactoryManagementClient:  # pylint: disable=too-many-instance-attributes
    """The Azure Data Factory V2 management API provides a RESTful set of web services that interact
    with Azure Data Factory V2 services.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.datafactory.operations.Operations
    :ivar factories: FactoriesOperations operations
    :vartype factories: azure.mgmt.datafactory.operations.FactoriesOperations
    :ivar exposure_control: ExposureControlOperations operations
    :vartype exposure_control: azure.mgmt.datafactory.operations.ExposureControlOperations
    :ivar integration_runtimes: IntegrationRuntimesOperations operations
    :vartype integration_runtimes: azure.mgmt.datafactory.operations.IntegrationRuntimesOperations
    :ivar integration_runtime_object_metadata: IntegrationRuntimeObjectMetadataOperations
     operations
    :vartype integration_runtime_object_metadata:
     azure.mgmt.datafactory.operations.IntegrationRuntimeObjectMetadataOperations
    :ivar integration_runtime_nodes: IntegrationRuntimeNodesOperations operations
    :vartype integration_runtime_nodes:
     azure.mgmt.datafactory.operations.IntegrationRuntimeNodesOperations
    :ivar linked_services: LinkedServicesOperations operations
    :vartype linked_services: azure.mgmt.datafactory.operations.LinkedServicesOperations
    :ivar datasets: DatasetsOperations operations
    :vartype datasets: azure.mgmt.datafactory.operations.DatasetsOperations
    :ivar pipelines: PipelinesOperations operations
    :vartype pipelines: azure.mgmt.datafactory.operations.PipelinesOperations
    :ivar pipeline_runs: PipelineRunsOperations operations
    :vartype pipeline_runs: azure.mgmt.datafactory.operations.PipelineRunsOperations
    :ivar activity_runs: ActivityRunsOperations operations
    :vartype activity_runs: azure.mgmt.datafactory.operations.ActivityRunsOperations
    :ivar triggers: TriggersOperations operations
    :vartype triggers: azure.mgmt.datafactory.operations.TriggersOperations
    :ivar trigger_runs: TriggerRunsOperations operations
    :vartype trigger_runs: azure.mgmt.datafactory.operations.TriggerRunsOperations
    :ivar data_flows: DataFlowsOperations operations
    :vartype data_flows: azure.mgmt.datafactory.operations.DataFlowsOperations
    :ivar data_flow_debug_session: DataFlowDebugSessionOperations operations
    :vartype data_flow_debug_session:
     azure.mgmt.datafactory.operations.DataFlowDebugSessionOperations
    :ivar managed_virtual_networks: ManagedVirtualNetworksOperations operations
    :vartype managed_virtual_networks:
     azure.mgmt.datafactory.operations.ManagedVirtualNetworksOperations
    :ivar managed_private_endpoints: ManagedPrivateEndpointsOperations operations
    :vartype managed_private_endpoints:
     azure.mgmt.datafactory.operations.ManagedPrivateEndpointsOperations
    :ivar credential_operations: CredentialOperationsOperations operations
    :vartype credential_operations:
     azure.mgmt.datafactory.operations.CredentialOperationsOperations
    :ivar private_end_point_connections: PrivateEndPointConnectionsOperations operations
    :vartype private_end_point_connections:
     azure.mgmt.datafactory.operations.PrivateEndPointConnectionsOperations
    :ivar private_endpoint_connection: PrivateEndpointConnectionOperations operations
    :vartype private_endpoint_connection:
     azure.mgmt.datafactory.operations.PrivateEndpointConnectionOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.datafactory.operations.PrivateLinkResourcesOperations
    :ivar global_parameters: GlobalParametersOperations operations
    :vartype global_parameters: azure.mgmt.datafactory.operations.GlobalParametersOperations
    :ivar change_data_capture: ChangeDataCaptureOperations operations
    :vartype change_data_capture: azure.mgmt.datafactory.operations.ChangeDataCaptureOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The subscription identifier. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2018-06-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = DataFactoryManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                ARMAutoResourceProviderRegistrationPolicy(),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, policies=_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.factories = FactoriesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.exposure_control = ExposureControlOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.integration_runtimes = IntegrationRuntimesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.integration_runtime_object_metadata = IntegrationRuntimeObjectMetadataOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.integration_runtime_nodes = IntegrationRuntimeNodesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.linked_services = LinkedServicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.datasets = DatasetsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.pipelines = PipelinesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.pipeline_runs = PipelineRunsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.activity_runs = ActivityRunsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.triggers = TriggersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.trigger_runs = TriggerRunsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.data_flows = DataFlowsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.data_flow_debug_session = DataFlowDebugSessionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.managed_virtual_networks = ManagedVirtualNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.managed_private_endpoints = ManagedPrivateEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.credential_operations = CredentialOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_end_point_connections = PrivateEndPointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_endpoint_connection = PrivateEndpointConnectionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.global_parameters = GlobalParametersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.change_data_capture = ChangeDataCaptureOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
