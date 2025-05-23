#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
Example to show streaming sending events with different options to an Event Hub.
"""

import time
import os

from azure.eventhub import EventHubProducerClient, EventData
from azure.identity import DefaultAzureCredential

FULLY_QUALIFIED_NAMESPACE = os.environ["EVENT_HUB_HOSTNAME"]
EVENTHUB_NAME = os.environ["EVENT_HUB_NAME"]


start_time = time.time()

producer = EventHubProducerClient(
    fully_qualified_namespace=FULLY_QUALIFIED_NAMESPACE,
    eventhub_name=EVENTHUB_NAME,
    credential=DefaultAzureCredential(),
)
to_send_message_cnt = 500
bytes_per_message = 256

with producer:
    event_data_batch = producer.create_batch()
    for i in range(to_send_message_cnt):
        event_data = EventData("D" * bytes_per_message)
        try:
            event_data_batch.add(event_data)
        except ValueError:
            producer.send_batch(event_data_batch)
            event_data_batch = producer.create_batch()
            event_data_batch.add(event_data)
    if len(event_data_batch) > 0:
        producer.send_batch(event_data_batch)

print("Send messages in {} seconds.".format(time.time() - start_time))
