.. :changelog:

Release History
===============

0.5.0 (2019-11-11)
++++++++++++++++++

**Features**

- Model ClusterUpdate has a new parameter key_vault_properties
- Model ClusterUpdate has a new parameter identity
- Model Cluster has a new parameter key_vault_properties
- Model Cluster has a new parameter identity
- Added operation ClustersOperations.detach_follower_databases
- Added operation ClustersOperations.list_follower_databases
- Added operation group AttachedDatabaseConfigurationsOperations

**Breaking changes**

- Operation DatabasesOperations.check_name_availability has a new signature
- Model Database no longer has parameter soft_delete_period
- Model Database no longer has parameter hot_cache_period
- Model Database no longer has parameter statistics
- Model Database no longer has parameter provisioning_state
- Model Database has a new required parameter kind

0.4.0 (2019-08-27)
++++++++++++++++++

**Features**

- Model Cluster has a new parameter enable_disk_encryption
- Model Cluster has a new parameter zones
- Model Cluster has a new parameter optimized_autoscale
- Model Cluster has a new parameter virtual_network_configuration
- Model Cluster has a new parameter enable_streaming_ingest
- Model EventHubDataConnection has a new parameter event_system_properties
- Model CheckNameResult has a new parameter reason
- Model DatabasePrincipal has a new parameter tenant_name
- Model ClusterUpdate has a new parameter enable_disk_encryption
- Model ClusterUpdate has a new parameter optimized_autoscale
- Model ClusterUpdate has a new parameter enable_streaming_ingest
- Model ClusterUpdate has a new parameter virtual_network_configuration
- Added operation DataConnectionsOperations.check_name_availability

**General breaking changes**  

This version uses a next-generation code generator that *might* introduce breaking changes if from some import.
In summary, some modules were incorrectly visible/importable and have been renamed. This fixed several issues caused by usage of classes that were not supposed to be used in the first place.

- KustoManagementClient cannot be imported from `azure.mgmt.kusto.kusto_management_client` anymore (import from `azure.mgmt.kusto` works like before)
- KustoManagementClientConfiguration import has been moved from `azure.mgmt.kusto.kusto_management_client` to `azure.mgmt.kusto`
- A model `MyClass` from a "models" sub-module cannot be imported anymore using `azure.mgmt.kusto.models.my_class` (import from `azure.mgmt.kusto.models` works like before)
- An operation class `MyClassOperations` from an `operations` sub-module cannot be imported anymore using `azure.mgmt.kusto.operations.my_class_operations` (import from `azure.mgmt.kusto.operations` works like before)
        
Last but not least, HTTP connection pooling is now enabled by default. You should always use a client as a context manager, or call close(), or use no more than one client per process.

0.3.0 (2019-02-06)
++++++++++++++++++

**Features**

- Model DatabaseUpdate has a new parameter hot_cache_period
- Model DatabaseUpdate has a new parameter soft_delete_period
- Model Database has a new parameter hot_cache_period
- Model Database has a new parameter soft_delete_period
- Added operation group DataConnectionsOperations

**Breaking changes**

- Model DatabaseUpdate no longer has parameter hot_cache_period_in_days
- Model DatabaseUpdate no longer has parameter etag
- Model DatabaseUpdate no longer has parameter soft_delete_period_in_days
- Model Database no longer has parameter tags
- Model Database no longer has parameter etag
- Model Database no longer has parameter hot_cache_period_in_days
- Model Database no longer has parameter soft_delete_period_in_days
- Model Cluster no longer has parameter etag
- Model ClusterUpdate no longer has parameter etag
- Removed operation group EventHubConnectionsOperations

0.2.0 (2018-11-27)
++++++++++++++++++

**Features**

- Model Cluster has a new parameter uri
- Model Cluster has a new parameter state
- Model Cluster has a new parameter data_ingestion_uri
- Model Cluster has a new parameter trusted_external_tenants
- Model DatabaseUpdate has a new parameter etag
- Model DatabaseUpdate has a new parameter statistics
- Model DatabaseUpdate has a new parameter hot_cache_period_in_days
- Model Database has a new parameter statistics
- Model Database has a new parameter hot_cache_period_in_days
- Model ClusterUpdate has a new parameter uri
- Model ClusterUpdate has a new parameter etag
- Model ClusterUpdate has a new parameter state
- Model ClusterUpdate has a new parameter sku
- Model ClusterUpdate has a new parameter tags
- Model ClusterUpdate has a new parameter data_ingestion_uri
- Model ClusterUpdate has a new parameter trusted_external_tenants
- Added operation DatabasesOperations.list_principals
- Added operation DatabasesOperations.check_name_availability
- Added operation DatabasesOperations.add_principals
- Added operation DatabasesOperations.remove_principals
- Added operation ClustersOperations.list_skus
- Added operation ClustersOperations.list_skus_by_resource
- Added operation ClustersOperations.start
- Added operation ClustersOperations.check_name_availability
- Added operation ClustersOperations.stop
- Added operation group EventHubConnectionsOperations

**Breaking changes**

- Operation DatabasesOperations.update has a new signature
- Operation ClustersOperations.update has a new signature
- Operation DatabasesOperations.update has a new signature
- Operation ClustersOperations.create_or_update has a new signature
- Model Cluster has a new required parameter sku

0.1.0 (2018-08-09)
++++++++++++++++++

* Initial Release
