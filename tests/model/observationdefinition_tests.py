#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 on 2019-11-18.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from model import observationdefinition
from model.fhirdate import FHIRDate


class ObservationDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ObservationDefinition", js["resourceType"])
        return observationdefinition.ObservationDefinition(js)

    def testObservationDefinition1(self):
        inst = self.instantiate_from("observationdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ObservationDefinition instance")
        self.implObservationDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("ObservationDefinition", js["resourceType"])
        inst2 = observationdefinition.ObservationDefinition(js)
        self.implObservationDefinition1(inst2)

    def implObservationDefinition1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "laboratory")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/observation-category")
        self.assertEqual(inst.code.coding[0].code, "13980-8")
        self.assertEqual(inst.code.coding[0].display, "Albumin/Protein.total in Serum or Plasma by Electrophoresis")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.method.coding[0].code, "115341008")
        self.assertEqual(inst.method.coding[0].display, "Total measurement")
        self.assertEqual(inst.method.coding[0].system, "http://snomed.info/sct")
        self.assertFalse(inst.multipleResultsAllowed)
        self.assertEqual(inst.permittedDataType[0], "Quantity")
        self.assertEqual(inst.qualifiedInterval[0].category, "reference")
        self.assertEqual(inst.qualifiedInterval[0].context.coding[0].code, "normal")
        self.assertEqual(inst.qualifiedInterval[0].context.coding[0].display, "Normal Range")
        self.assertEqual(inst.qualifiedInterval[0].context.coding[0].system, "http://terminology.hl7.org/CodeSystem/referencerange-meaning")
        self.assertEqual(inst.qualifiedInterval[0].range.low.value, 50)
        self.assertEqual(inst.qualifiedInterval[1].category, "critical")
        self.assertEqual(inst.qualifiedInterval[1].context.coding[0].code, "normal")
        self.assertEqual(inst.qualifiedInterval[1].context.coding[0].display, "Normal Range")
        self.assertEqual(inst.qualifiedInterval[1].context.coding[0].system, "http://terminology.hl7.org/CodeSystem/referencerange-meaning")
        self.assertEqual(inst.qualifiedInterval[1].range.high.value, 40)
        self.assertEqual(inst.quantitativeDetails.decimalPrecision, 0)
        self.assertEqual(inst.quantitativeDetails.unit.coding[0].code, "%")
        self.assertEqual(inst.quantitativeDetails.unit.coding[0].display, "%")
        self.assertEqual(inst.quantitativeDetails.unit.coding[0].system, "http://unitsofmeasure.org")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

if __name__ == '__main__':
    unittest.main()