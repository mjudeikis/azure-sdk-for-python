# -- coding: utf-8 --
#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import pytest
import time
import json
import sys

from azure.eventhub import EventData, TransportType
from azure.eventhub import EventHubProducerClient


@pytest.mark.liveTest
def test_send_with_partition_key(connstr_receivers):
    connection_str, receivers = connstr_receivers
    client = EventHubProducerClient.from_connection_string(connection_str)
    with client:
        data_val = 0
        for partition in [b"a", b"b", b"c", b"d", b"e", b"f"]:
            partition_key = b"test_partition_" + partition
            for i in range(50):
                batch = client.create_batch(partition_key=partition_key)
                batch.add(EventData(str(data_val)))
                data_val += 1
                client.send_batch(batch)

    found_partition_keys = {}
    for index, partition in enumerate(receivers):
        received = partition.receive_message_batch(timeout=5000)
        for message in received:
            try:
                event_data = EventData._from_message(message)
                existing = found_partition_keys[event_data.partition_key]
                assert existing == index
            except KeyError:
                found_partition_keys[event_data.partition_key] = index


@pytest.mark.liveTest
def test_send_and_receive_large_body_size(connstr_receivers):
    if sys.platform.startswith('darwin'):
        pytest.skip("Skipping on OSX - open issue regarding message size")
    connection_str, receivers = connstr_receivers
    client = EventHubProducerClient.from_connection_string(connection_str)
    with client:
        payload = 250 * 1024
        batch = client.create_batch()
        batch.add(EventData("A" * payload))
        client.send_batch(batch)

    received = []
    for r in receivers:
        received.extend([EventData._from_message(x) for x in r.receive_message_batch(timeout=10000)])

    assert len(received) == 1
    assert len(list(received[0].body)[0]) == payload


@pytest.mark.parametrize("payload",
                         [b"", b"A single event"])
@pytest.mark.liveTest
def test_send_and_receive_small_body(connstr_receivers, payload):
    connection_str, receivers = connstr_receivers
    client = EventHubProducerClient.from_connection_string(connection_str)
    with client:
        batch = client.create_batch()
        batch.add(EventData(payload))
        client.send_batch(batch)
    received = []
    for r in receivers:
        received.extend([EventData._from_message(x) for x in r.receive_message_batch(timeout=5000)])

    assert len(received) == 1
    assert list(received[0].body)[0] == payload


@pytest.mark.liveTest
def test_send_partition(connstr_receivers):
    connection_str, receivers = connstr_receivers
    client = EventHubProducerClient.from_connection_string(connection_str)
    with client:
        batch = client.create_batch(partition_id="1")
        batch.add(EventData(b"Data"))
        client.send_batch(batch)

    partition_0 = receivers[0].receive_message_batch(timeout=5000)
    assert len(partition_0) == 0
    partition_1 = receivers[1].receive_message_batch(timeout=5000)
    assert len(partition_1) == 1


@pytest.mark.liveTest
def test_send_non_ascii(connstr_receivers):
    connection_str, receivers = connstr_receivers
    client = EventHubProducerClient.from_connection_string(connection_str)
    with client:
        batch = client.create_batch(partition_id="0")
        batch.add(EventData(u"é,è,à,ù,â,ê,î,ô,û"))
        batch.add(EventData(json.dumps({"foo": u"漢字"})))
        client.send_batch(batch)
    time.sleep(1)
    partition_0 = [EventData._from_message(x) for x in receivers[0].receive_message_batch(timeout=5000)]
    assert len(partition_0) == 2
    assert partition_0[0].body_as_str() == u"é,è,à,ù,â,ê,î,ô,û"
    assert partition_0[1].body_as_json() == {"foo": u"漢字"}


@pytest.mark.liveTest
def test_send_multiple_partitions_with_app_prop(connstr_receivers):
    connection_str, receivers = connstr_receivers
    app_prop_key = "raw_prop"
    app_prop_value = "raw_value"
    app_prop = {app_prop_key: app_prop_value}
    client = EventHubProducerClient.from_connection_string(connection_str)
    with client:
        ed0 = EventData(b"Message 0")
        ed0.properties = app_prop
        batch = client.create_batch(partition_id="0")
        batch.add(ed0)
        client.send_batch(batch)

        ed1 = EventData(b"Message 1")
        ed1.properties = app_prop
        batch = client.create_batch(partition_id="1")
        batch.add(ed1)
        client.send_batch(batch)

    partition_0 = [EventData._from_message(x) for x in receivers[0].receive_message_batch(timeout=5000)]
    assert len(partition_0) == 1
    assert partition_0[0].properties[b"raw_prop"] == b"raw_value"
    partition_1 = [EventData._from_message(x) for x in receivers[1].receive_message_batch(timeout=5000)]
    assert len(partition_1) == 1
    assert partition_1[0].properties[b"raw_prop"] == b"raw_value"


@pytest.mark.liveTest
def test_send_over_websocket_sync(connstr_receivers):
    connection_str, receivers = connstr_receivers
    client = EventHubProducerClient.from_connection_string(connection_str, transport_type=TransportType.AmqpOverWebsocket)

    with client:
        batch = client.create_batch()
        for i in range(20):
            batch.add(EventData("Event Number {}".format(i)))
        client.send_batch(batch)

    time.sleep(1)
    received = []
    for r in receivers:
        received.extend(r.receive_message_batch(timeout=5000))
    assert len(received) == 20


@pytest.mark.liveTest
def test_send_with_create_event_batch_with_app_prop_sync(connstr_receivers):
    connection_str, receivers = connstr_receivers
    app_prop_key = "raw_prop"
    app_prop_value = "raw_value"
    app_prop = {app_prop_key: app_prop_value}
    client = EventHubProducerClient.from_connection_string(connection_str, transport_type=TransportType.AmqpOverWebsocket)
    with client:
        event_data_batch = client.create_batch(max_size_in_bytes=100000)
        while True:
            try:
                ed = EventData('A single event data')
                ed.properties = app_prop
                event_data_batch.add(ed)
            except ValueError:
                break
        client.send_batch(event_data_batch)
        received = []
        for r in receivers:
            received.extend(r.receive_message_batch(timeout=5000))
        assert len(received) > 1
        assert EventData._from_message(received[0]).properties[b"raw_prop"] == b"raw_value"
