#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 on 2019-11-17.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from model import substanceprotein
from model.fhirdate import FHIRDate


class SubstanceProteinTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SubstanceProtein", js["resourceType"])
        return substanceprotein.SubstanceProtein(js)

    def testSubstanceProtein1(self):
        inst = self.instantiate_from("substanceprotein-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SubstanceProtein instance")
        self.implSubstanceProtein1(inst)

        js = inst.as_json()
        self.assertEqual("SubstanceProtein", js["resourceType"])
        inst2 = substanceprotein.SubstanceProtein(js)
        self.implSubstanceProtein1(inst2)

    def implSubstanceProtein1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p></div>")
        self.assertEqual(inst.text.status, "generated")

if __name__ == '__main__':
    unittest.main()