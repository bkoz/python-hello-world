#!/usr/bin/env python
# coding: utf-8

"""
Example ElasticSearch client using the SDK.
"""

import logging
import os
from datetime import datetime
from elasticsearch import Elasticsearch

logging.basicConfig(level=logging.INFO)

#
# Environment variables and defaults.
#
ELASTIC_HOST = os.getenv("ELASTIC_HOST", "localhost")
ELASTIC_PASSWORD = os.getenv("ELASTIC_PASSWORD", "elastic_password")
ELASTIC_USER = os.getenv("ELASTIC_USER", "elastic")
ELASTIC_PORT = os.getenv("ELASTIC_PORT", "443")
VERIFY_CERTS = os.getenv("VERIFY_CERTS", False)

url = f'https://{ELASTIC_HOST}:{ELASTIC_PORT}'
logging.info("url: %s", url)

es = Elasticsearch(url, verify_certs=VERIFY_CERTS, basic_auth=(ELASTIC_USER, ELASTIC_PASSWORD))

#
# GET the Elastic status.
#
logging.info("Elastic info: %s:", es.info())

#
# POST some example data.
#
# To index a document, three pieces of information are required: index, id, and a body
#
doc = {
    'author': 'Abraham Lincoln',
    'text': 'Four score and seven years ago...',
    'timestamp': datetime.now(),
}
resp = es.index(index="test-index", id=1, document=doc)
logging.info("response: %s", resp['result'])

#
# GET the example back.
#
# To get a document, the index and id are required:
#
resp = es.get(index="test-index", id=1)
logging.info("response: %s", resp['_source'])

#
# Search
#
resp = es.search(index="test-index", query={"match_all": {}})
logging.info("Got %d Hits:", resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    logging.info("%(timestamp)s %(author)s: %(text)s", hit["_source"])
