#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 on 2019-11-18.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from model import topic
from model.fhirdate import FHIRDate


class TopicTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Topic", js["resourceType"])
        return topic.Topic(js)

    def testTopic1(self):
        inst = self.instantiate_from("topic-example-admission.json")
        self.assertIsNotNone(inst, "Must have instantiated a Topic instance")
        self.implTopic1(inst)

        js = inst.as_json()
        self.assertEqual("Topic", js["resourceType"])
        inst2 = topic.Topic(js)
        self.implTopic1(inst2)

    def implTopic1(self, inst):
        self.assertEqual(inst.canFilterBy[0].documentation, "Matching based on the Patient (subject) of an Encounter or based on the Patient's group membership (in/not-in).")
        self.assertEqual(inst.canFilterBy[0].matchType[0], "=")
        self.assertEqual(inst.canFilterBy[0].matchType[1], "in")
        self.assertEqual(inst.canFilterBy[0].matchType[2], "not-in")
        self.assertEqual(inst.canFilterBy[0].name, "patient")
        self.assertEqual(inst.id, "admission")
        self.assertEqual(inst.resourceTrigger.description, "Beginning of a clinical encounter")
        self.assertEqual(inst.resourceTrigger.fhirPathCriteria, "%previous.status!='in-progress' and %current.status='in-progress'")
        self.assertEqual(inst.resourceTrigger.queryCriteria.current, "status=in-progress")
        self.assertEqual(inst.resourceTrigger.queryCriteria.previous, "status:not=in-progress")
        self.assertTrue(inst.resourceTrigger.queryCriteria.requireBoth)
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "admission")
        self.assertEqual(inst.url, "http://argonautproject.org/subscription-ig/Topic/admission")

if __name__ == '__main__':
    unittest.main()