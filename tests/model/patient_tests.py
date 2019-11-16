#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2019-11-16.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from model import patient
from model.fhirdate import FHIRDate


class PatientTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Patient", js["resourceType"])
        return patient.Patient(js)

    def testPatient1(self):
        inst = self.instantiate_from("patient-example-xds.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient1(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient1(inst2)

    def implPatient1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "Metropolis")
        self.assertEqual(inst.address[0].country, "USA")
        self.assertEqual(inst.address[0].line[0], "100 Main St")
        self.assertEqual(inst.address[0].postalCode, "44130")
        self.assertEqual(inst.address[0].state, "Il")
        self.assertEqual(inst.birthDate.date, FHIRDate("1956-05-27").date)
        self.assertEqual(inst.birthDate.as_json(), "1956-05-27")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "xds")
        self.assertEqual(inst.identifier[0].system, "urn:oid:1.2.3.4.5")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "MR")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].use, "usual")
        self.assertEqual(inst.identifier[0].value, "89765a87b")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Doe")
        self.assertEqual(inst.name[0].given[0], "John")
        self.assertEqual(inst.text.status, "generated")

    def testPatient2(self):
        inst = self.instantiate_from("patient-example-f001-pieter.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient2(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient2(inst2)

    def implPatient2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "Amsterdam")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Van Egmondkade 23")
        self.assertEqual(inst.address[0].postalCode, "1024 RJ")
        self.assertEqual(inst.address[0].use, "home")
        self.assertEqual(inst.birthDate.date, FHIRDate("1944-11-17").date)
        self.assertEqual(inst.birthDate.as_json(), "1944-11-17")
        self.assertEqual(inst.communication[0].language.coding[0].code, "nl")
        self.assertEqual(inst.communication[0].language.coding[0].display, "Dutch")
        self.assertEqual(inst.communication[0].language.coding[0].system, "urn:ietf:bcp:47")
        self.assertEqual(inst.communication[0].language.text, "Nederlands")
        self.assertTrue(inst.communication[0].preferred)
        self.assertEqual(inst.contact[0].name.family, "Abels")
        self.assertEqual(inst.contact[0].name.given[0], "Sarah")
        self.assertEqual(inst.contact[0].name.use, "usual")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].code, "C")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0131")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].use, "mobile")
        self.assertEqual(inst.contact[0].telecom[0].value, "0690383372")
        self.assertFalse(inst.deceasedBoolean)
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[0].use, "usual")
        self.assertEqual(inst.identifier[0].value, "738472983")
        self.assertEqual(inst.identifier[1].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[1].use, "usual")
        self.assertEqual(inst.maritalStatus.coding[0].code, "M")
        self.assertEqual(inst.maritalStatus.coding[0].display, "Married")
        self.assertEqual(inst.maritalStatus.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus")
        self.assertEqual(inst.maritalStatus.text, "Getrouwd")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertTrue(inst.multipleBirthBoolean)
        self.assertEqual(inst.name[0].family, "van de Heuvel")
        self.assertEqual(inst.name[0].given[0], "Pieter")
        self.assertEqual(inst.name[0].suffix[0], "MSc")
        self.assertEqual(inst.name[0].use, "usual")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "mobile")
        self.assertEqual(inst.telecom[0].value, "0648352638")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "home")
        self.assertEqual(inst.telecom[1].value, "p.heuvel@gmail.com")
        self.assertEqual(inst.text.status, "generated")

    def testPatient3(self):
        inst = self.instantiate_from("patient-example-d.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient3(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient3(inst2)

    def implPatient3(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.birthDate.date, FHIRDate("1982-08-02").date)
        self.assertEqual(inst.birthDate.as_json(), "1982-08-02")
        self.assertTrue(inst.deceasedBoolean)
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "pat4")
        self.assertEqual(inst.identifier[0].system, "urn:oid:0.1.2.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "MR")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].use, "usual")
        self.assertEqual(inst.identifier[0].value, "123458")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Notsowell")
        self.assertEqual(inst.name[0].given[0], "Sandy")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.text.status, "generated")

    def testPatient4(self):
        inst = self.instantiate_from("patient-example-infant-twin-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient4(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient4(inst2)

    def implPatient4(self, inst):
        self.assertEqual(inst.birthDate.date, FHIRDate("2017-05-15").date)
        self.assertEqual(inst.birthDate.as_json(), "2017-05-15")
        self.assertEqual(inst.contact[0].name.family, "Organa")
        self.assertEqual(inst.contact[0].name.given[0], "Leia")
        self.assertEqual(inst.contact[0].name.use, "maiden")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].code, "72705000")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].display, "Mother")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.contact[0].relationship[0].coding[1].code, "N")
        self.assertEqual(inst.contact[0].relationship[0].coding[1].system, "http://terminology.hl7.org/CodeSystem/v2-0131")
        self.assertEqual(inst.contact[0].relationship[0].coding[2].code, "MTH")
        self.assertEqual(inst.contact[0].relationship[0].coding[2].system, "http://terminology.hl7.org/CodeSystem/v3-RoleCode")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].use, "mobile")
        self.assertEqual(inst.contact[0].telecom[0].value, "+31201234567")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName")
        self.assertEqual(inst.extension[0].valueString, "Organa")
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "infant-twin-1")
        self.assertEqual(inst.identifier[0].system, "http://coruscanthealth.org/main-hospital/patient-identifier")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "MR")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].value, "MRN7465737865")
        self.assertEqual(inst.identifier[1].system, "http://new-republic.gov/galactic-citizen-identifier")
        self.assertEqual(inst.identifier[1].value, "7465737865")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.multipleBirthInteger, 1)
        self.assertEqual(inst.name[0].family, "Solo")
        self.assertEqual(inst.name[0].given[0], "Jaina")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.text.status, "generated")

    def testPatient5(self):
        inst = self.instantiate_from("patient-example-infant-mom.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient5(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient5(inst2)

    def implPatient5(self, inst):
        self.assertEqual(inst.birthDate.date, FHIRDate("1995-10-12").date)
        self.assertEqual(inst.birthDate.as_json(), "1995-10-12")
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "infant-mom")
        self.assertEqual(inst.maritalStatus.coding[0].code, "M")
        self.assertEqual(inst.maritalStatus.coding[0].display, "Married")
        self.assertEqual(inst.maritalStatus.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Solo")
        self.assertEqual(inst.name[0].given[0], "Leia")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.name[1].family, "Organa")
        self.assertEqual(inst.name[1].given[0], "Leia")
        self.assertEqual(inst.name[1].use, "maiden")
        self.assertEqual(inst.text.status, "generated")

    def testPatient6(self):
        inst = self.instantiate_from("patient-example-newborn.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient6(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient6(inst2)

    def implPatient6(self, inst):
        self.assertEqual(inst.birthDate.date, FHIRDate("2017-09-05").date)
        self.assertEqual(inst.birthDate.as_json(), "2017-09-05")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName")
        self.assertEqual(inst.extension[0].valueString, "Everywoman")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "newborn")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.multipleBirthInteger, 2)
        self.assertEqual(inst.text.status, "generated")

    def testPatient7(self):
        inst = self.instantiate_from("patient-example-infant-fetal.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient7(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient7(inst2)

    def implPatient7(self, inst):
        self.assertEqual(inst.contact[0].name.family, "Organa")
        self.assertEqual(inst.contact[0].name.given[0], "Leia")
        self.assertEqual(inst.contact[0].name.use, "maiden")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].code, "72705000")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].display, "Mother")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.contact[0].relationship[0].coding[1].code, "N")
        self.assertEqual(inst.contact[0].relationship[0].coding[1].system, "http://terminology.hl7.org/CodeSystem/v2-0131")
        self.assertEqual(inst.contact[0].relationship[0].coding[2].code, "MTH")
        self.assertEqual(inst.contact[0].relationship[0].coding[2].system, "http://terminology.hl7.org/CodeSystem/v3-RoleCode")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].use, "mobile")
        self.assertEqual(inst.contact[0].telecom[0].value, "+31201234567")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName")
        self.assertEqual(inst.extension[0].valueString, "Organa")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "infant-fetal")
        self.assertEqual(inst.identifier[0].system, "http://coruscanthealth.org/main-hospital/patient-identifier")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "MR")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].value, "MRN657865757378")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")

    def testPatient8(self):
        inst = self.instantiate_from("patient-genetics-example1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient8(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient8(inst2)

    def implPatient8(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].line[0], "2222 Home Street")
        self.assertEqual(inst.address[0].use, "home")
        self.assertEqual(inst.birthDate.date, FHIRDate("1973-05-31").date)
        self.assertEqual(inst.birthDate.as_json(), "1973-05-31")
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "genetics-example1")
        self.assertEqual(inst.identifier[0].system, "http://hl7.org/fhir/sid/us-ssn")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "SS")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].value, "444222222")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Everywoman")
        self.assertEqual(inst.name[0].given[0], "Eve")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "555-555-2003")
        self.assertEqual(inst.text.status, "generated")

    def testPatient9(self):
        inst = self.instantiate_from("patient-example-b.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient9(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient9(inst2)

    def implPatient9(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.gender, "other")
        self.assertEqual(inst.id, "pat2")
        self.assertEqual(inst.identifier[0].system, "urn:oid:0.1.2.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "MR")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].use, "usual")
        self.assertEqual(inst.identifier[0].value, "123456")
        self.assertEqual(inst.link[0].type, "seealso")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Donald")
        self.assertEqual(inst.name[0].given[0], "Duck")
        self.assertEqual(inst.name[0].given[1], "D")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.photo[0].contentType, "image/gif")
        self.assertEqual(inst.text.status, "generated")

    def testPatient10(self):
        inst = self.instantiate_from("patient-example-c.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient10(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient10(inst2)

    def implPatient10(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.birthDate.date, FHIRDate("1982-01-23").date)
        self.assertEqual(inst.birthDate.as_json(), "1982-01-23")
        self.assertEqual(inst.deceasedDateTime.date, FHIRDate("2015-02-14T13:42:00+10:00").date)
        self.assertEqual(inst.deceasedDateTime.as_json(), "2015-02-14T13:42:00+10:00")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "pat3")
        self.assertEqual(inst.identifier[0].system, "urn:oid:0.1.2.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "MR")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].use, "usual")
        self.assertEqual(inst.identifier[0].value, "123457")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Notsowell")
        self.assertEqual(inst.name[0].given[0], "Simon")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.text.status, "generated")

if __name__ == '__main__':
    unittest.main()