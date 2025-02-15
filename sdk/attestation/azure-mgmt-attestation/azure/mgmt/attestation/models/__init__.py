# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AttestationProvider
    from ._models_py3 import AttestationProviderListResult
    from ._models_py3 import AttestationServiceCreationParams
    from ._models_py3 import AzureEntityResource
    from ._models_py3 import JSONWebKey
    from ._models_py3 import JSONWebKeySet
    from ._models_py3 import OperationList
    from ._models_py3 import OperationsDefinition
    from ._models_py3 import OperationsDisplayDefinition
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import TrackedResource
except (SyntaxError, ImportError):
    from ._models import AttestationProvider
    from ._models import AttestationProviderListResult
    from ._models import AttestationServiceCreationParams
    from ._models import AzureEntityResource
    from ._models import JSONWebKey
    from ._models import JSONWebKeySet
    from ._models import OperationList
    from ._models import OperationsDefinition
    from ._models import OperationsDisplayDefinition
    from ._models import ProxyResource
    from ._models import Resource
    from ._models import TrackedResource
from ._attestation_management_client_enums import (
    AttestationServiceStatus,
)

__all__ = [
    'AttestationProvider',
    'AttestationProviderListResult',
    'AttestationServiceCreationParams',
    'AzureEntityResource',
    'JSONWebKey',
    'JSONWebKeySet',
    'OperationList',
    'OperationsDefinition',
    'OperationsDisplayDefinition',
    'ProxyResource',
    'Resource',
    'TrackedResource',
    'AttestationServiceStatus',
]
