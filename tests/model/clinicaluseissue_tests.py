#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 on 2019-11-18.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from model import clinicaluseissue
from model.fhirdate import FHIRDate


class ClinicalUseIssueTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ClinicalUseIssue", js["resourceType"])
        return clinicaluseissue.ClinicalUseIssue(js)

    def testClinicalUseIssue1(self):
        inst = self.instantiate_from("clinicaluseissue-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ClinicalUseIssue instance")
        self.implClinicalUseIssue1(inst)

        js = inst.as_json()
        self.assertEqual("ClinicalUseIssue", js["resourceType"])
        inst2 = clinicaluseissue.ClinicalUseIssue(js)
        self.implClinicalUseIssue1(inst2)

    def implClinicalUseIssue1(self, inst):
        self.assertEqual(inst.contraindication.comorbidity[0].coding[0].code, "Hepaticdisease")
        self.assertEqual(inst.contraindication.comorbidity[0].coding[0].system, "http://ema.europa.eu/example/comorbidity")
        self.assertEqual(inst.contraindication.diseaseSymptomProcedure.coding[0].code, "Coagulopathiesandbleedingdiatheses(exclthrombocytopenic)")
        self.assertEqual(inst.contraindication.diseaseSymptomProcedure.coding[0].system, "http://ema.europa.eu/example/contraindicationsasdisease-symptom-procedure")
        self.assertEqual(inst.contraindication.diseaseSymptomProcedure.text, "Hepatic disease associated with coagulopathy and clinically relevant bleeding risk")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "contraindication")

if __name__ == '__main__':
    unittest.main()