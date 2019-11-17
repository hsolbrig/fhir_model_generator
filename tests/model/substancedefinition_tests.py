#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 on 2019-11-17.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from model import substancedefinition
from model.fhirdate import FHIRDate


class SubstanceDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SubstanceDefinition", js["resourceType"])
        return substancedefinition.SubstanceDefinition(js)

    def testSubstanceDefinition1(self):
        inst = self.instantiate_from("substancedefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SubstanceDefinition instance")
        self.implSubstanceDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("SubstanceDefinition", js["resourceType"])
        inst2 = substancedefinition.SubstanceDefinition(js)
        self.implSubstanceDefinition1(inst2)

    def implSubstanceDefinition1(self, inst):
        self.assertEqual(inst.category.coding[0].code, "100000075670")
        self.assertEqual(inst.category.coding[0].display, "Chemical")
        self.assertEqual(inst.category.coding[0].system, "http://example.europa.eu/fhir/SubstanceType")
        self.assertEqual(inst.code[0].code.coding[0].code, "SUB99611MIG")
        self.assertEqual(inst.code[0].code.coding[0].system, "http://example.europa.eu/fhir/Substance")
        self.assertEqual(inst.domain.coding[0].code, "100000000012")
        self.assertEqual(inst.domain.coding[0].display, "Human use")
        self.assertEqual(inst.domain.coding[0].system, "http://example.europa.eu/fhir/Domain")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "http://example.europa.eu/fhir/SMSId")
        self.assertEqual(inst.identifier.value, "100000099270")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].language[0].coding[0].code, "100000072147")
        self.assertEqual(inst.name[0].language[0].coding[0].display, "English")
        self.assertEqual(inst.name[0].language[0].coding[0].system, "http://example.europa.eu/fhir/Language")
        self.assertEqual(inst.name[0].name, "PARACETAMOL")
        self.assertTrue(inst.name[0].preferred)
        self.assertEqual(inst.name[0].status.coding[0].code, "200000005004")
        self.assertEqual(inst.name[0].status.coding[0].display, "Current")
        self.assertEqual(inst.name[0].status.coding[0].system, "http://example.europa.eu/fhir/Status")
        self.assertEqual(inst.name[1].language[0].coding[0].code, "100000072181")
        self.assertEqual(inst.name[1].language[0].coding[0].display, "Greek, Modern (1453-)")
        self.assertEqual(inst.name[1].language[0].coding[0].system, "http://example.europa.eu/fhir/Language")
        self.assertEqual(inst.name[1].name, "ΠΑΡΑΚΕΤΑΜΌΛΗ")
        self.assertFalse(inst.name[1].preferred)
        self.assertEqual(inst.name[1].status.coding[0].code, "200000005004")
        self.assertEqual(inst.name[1].status.coding[0].display, "Current")
        self.assertEqual(inst.name[1].status.coding[0].system, "http://example.europa.eu/fhir/Status")
        self.assertEqual(inst.name[2].language[0].coding[0].code, "100000072142")
        self.assertEqual(inst.name[2].language[0].coding[0].display, "Bulgarian")
        self.assertEqual(inst.name[2].language[0].coding[0].system, "http://example.europa.eu/fhir/Language")
        self.assertEqual(inst.name[2].name, "ПАРАЦЕТАМОЛ")
        self.assertFalse(inst.name[2].preferred)
        self.assertEqual(inst.name[2].status.coding[0].code, "200000005004")
        self.assertEqual(inst.name[2].status.coding[0].display, "Current")
        self.assertEqual(inst.name[2].status.coding[0].system, "http://example.europa.eu/fhir/Status")
        self.assertEqual(inst.name[3].language[0].coding[0].code, "100000072147")
        self.assertEqual(inst.name[3].language[0].coding[0].display, "English")
        self.assertEqual(inst.name[3].language[0].coding[0].system, "http://example.europa.eu/fhir/Language")
        self.assertEqual(inst.name[3].name, "ACETAMINOPHEN")
        self.assertFalse(inst.name[3].preferred)
        self.assertEqual(inst.name[3].status.coding[0].code, "200000005004")
        self.assertEqual(inst.name[3].status.coding[0].display, "Current")
        self.assertEqual(inst.name[3].status.coding[0].system, "http://example.europa.eu/fhir/Status")
        self.assertEqual(inst.status.coding[0].code, "200000005004")
        self.assertEqual(inst.status.coding[0].display, "Current")
        self.assertEqual(inst.status.coding[0].system, "http://example.europa.eu/fhir/Status")
        self.assertEqual(inst.text.status, "generated")

if __name__ == '__main__':
    unittest.main()