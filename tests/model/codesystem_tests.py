#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 on 2019-11-17.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from model import codesystem
from model.fhirdate import FHIRDate


class CodeSystemTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CodeSystem", js["resourceType"])
        return codesystem.CodeSystem(js)

    def testCodeSystem1(self):
        inst = self.instantiate_from("codesystem-codesystem-list-example-codes(list-example-codes).json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem1(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem1(inst2)

    def implCodeSystem1(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(inst.concept[0].code, "alerts")
        self.assertEqual(inst.concept[0].definition, "A list of alerts for the patient.")
        self.assertEqual(inst.concept[0].display, "Alerts")
        self.assertEqual(inst.concept[1].code, "adverserxns")
        self.assertEqual(inst.concept[1].definition, "A list of part adverse reactions.")
        self.assertEqual(inst.concept[1].display, "Adverse Reactions")
        self.assertEqual(inst.concept[2].code, "allergies")
        self.assertEqual(inst.concept[2].definition, "A list of Allergies for the patient.")
        self.assertEqual(inst.concept[2].display, "Allergies")
        self.assertEqual(inst.concept[3].code, "medications")
        self.assertEqual(inst.concept[3].definition, "A list of medication statements for the patient.")
        self.assertEqual(inst.concept[3].display, "Medication List")
        self.assertEqual(inst.concept[4].code, "problems")
        self.assertEqual(inst.concept[4].definition, "A list of problems that the patient is known of have (or have had in the past).")
        self.assertEqual(inst.concept[4].display, "Problem List")
        self.assertEqual(inst.concept[5].code, "worklist")
        self.assertEqual(inst.concept[5].definition, "A list of items that constitute a set of work to be performed (typically this code would be specialized for more specific uses, such as a ward round list).")
        self.assertEqual(inst.concept[5].display, "Worklist")
        self.assertEqual(inst.concept[6].code, "waiting")
        self.assertEqual(inst.concept[6].definition, "A list of items waiting for an event (perhaps a surgical patient waiting list).")
        self.assertEqual(inst.concept[6].display, "Waiting List")
        self.assertEqual(inst.concept[7].code, "protocols")
        self.assertEqual(inst.concept[7].definition, "A set of protocols to be followed.")
        self.assertEqual(inst.concept[7].display, "Protocols")
        self.assertEqual(inst.concept[8].code, "plans")
        self.assertEqual(inst.concept[8].definition, "A set of care plans that apply in a particular context of care.")
        self.assertEqual(inst.concept[8].display, "Care Plans")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.content, "complete")
        self.assertEqual(inst.description, "Example use codes for the List resource - typical kinds of use.")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status")
        self.assertEqual(inst.extension[0].valueString, "Informative")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm")
        self.assertEqual(inst.extension[1].valueInteger, 1)
        self.assertEqual(inst.extension[2].url, "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg")
        self.assertEqual(inst.extension[2].valueCode, "fhir")
        self.assertEqual(inst.id, "list-example-codes")
        self.assertEqual(inst.identifier.system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier.value, "urn:oid:2.16.840.1.113883.4.642.1.308")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2019-10-24T11:53:00+11:00").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2019-10-24T11:53:00+11:00")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/shareablecodesystem")
        self.assertEqual(inst.name, "Example Use Codes for List")
        self.assertEqual(inst.publisher, "FHIR Project")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/list-example-use-codes")
        self.assertEqual(inst.valueSet, "http://hl7.org/fhir/ValueSet/list-example-codes")
        self.assertEqual(inst.version, "3.0.2")

if __name__ == '__main__':
    unittest.main()