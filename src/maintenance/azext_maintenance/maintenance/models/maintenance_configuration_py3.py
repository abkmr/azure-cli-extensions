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

from .resource_py3 import Resource


class MaintenanceConfiguration(Resource):
    """Maintenance configuration record type.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified identifier of the resource
    :vartype id: str
    :ivar name: Name of the resource
    :vartype name: str
    :ivar type: Type of the resource
    :vartype type: str
    :param location: Gets or sets location of the resource
    :type location: str
    :param tags: Gets or sets tags of the resource
    :type tags: dict[str, str]
    :param namespace: Gets or sets namespace of the resource
    :type namespace: str
    :param extension_properties: Gets or sets extensionProperties of the
     maintenanceConfiguration
    :type extension_properties: dict[str, str]
    :param maintenance_scope: Gets or sets maintenanceScope of the
     configuration. Possible values include: 'All', 'Host', 'Resource',
     'InResource'
    :type maintenance_scope: str or
     ~azure.mgmt.maintenance.models.MaintenanceScope
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'namespace': {'key': 'properties.namespace', 'type': 'str'},
        'extension_properties': {'key': 'properties.extensionProperties', 'type': '{str}'},
        'maintenance_scope': {'key': 'properties.maintenanceScope', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, tags=None, namespace: str=None, extension_properties=None, maintenance_scope=None, **kwargs) -> None:
        super(MaintenanceConfiguration, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.namespace = namespace
        self.extension_properties = extension_properties
        self.maintenance_scope = maintenance_scope
