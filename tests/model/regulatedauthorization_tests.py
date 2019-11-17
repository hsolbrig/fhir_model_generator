#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 on 2019-11-17.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from model import regulatedauthorization
from model.fhirdate import FHIRDate


class RegulatedAuthorizationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("RegulatedAuthorization", js["resourceType"])
        return regulatedauthorization.RegulatedAuthorization(js)

    def testRegulatedAuthorization1(self):
        inst = self.instantiate_from("regulatedauthorization-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a RegulatedAuthorization instance")
        self.implRegulatedAuthorization1(inst)

        js = inst.as_json()
        self.assertEqual("RegulatedAuthorization", js["resourceType"])
        inst2 = regulatedauthorization.RegulatedAuthorization(js)
        self.implRegulatedAuthorization1(inst2)

    def implRegulatedAuthorization1(self, inst):
        self.assertEqual(inst.case.application[0].dateDateTime.date, FHIRDate("2015-08-01").date)
        self.assertEqual(inst.case.application[0].dateDateTime.as_json(), "2015-08-01")
        self.assertEqual(inst.case.application[0].identifier.system, "http://ema.europa.eu/example/applicationidentifier-number")
        self.assertEqual(inst.case.application[0].identifier.value, "IA38G")
        self.assertEqual(inst.case.application[0].type.coding[0].code, "GroupTypeIAVariationNotification")
        self.assertEqual(inst.case.application[0].type.coding[0].system, "http://ema.europa.eu/example/marketingAuthorisationApplicationType")
        self.assertEqual(inst.case.datePeriod.end.date, FHIRDate("2015-08-21").date)
        self.assertEqual(inst.case.datePeriod.end.as_json(), "2015-08-21")
        self.assertEqual(inst.case.datePeriod.start.date, FHIRDate("2015-08-02").date)
        self.assertEqual(inst.case.datePeriod.start.as_json(), "2015-08-02")
        self.assertEqual(inst.case.identifier.system, "http://ema.europa.eu/example/procedureidentifier-number")
        self.assertEqual(inst.case.identifier.value, "EMEA/H/C/009999/IA/0099/G")
        self.assertEqual(inst.case.type.coding[0].code, "VariationTypeIA")
        self.assertEqual(inst.case.type.coding[0].system, "http://ema.europa.eu/example/marketingAuthorisationProcedureType")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://ema.europa.eu/example/marketingAuthorisationNumber")
        self.assertEqual(inst.identifier[0].value, "EU/1/11/999/001")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.region[0].coding[0].code, "EU")
        self.assertEqual(inst.region[0].coding[0].system, "http://ema.europa.eu/example/country")
        self.assertEqual(inst.status.coding[0].code, "active")
        self.assertEqual(inst.status.coding[0].system, "http://ema.europa.eu/example/authorisationstatus")
        self.assertEqual(inst.statusDate.date, FHIRDate("2015-01-14").date)
        self.assertEqual(inst.statusDate.as_json(), "2015-01-14")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.validityPeriod.end.date, FHIRDate("2020-05-20").date)
        self.assertEqual(inst.validityPeriod.end.as_json(), "2020-05-20")
        self.assertEqual(inst.validityPeriod.start.date, FHIRDate("2015-08-16").date)
        self.assertEqual(inst.validityPeriod.start.as_json(), "2015-08-16")

if __name__ == '__main__':
    unittest.main()