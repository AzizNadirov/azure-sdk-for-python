# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models
from ._configuration import AzureMachineLearningWorkspacesConfiguration
from .operations import BatchDeploymentsOperations, BatchEndpointsOperations, CapabilityHostsOperations, CodeContainersOperations, CodeVersionsOperations, ComponentContainersOperations, ComponentVersionsOperations, ComputeOperations, ConnectionOperations, ConnectionRaiBlocklistItemOperations, ConnectionRaiBlocklistItemsOperations, ConnectionRaiBlocklistOperations, ConnectionRaiBlocklistsOperations, ConnectionRaiPoliciesOperations, ConnectionRaiPolicyOperations, DataContainersOperations, DataVersionsOperations, DatastoresOperations, EndpointDeploymentOperations, EndpointOperations, EnvironmentContainersOperations, EnvironmentVersionsOperations, FeaturesOperations, FeaturesetContainersOperations, FeaturesetVersionsOperations, FeaturestoreEntityContainersOperations, FeaturestoreEntityVersionsOperations, InferenceEndpointsOperations, InferenceGroupsOperations, InferencePoolsOperations, JobsOperations, ManagedNetworkProvisionsOperations, ManagedNetworkSettingsRuleOperations, MarketplaceSubscriptionsOperations, ModelContainersOperations, ModelVersionsOperations, OnlineDeploymentsOperations, OnlineEndpointsOperations, Operations, PTUQuotaOperations, PrivateEndpointConnectionsOperations, PrivateLinkResourcesOperations, QuotasOperations, RaiPoliciesOperations, RaiPolicyOperations, RegistriesOperations, RegistryCodeContainersOperations, RegistryCodeVersionsOperations, RegistryComponentContainersOperations, RegistryComponentVersionsOperations, RegistryDataContainersOperations, RegistryDataReferencesOperations, RegistryDataVersionsOperations, RegistryEnvironmentContainersOperations, RegistryEnvironmentVersionsOperations, RegistryModelContainersOperations, RegistryModelVersionsOperations, SchedulesOperations, ServerlessEndpointsOperations, UsagesOperations, VirtualMachineSizesOperations, WorkspaceConnectionsOperations, WorkspaceFeaturesOperations, WorkspacesOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

