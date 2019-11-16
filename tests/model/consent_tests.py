#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2019-11-16.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from model import consent
from model.fhirdate import FHIRDate


class ConsentTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Consent", js["resourceType"])
        return consent.Consent(js)

    def testConsent1(self):
        inst = self.instantiate_from("consent-example-notThis.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent1(inst)

        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent1(inst2)

    def implConsent1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "59284-0")
        self.assertEqual(inst.category[0].coding[0].system, "http://loinc.org")
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(inst.id, "consent-example-notThis")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.policyRule.coding[0].code, "OPTIN")
        self.assertEqual(inst.policyRule.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.data[0].meaning, "related")
        self.assertEqual(inst.scope.coding[0].code, "patient-privacy")
        self.assertEqual(inst.scope.coding[0].system, "http://terminology.hl7.org/CodeSystem/consentscope")
        self.assertEqual(inst.sourceAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

    def testConsent2(self):
        inst = self.instantiate_from("consent-example-smartonfhir.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent2(inst)

        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent2(inst2)

    def implConsent2(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "59284-0")
        self.assertEqual(inst.category[0].coding[0].system, "http://loinc.org")
        self.assertEqual(inst.dateTime.date, FHIRDate("2016-06-23T17:02:33+10:00").date)
        self.assertEqual(inst.dateTime.as_json(), "2016-06-23T17:02:33+10:00")
        self.assertEqual(inst.id, "consent-example-smartonfhir")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.policyRule.coding[0].code, "OPTIN")
        self.assertEqual(inst.policyRule.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.period.end.date, FHIRDate("2016-06-23T17:32:33+10:00").date)
        self.assertEqual(inst.provision.period.end.as_json(), "2016-06-23T17:32:33+10:00")
        self.assertEqual(inst.provision.period.start.date, FHIRDate("2016-06-23T17:02:33+10:00").date)
        self.assertEqual(inst.provision.period.start.as_json(), "2016-06-23T17:02:33+10:00")
        self.assertEqual(inst.provision.provision[0].action[0].coding[0].code, "access")
        self.assertEqual(inst.provision.provision[0].action[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.provision[0].class_fhir[0].code, "MedicationRequest")
        self.assertEqual(inst.provision.provision[0].class_fhir[0].system, "http://hl7.org/fhir/resource-types")
        self.assertEqual(inst.provision.provision[0].type, "permit")
        self.assertEqual(inst.scope.coding[0].code, "patient-privacy")
        self.assertEqual(inst.scope.coding[0].system, "http://terminology.hl7.org/CodeSystem/consentscope")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

    def testConsent3(self):
        inst = self.instantiate_from("consent-example-notAuthor.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent3(inst)

        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent3(inst2)

    def implConsent3(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "59284-0")
        self.assertEqual(inst.category[0].coding[0].system, "http://loinc.org")
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(inst.id, "consent-example-notAuthor")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.policyRule.coding[0].code, "OPTIN")
        self.assertEqual(inst.policyRule.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.actor[0].role.coding[0].code, "CST")
        self.assertEqual(inst.provision.actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.scope.coding[0].code, "patient-privacy")
        self.assertEqual(inst.scope.coding[0].system, "http://terminology.hl7.org/CodeSystem/consentscope")
        self.assertEqual(inst.sourceAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

    def testConsent4(self):
        inst = self.instantiate_from("consent-example-notTime.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent4(inst)

        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent4(inst2)

    def implConsent4(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "59284-0")
        self.assertEqual(inst.category[0].coding[0].system, "http://loinc.org")
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(inst.id, "consent-example-notTime")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.policyRule.coding[0].code, "OPTIN")
        self.assertEqual(inst.policyRule.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.period.end.date, FHIRDate("2015-02-01").date)
        self.assertEqual(inst.provision.period.end.as_json(), "2015-02-01")
        self.assertEqual(inst.provision.period.start.date, FHIRDate("2015-01-01").date)
        self.assertEqual(inst.provision.period.start.as_json(), "2015-01-01")
        self.assertEqual(inst.scope.coding[0].code, "patient-privacy")
        self.assertEqual(inst.scope.coding[0].system, "http://terminology.hl7.org/CodeSystem/consentscope")
        self.assertEqual(inst.sourceAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

    def testConsent5(self):
        inst = self.instantiate_from("consent-example-signature.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent5(inst)

        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent5(inst2)

    def implConsent5(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "npp")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentcategorycodes")
        self.assertEqual(inst.dateTime.date, FHIRDate("2016-05-26T00:41:10-04:00").date)
        self.assertEqual(inst.dateTime.as_json(), "2016-05-26T00:41:10-04:00")
        self.assertEqual(inst.id, "consent-example-signature")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.840.1.113883.3.72.5.9.1")
        self.assertEqual(inst.identifier[0].value, "494e0c7a-a69e-4fb4-9d02-6aae747790d7")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.policyRule.coding[0].code, "OPTIN")
        self.assertEqual(inst.policyRule.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.provision.actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.provision.period.end.date, FHIRDate("2016-10-10").date)
        self.assertEqual(inst.provision.period.end.as_json(), "2016-10-10")
        self.assertEqual(inst.provision.period.start.date, FHIRDate("2015-10-10").date)
        self.assertEqual(inst.provision.period.start.as_json(), "2015-10-10")
        self.assertEqual(inst.provision.provision[0].actor[0].role.coding[0].code, "AUT")
        self.assertEqual(inst.provision.provision[0].actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.provision.provision[0].class_fhir[0].code, "application/hl7-cda+xml")
        self.assertEqual(inst.provision.provision[0].class_fhir[0].system, "urn:ietf:bcp:13")
        self.assertEqual(inst.provision.provision[0].code[0].coding[0].code, "34133-9")
        self.assertEqual(inst.provision.provision[0].code[0].coding[0].system, "http://loinc.org")
        self.assertEqual(inst.provision.provision[0].code[1].coding[0].code, "18842-5")
        self.assertEqual(inst.provision.provision[0].code[1].coding[0].system, "http://loinc.org")
        self.assertEqual(inst.provision.provision[0].type, "permit")
        self.assertEqual(inst.scope.coding[0].code, "patient-privacy")
        self.assertEqual(inst.scope.coding[0].system, "http://terminology.hl7.org/CodeSystem/consentscope")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

    def testConsent6(self):
        inst = self.instantiate_from("consent-example-notThem.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent6(inst)

        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent6(inst2)

    def implConsent6(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "59284-0")
        self.assertEqual(inst.category[0].coding[0].system, "http://loinc.org")
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(inst.id, "consent-example-notThem")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.policyRule.coding[0].code, "OPTIN")
        self.assertEqual(inst.policyRule.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.action[0].coding[0].code, "access")
        self.assertEqual(inst.provision.action[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.action[1].coding[0].code, "correct")
        self.assertEqual(inst.provision.action[1].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.provision.actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.scope.coding[0].code, "patient-privacy")
        self.assertEqual(inst.scope.coding[0].system, "http://terminology.hl7.org/CodeSystem/consentscope")
        self.assertEqual(inst.sourceAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

    def testConsent7(self):
        inst = self.instantiate_from("consent-example-grantor.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent7(inst)

        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent7(inst2)

    def implConsent7(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "INFAO")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(inst.id, "consent-example-grantor")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.policyRule.coding[0].code, "OPTOUT")
        self.assertEqual(inst.policyRule.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.action[0].coding[0].code, "access")
        self.assertEqual(inst.provision.action[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.actor[0].role.coding[0].code, "CST")
        self.assertEqual(inst.provision.actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.provision.actor[1].role.coding[0].code, "PRCP")
        self.assertEqual(inst.provision.actor[1].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.scope.coding[0].code, "patient-privacy")
        self.assertEqual(inst.scope.coding[0].system, "http://terminology.hl7.org/CodeSystem/consentscope")
        self.assertEqual(inst.sourceAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

    def testConsent8(self):
        inst = self.instantiate_from("consent-example-notOrg.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent8(inst)

        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent8(inst2)

    def implConsent8(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "59284-0")
        self.assertEqual(inst.category[0].coding[0].system, "http://loinc.org")
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(inst.id, "consent-example-notOrg")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.policyRule.coding[0].code, "OPTIN")
        self.assertEqual(inst.policyRule.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.action[0].coding[0].code, "access")
        self.assertEqual(inst.provision.action[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.action[1].coding[0].code, "correct")
        self.assertEqual(inst.provision.action[1].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.provision.actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.provision.type, "deny")
        self.assertEqual(inst.scope.coding[0].code, "patient-privacy")
        self.assertEqual(inst.scope.coding[0].system, "http://terminology.hl7.org/CodeSystem/consentscope")
        self.assertEqual(inst.sourceAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

    def testConsent9(self):
        inst = self.instantiate_from("consent-example-pkb.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent9(inst)

        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent9(inst2)

    def implConsent9(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "59284-0")
        self.assertEqual(inst.category[0].coding[0].system, "http://loinc.org")
        self.assertEqual(inst.dateTime.date, FHIRDate("2016-06-16").date)
        self.assertEqual(inst.dateTime.as_json(), "2016-06-16")
        self.assertEqual(inst.id, "consent-example-pkb")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.policyRule.coding[0].code, "OPTOUT")
        self.assertEqual(inst.policyRule.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.action[0].coding[0].code, "access")
        self.assertEqual(inst.provision.action[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.provision.actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.provision.provision[0].action[0].coding[0].code, "access")
        self.assertEqual(inst.provision.provision[0].action[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.provision[0].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.provision.provision[0].actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.provision.provision[0].securityLabel[0].code, "PSY")
        self.assertEqual(inst.provision.provision[0].securityLabel[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.provision[1].action[0].coding[0].code, "access")
        self.assertEqual(inst.provision.provision[1].action[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.provision[1].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.provision.provision[1].actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.provision.provision[1].securityLabel[0].code, "SPI")
        self.assertEqual(inst.provision.provision[1].securityLabel[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.provision[2].action[0].coding[0].code, "access")
        self.assertEqual(inst.provision.provision[2].action[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.provision[2].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.provision.provision[2].actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.provision.provision[2].securityLabel[0].code, "N")
        self.assertEqual(inst.provision.provision[2].securityLabel[0].system, "http://terminology.hl7.org/CodeSystem/v3-Confidentiality")
        self.assertEqual(inst.provision.provision[3].action[0].coding[0].code, "access")
        self.assertEqual(inst.provision.provision[3].action[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.provision[3].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.provision.provision[3].actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.provision.provision[3].securityLabel[0].code, "PSY")
        self.assertEqual(inst.provision.provision[3].securityLabel[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.provision[4].action[0].coding[0].code, "access")
        self.assertEqual(inst.provision.provision[4].action[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.provision[4].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.provision.provision[4].actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.provision.provision[4].securityLabel[0].code, "SPI")
        self.assertEqual(inst.provision.provision[4].securityLabel[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.provision[5].action[0].coding[0].code, "access")
        self.assertEqual(inst.provision.provision[5].action[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.provision[5].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.provision.provision[5].actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.provision.provision[5].securityLabel[0].code, "SEX")
        self.assertEqual(inst.provision.provision[5].securityLabel[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.provision[6].action[0].coding[0].code, "access")
        self.assertEqual(inst.provision.provision[6].action[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.provision[6].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.provision.provision[6].actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.provision.provision[6].securityLabel[0].code, "N")
        self.assertEqual(inst.provision.provision[6].securityLabel[0].system, "http://terminology.hl7.org/CodeSystem/v3-Confidentiality")
        self.assertEqual(inst.provision.provision[7].action[0].coding[0].code, "access")
        self.assertEqual(inst.provision.provision[7].action[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.provision[7].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.provision.provision[7].actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.provision.provision[7].securityLabel[0].code, "PSY")
        self.assertEqual(inst.provision.provision[7].securityLabel[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.provision[8].action[0].coding[0].code, "access")
        self.assertEqual(inst.provision.provision[8].action[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.provision[8].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.provision.provision[8].actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.provision.provision[8].securityLabel[0].code, "SPI")
        self.assertEqual(inst.provision.provision[8].securityLabel[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.provision[9].action[0].coding[0].code, "access")
        self.assertEqual(inst.provision.provision[9].action[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentaction")
        self.assertEqual(inst.provision.provision[9].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.provision.provision[9].actor[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.provision.provision[9].securityLabel[0].code, "SEX")
        self.assertEqual(inst.provision.provision[9].securityLabel[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.securityLabel[0].code, "N")
        self.assertEqual(inst.provision.securityLabel[0].system, "http://terminology.hl7.org/CodeSystem/v3-Confidentiality")
        self.assertEqual(inst.scope.coding[0].code, "patient-privacy")
        self.assertEqual(inst.scope.coding[0].system, "http://terminology.hl7.org/CodeSystem/consentscope")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

    def testConsent10(self):
        inst = self.instantiate_from("consent-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent10(inst)

        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent10(inst2)

    def implConsent10(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "59284-0")
        self.assertEqual(inst.category[0].coding[0].system, "http://loinc.org")
        self.assertEqual(inst.dateTime.date, FHIRDate("2016-05-11").date)
        self.assertEqual(inst.dateTime.as_json(), "2016-05-11")
        self.assertEqual(inst.id, "consent-example-basic")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.policyRule.coding[0].code, "OPTIN")
        self.assertEqual(inst.policyRule.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.provision.period.end.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.provision.period.end.as_json(), "2016-01-01")
        self.assertEqual(inst.provision.period.start.date, FHIRDate("1964-01-01").date)
        self.assertEqual(inst.provision.period.start.as_json(), "1964-01-01")
        self.assertEqual(inst.scope.coding[0].code, "patient-privacy")
        self.assertEqual(inst.scope.coding[0].system, "http://terminology.hl7.org/CodeSystem/consentscope")
        self.assertEqual(inst.sourceAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

if __name__ == '__main__':
    unittest.main()