#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import pytest
from azure.eventhub import EventHubSharedKeyCredential
from azure.eventhub import EventHubConsumerClient


@pytest.mark.liveTest
def test_get_properties(live_eventhub):
    client = EventHubConsumerClient(live_eventhub['hostname'], live_eventhub['event_hub'], '$default',
                            EventHubSharedKeyCredential(live_eventhub['key_name'], live_eventhub['access_key']))
    properties = client.get_eventhub_properties()
    assert properties['eventhub_name'] == live_eventhub['event_hub'] and properties['partition_ids'] == ['0', '1']
    client.close()


@pytest.mark.liveTest
def test_get_partition_ids(live_eventhub):
    client = EventHubConsumerClient(live_eventhub['hostname'], live_eventhub['event_hub'], '$default',
                            EventHubSharedKeyCredential(live_eventhub['key_name'], live_eventhub['access_key']))
    partition_ids = client.get_partition_ids()
    assert partition_ids == ['0', '1']
    client.close()


@pytest.mark.liveTest
def test_get_partition_properties(live_eventhub):
    client = EventHubConsumerClient(live_eventhub['hostname'], live_eventhub['event_hub'], '$default',
                            EventHubSharedKeyCredential(live_eventhub['key_name'], live_eventhub['access_key']))
    properties = client.get_partition_properties('0')
    assert properties['eventhub_name'] == live_eventhub['event_hub'] \
        and properties['id'] == '0' \
        and 'beginning_sequence_number' in properties \
        and 'last_enqueued_sequence_number' in properties \
        and 'last_enqueued_offset' in properties \
        and 'last_enqueued_time_utc' in properties \
        and 'is_empty' in properties
    client.close()