class AzureMachineLearningWorkspaces:    # pylint: disable=too-many-instance-attributes
    """These APIs allow end users to operate on Azure Machine Learning Workspace resources.

    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.machinelearningservices.aio.operations.UsagesOperations
    :ivar virtual_machine_sizes: VirtualMachineSizesOperations operations
    :vartype virtual_machine_sizes:
     azure.mgmt.machinelearningservices.aio.operations.VirtualMachineSizesOperations
    :ivar quotas: QuotasOperations operations
    :vartype quotas: azure.mgmt.machinelearningservices.aio.operations.QuotasOperations
    :ivar compute: ComputeOperations operations
    :vartype compute: azure.mgmt.machinelearningservices.aio.operations.ComputeOperations
    :ivar registries: RegistriesOperations operations
    :vartype registries: azure.mgmt.machinelearningservices.aio.operations.RegistriesOperations
    :ivar workspace_features: WorkspaceFeaturesOperations operations
    :vartype workspace_features:
     azure.mgmt.machinelearningservices.aio.operations.WorkspaceFeaturesOperations
    :ivar ptu_quota: PTUQuotaOperations operations
    :vartype ptu_quota: azure.mgmt.machinelearningservices.aio.operations.PTUQuotaOperations
    :ivar registry_code_containers: RegistryCodeContainersOperations operations
    :vartype registry_code_containers:
     azure.mgmt.machinelearningservices.aio.operations.RegistryCodeContainersOperations
    :ivar registry_code_versions: RegistryCodeVersionsOperations operations
    :vartype registry_code_versions:
     azure.mgmt.machinelearningservices.aio.operations.RegistryCodeVersionsOperations
    :ivar registry_component_containers: RegistryComponentContainersOperations operations
    :vartype registry_component_containers:
     azure.mgmt.machinelearningservices.aio.operations.RegistryComponentContainersOperations
    :ivar registry_component_versions: RegistryComponentVersionsOperations operations
    :vartype registry_component_versions:
     azure.mgmt.machinelearningservices.aio.operations.RegistryComponentVersionsOperations
    :ivar registry_data_containers: RegistryDataContainersOperations operations
    :vartype registry_data_containers:
     azure.mgmt.machinelearningservices.aio.operations.RegistryDataContainersOperations
    :ivar registry_data_versions: RegistryDataVersionsOperations operations
    :vartype registry_data_versions:
     azure.mgmt.machinelearningservices.aio.operations.RegistryDataVersionsOperations
    :ivar registry_data_references: RegistryDataReferencesOperations operations
    :vartype registry_data_references:
     azure.mgmt.machinelearningservices.aio.operations.RegistryDataReferencesOperations
    :ivar registry_environment_containers: RegistryEnvironmentContainersOperations operations
    :vartype registry_environment_containers:
     azure.mgmt.machinelearningservices.aio.operations.RegistryEnvironmentContainersOperations
    :ivar registry_environment_versions: RegistryEnvironmentVersionsOperations operations
    :vartype registry_environment_versions:
     azure.mgmt.machinelearningservices.aio.operations.RegistryEnvironmentVersionsOperations
    :ivar registry_model_containers: RegistryModelContainersOperations operations
    :vartype registry_model_containers:
     azure.mgmt.machinelearningservices.aio.operations.RegistryModelContainersOperations
    :ivar registry_model_versions: RegistryModelVersionsOperations operations
    :vartype registry_model_versions:
     azure.mgmt.machinelearningservices.aio.operations.RegistryModelVersionsOperations
    :ivar batch_endpoints: BatchEndpointsOperations operations
    :vartype batch_endpoints:
     azure.mgmt.machinelearningservices.aio.operations.BatchEndpointsOperations
    :ivar batch_deployments: BatchDeploymentsOperations operations
    :vartype batch_deployments:
     azure.mgmt.machinelearningservices.aio.operations.BatchDeploymentsOperations
    :ivar capability_hosts: CapabilityHostsOperations operations
    :vartype capability_hosts:
     azure.mgmt.machinelearningservices.aio.operations.CapabilityHostsOperations
    :ivar code_containers: CodeContainersOperations operations
    :vartype code_containers:
     azure.mgmt.machinelearningservices.aio.operations.CodeContainersOperations
    :ivar code_versions: CodeVersionsOperations operations
    :vartype code_versions:
     azure.mgmt.machinelearningservices.aio.operations.CodeVersionsOperations
    :ivar component_containers: ComponentContainersOperations operations
    :vartype component_containers:
     azure.mgmt.machinelearningservices.aio.operations.ComponentContainersOperations
    :ivar component_versions: ComponentVersionsOperations operations
    :vartype component_versions:
     azure.mgmt.machinelearningservices.aio.operations.ComponentVersionsOperations
    :ivar data_containers: DataContainersOperations operations
    :vartype data_containers:
     azure.mgmt.machinelearningservices.aio.operations.DataContainersOperations
    :ivar data_versions: DataVersionsOperations operations
    :vartype data_versions:
     azure.mgmt.machinelearningservices.aio.operations.DataVersionsOperations
    :ivar datastores: DatastoresOperations operations
    :vartype datastores: azure.mgmt.machinelearningservices.aio.operations.DatastoresOperations
    :ivar environment_containers: EnvironmentContainersOperations operations
    :vartype environment_containers:
     azure.mgmt.machinelearningservices.aio.operations.EnvironmentContainersOperations
    :ivar environment_versions: EnvironmentVersionsOperations operations
    :vartype environment_versions:
     azure.mgmt.machinelearningservices.aio.operations.EnvironmentVersionsOperations
    :ivar featureset_containers: FeaturesetContainersOperations operations
    :vartype featureset_containers:
     azure.mgmt.machinelearningservices.aio.operations.FeaturesetContainersOperations
    :ivar features: FeaturesOperations operations
    :vartype features: azure.mgmt.machinelearningservices.aio.operations.FeaturesOperations
    :ivar featureset_versions: FeaturesetVersionsOperations operations
    :vartype featureset_versions:
     azure.mgmt.machinelearningservices.aio.operations.FeaturesetVersionsOperations
    :ivar featurestore_entity_containers: FeaturestoreEntityContainersOperations operations
    :vartype featurestore_entity_containers:
     azure.mgmt.machinelearningservices.aio.operations.FeaturestoreEntityContainersOperations
    :ivar featurestore_entity_versions: FeaturestoreEntityVersionsOperations operations
    :vartype featurestore_entity_versions:
     azure.mgmt.machinelearningservices.aio.operations.FeaturestoreEntityVersionsOperations
    :ivar inference_pools: InferencePoolsOperations operations
    :vartype inference_pools:
     azure.mgmt.machinelearningservices.aio.operations.InferencePoolsOperations
    :ivar inference_endpoints: InferenceEndpointsOperations operations
    :vartype inference_endpoints:
     azure.mgmt.machinelearningservices.aio.operations.InferenceEndpointsOperations
    :ivar inference_groups: InferenceGroupsOperations operations
    :vartype inference_groups:
     azure.mgmt.machinelearningservices.aio.operations.InferenceGroupsOperations
    :ivar jobs: JobsOperations operations
    :vartype jobs: azure.mgmt.machinelearningservices.aio.operations.JobsOperations
    :ivar marketplace_subscriptions: MarketplaceSubscriptionsOperations operations
    :vartype marketplace_subscriptions:
     azure.mgmt.machinelearningservices.aio.operations.MarketplaceSubscriptionsOperations
    :ivar model_containers: ModelContainersOperations operations
    :vartype model_containers:
     azure.mgmt.machinelearningservices.aio.operations.ModelContainersOperations
    :ivar model_versions: ModelVersionsOperations operations
    :vartype model_versions:
     azure.mgmt.machinelearningservices.aio.operations.ModelVersionsOperations
    :ivar online_endpoints: OnlineEndpointsOperations operations
    :vartype online_endpoints:
     azure.mgmt.machinelearningservices.aio.operations.OnlineEndpointsOperations
    :ivar online_deployments: OnlineDeploymentsOperations operations
    :vartype online_deployments:
     azure.mgmt.machinelearningservices.aio.operations.OnlineDeploymentsOperations
    :ivar schedules: SchedulesOperations operations
    :vartype schedules: azure.mgmt.machinelearningservices.aio.operations.SchedulesOperations
    :ivar serverless_endpoints: ServerlessEndpointsOperations operations
    :vartype serverless_endpoints:
     azure.mgmt.machinelearningservices.aio.operations.ServerlessEndpointsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.machinelearningservices.aio.operations.Operations
    :ivar workspaces: WorkspacesOperations operations
    :vartype workspaces: azure.mgmt.machinelearningservices.aio.operations.WorkspacesOperations
    :ivar workspace_connections: WorkspaceConnectionsOperations operations
    :vartype workspace_connections:
     azure.mgmt.machinelearningservices.aio.operations.WorkspaceConnectionsOperations
    :ivar connection: ConnectionOperations operations
    :vartype connection: azure.mgmt.machinelearningservices.aio.operations.ConnectionOperations
    :ivar connection_rai_blocklists: ConnectionRaiBlocklistsOperations operations
    :vartype connection_rai_blocklists:
     azure.mgmt.machinelearningservices.aio.operations.ConnectionRaiBlocklistsOperations
    :ivar connection_rai_blocklist: ConnectionRaiBlocklistOperations operations
    :vartype connection_rai_blocklist:
     azure.mgmt.machinelearningservices.aio.operations.ConnectionRaiBlocklistOperations
    :ivar connection_rai_blocklist_item: ConnectionRaiBlocklistItemOperations operations
    :vartype connection_rai_blocklist_item:
     azure.mgmt.machinelearningservices.aio.operations.ConnectionRaiBlocklistItemOperations
    :ivar connection_rai_blocklist_items: ConnectionRaiBlocklistItemsOperations operations
    :vartype connection_rai_blocklist_items:
     azure.mgmt.machinelearningservices.aio.operations.ConnectionRaiBlocklistItemsOperations
    :ivar connection_rai_policies: ConnectionRaiPoliciesOperations operations
    :vartype connection_rai_policies:
     azure.mgmt.machinelearningservices.aio.operations.ConnectionRaiPoliciesOperations
    :ivar connection_rai_policy: ConnectionRaiPolicyOperations operations
    :vartype connection_rai_policy:
     azure.mgmt.machinelearningservices.aio.operations.ConnectionRaiPolicyOperations
    :ivar endpoint_deployment: EndpointDeploymentOperations operations
    :vartype endpoint_deployment:
     azure.mgmt.machinelearningservices.aio.operations.EndpointDeploymentOperations
    :ivar endpoint: EndpointOperations operations
    :vartype endpoint: azure.mgmt.machinelearningservices.aio.operations.EndpointOperations
    :ivar rai_policies: RaiPoliciesOperations operations
    :vartype rai_policies: azure.mgmt.machinelearningservices.aio.operations.RaiPoliciesOperations
    :ivar rai_policy: RaiPolicyOperations operations
    :vartype rai_policy: azure.mgmt.machinelearningservices.aio.operations.RaiPolicyOperations
    :ivar managed_network_settings_rule: ManagedNetworkSettingsRuleOperations operations
    :vartype managed_network_settings_rule:
     azure.mgmt.machinelearningservices.aio.operations.ManagedNetworkSettingsRuleOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.machinelearningservices.aio.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.machinelearningservices.aio.operations.PrivateLinkResourcesOperations
    :ivar managed_network_provisions: ManagedNetworkProvisionsOperations operations
    :vartype managed_network_provisions:
     azure.mgmt.machinelearningservices.aio.operations.ManagedNetworkProvisionsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param base_url: Service URL. Default value is 'https://management.azure.com'.
    :type base_url: str
    :keyword api_version: Api Version. The default value is "2025-01-01-preview". Note that
     overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = AzureMachineLearningWorkspacesConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.usages = UsagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_sizes = VirtualMachineSizesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.quotas = QuotasOperations(self._client, self._config, self._serialize, self._deserialize)
        self.compute = ComputeOperations(self._client, self._config, self._serialize, self._deserialize)
        self.registries = RegistriesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.workspace_features = WorkspaceFeaturesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.ptu_quota = PTUQuotaOperations(self._client, self._config, self._serialize, self._deserialize)
        self.registry_code_containers = RegistryCodeContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.registry_code_versions = RegistryCodeVersionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.registry_component_containers = RegistryComponentContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.registry_component_versions = RegistryComponentVersionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.registry_data_containers = RegistryDataContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.registry_data_versions = RegistryDataVersionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.registry_data_references = RegistryDataReferencesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.registry_environment_containers = RegistryEnvironmentContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.registry_environment_versions = RegistryEnvironmentVersionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.registry_model_containers = RegistryModelContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.registry_model_versions = RegistryModelVersionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.batch_endpoints = BatchEndpointsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.batch_deployments = BatchDeploymentsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.capability_hosts = CapabilityHostsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.code_containers = CodeContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.code_versions = CodeVersionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.component_containers = ComponentContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.component_versions = ComponentVersionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.data_containers = DataContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.data_versions = DataVersionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.datastores = DatastoresOperations(self._client, self._config, self._serialize, self._deserialize)
        self.environment_containers = EnvironmentContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.environment_versions = EnvironmentVersionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.featureset_containers = FeaturesetContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.features = FeaturesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.featureset_versions = FeaturesetVersionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.featurestore_entity_containers = FeaturestoreEntityContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.featurestore_entity_versions = FeaturestoreEntityVersionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.inference_pools = InferencePoolsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.inference_endpoints = InferenceEndpointsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.inference_groups = InferenceGroupsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.marketplace_subscriptions = MarketplaceSubscriptionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.model_containers = ModelContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.model_versions = ModelVersionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.online_endpoints = OnlineEndpointsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.online_deployments = OnlineDeploymentsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.schedules = SchedulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.serverless_endpoints = ServerlessEndpointsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.workspace_connections = WorkspaceConnectionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.connection = ConnectionOperations(self._client, self._config, self._serialize, self._deserialize)
        self.connection_rai_blocklists = ConnectionRaiBlocklistsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.connection_rai_blocklist = ConnectionRaiBlocklistOperations(self._client, self._config, self._serialize, self._deserialize)
        self.connection_rai_blocklist_item = ConnectionRaiBlocklistItemOperations(self._client, self._config, self._serialize, self._deserialize)
        self.connection_rai_blocklist_items = ConnectionRaiBlocklistItemsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.connection_rai_policies = ConnectionRaiPoliciesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.connection_rai_policy = ConnectionRaiPolicyOperations(self._client, self._config, self._serialize, self._deserialize)
        self.endpoint_deployment = EndpointDeploymentOperations(self._client, self._config, self._serialize, self._deserialize)
        self.endpoint = EndpointOperations(self._client, self._config, self._serialize, self._deserialize)
        self.rai_policies = RaiPoliciesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.rai_policy = RaiPolicyOperations(self._client, self._config, self._serialize, self._deserialize)
        self.managed_network_settings_rule = ManagedNetworkSettingsRuleOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.managed_network_provisions = ManagedNetworkProvisionsOperations(self._client, self._config, self._serialize, self._deserialize)


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AzureMachineLearningWorkspaces":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
