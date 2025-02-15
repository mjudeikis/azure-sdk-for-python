# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging
from typing import Optional
from .._utils import get_last_enqueued_event_properties
from .checkpoint_store import CheckpointStore

_LOGGER = logging.getLogger(__name__)


class PartitionContext(object):
    """Contains partition related context information.

    A `PartitionContext` instance will be passed to the event, error and initialization callbacks defined
    when calling `EventHubConsumerClient.receive()`.
    Users can call `update_checkpoint()` of this class to persist checkpoint data.
    """
    def __init__(self, fully_qualified_namespace, eventhub_name, consumer_group,
                 partition_id, checkpoint_store=None):
        # type: (str, str, str, str, Optional[CheckpointStore]) -> None
        self.fully_qualified_namespace = fully_qualified_namespace
        self.partition_id = partition_id
        self.eventhub_name = eventhub_name
        self.consumer_group = consumer_group
        self._checkpoint_store = checkpoint_store
        self._last_received_event = None

    @property
    def last_enqueued_event_properties(self):
        """The latest enqueued event information.

        This property will be updated each time an event is received if the receiver is created
        with `track_last_enqueued_event_properties` set to `True`.
        The properties dict includes following information of the last enqueued event:

            - `sequence_number` (int)
            - `offset` (str)
            - `enqueued_time` (UTC datetime.datetime)
            - `retrieval_time` (UTC datetime.datetime)

        :rtype: dict or None
        """
        if self._last_received_event:
            return get_last_enqueued_event_properties(self._last_received_event)
        return None

    def update_checkpoint(self, event):
        """Updates the receive checkpoint to the given events offset.

        This operation will only update a checkpoint if a `checkpoint_store` was provided during
        creation of the `EventHubConsumerClient`. Otherwise a warning will be logged.

        :param ~azure.eventhub.EventData event: The EventData instance which contains the offset and
         sequence number information used for checkpoint.
        :rtype: None
        """
        if self._checkpoint_store:
            checkpoint = {
                'fully_qualified_namespace': self.fully_qualified_namespace,
                'eventhub_name': self.eventhub_name,
                'consumer_group': self.consumer_group,
                'partition_id': self.partition_id,
                'offset': event.offset,
                'sequence_number': event.sequence_number
            }
            self._checkpoint_store.update_checkpoint(checkpoint)
        else:
            _LOGGER.warning(
                "namespace %r, eventhub %r, consumer_group %r, partition_id %r "
                "update_checkpoint is called without checkpoint store. No checkpoint is updated.",
                self.fully_qualified_namespace, self.eventhub_name, self.consumer_group, self.partition_id)
