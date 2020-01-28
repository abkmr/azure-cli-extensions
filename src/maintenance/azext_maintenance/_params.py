# pylint: disable=line-too-long
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azure.cli.core.commands.parameters import (
    resource_group_name_type,
    get_location_type,
    get_resource_name_completion_list
)

from knack.log import get_logger

from ._constants import (
    MAINTENANCE_RESOURCE_TYPE
)


logger = get_logger(__name__)


def load_arguments(self, _):
    with self.argument_context('maintenance configuration') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type)
        c.argument('location',
                   arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('resource_name', options_list=['--name', '-n'],
                   completer=get_resource_name_completion_list(MAINTENANCE_RESOURCE_TYPE),
                   help='Name of resource.')



