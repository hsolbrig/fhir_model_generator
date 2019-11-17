#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 on 2019-11-17.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from model import documentreference
from model.fhirdate import FHIRDate


class DocumentReferenceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DocumentReference", js["resourceType"])
        return documentreference.DocumentReference(js)

    def testDocumentReference1(self):
        inst = self.instantiate_from("documentreference-example-dicom.json")
        self.assertIsNotNone(inst, "Must have instantiated a DocumentReference instance")
        self.implDocumentReference1(inst)

        js = inst.as_json()
        self.assertEqual("DocumentReference", js["resourceType"])
        inst2 = documentreference.DocumentReference(js)
        self.implDocumentReference1(inst2)

    def implDocumentReference1(self, inst):
        self.assertEqual(inst.content[0].attachment.contentType, "application/dicom")
        self.assertEqual(inst.content[0].attachment.height, 480)
        self.assertEqual(inst.content[0].attachment.width, 640)
        self.assertEqual(inst.context.event[0].coding[0].code, "US")
        self.assertEqual(inst.context.event[0].coding[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.context.event[1].coding[0].code, "399067008")
        self.assertEqual(inst.context.event[1].coding[0].display, "Lateral projection")
        self.assertEqual(inst.context.event[1].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.extension[0].url, "http://nema.org/fhir/extensions#0002-0010")
        self.assertEqual(inst.extension[0].valueUri, "urn:oid:1.2.840.10008.1.2.1")
        self.assertEqual(inst.id, "1.2.840.11361907579238403408700.3.1.04.19970327150033")
        self.assertEqual(inst.identifier[0].system, "urn:dicom:uid")
        self.assertEqual(inst.identifier[0].type.text, "InstanceUID")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "urn:oid:1.2.840.11361907579238403408700.3.1.04.19970327150033")
        self.assertEqual(inst.identifier[1].system, "http://acme-imaging.com/accession/2012")
        self.assertEqual(inst.identifier[1].type.text, "accessionNo")
        self.assertEqual(inst.identifier[1].value, "1234567")
        self.assertEqual(inst.identifier[2].system, "urn:dicom:uid")
        self.assertEqual(inst.identifier[2].type.text, "studyId")
        self.assertEqual(inst.identifier[2].value, "urn:oid:1.2.840.113619.2.21.848.34082.0.538976288.3")
        self.assertEqual(inst.identifier[3].system, "urn:dicom:uid")
        self.assertEqual(inst.identifier[3].type.text, "seriesId")
        self.assertEqual(inst.identifier[3].value, "urn:oid:1.2.840.113619.2.21.3408.700.0.757923840.3.0")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")

    def testDocumentReference2(self):
        inst = self.instantiate_from("documentreference-example-xray.json")
        self.assertIsNotNone(inst, "Must have instantiated a DocumentReference instance")
        self.implDocumentReference2(inst)

        js = inst.as_json()
        self.assertEqual("DocumentReference", js["resourceType"])
        inst2 = documentreference.DocumentReference(js)
        self.implDocumentReference2(inst2)

    def implDocumentReference2(self, inst):
        self.assertEqual(inst.content[0].attachment.contentType, "image/jpeg")
        self.assertEqual(inst.content[0].attachment.creation.date, FHIRDate("2016-03-15").date)
        self.assertEqual(inst.content[0].attachment.creation.as_json(), "2016-03-15")
        self.assertEqual(inst.content[0].attachment.height, 432)
        self.assertEqual(inst.content[0].attachment.url, "http://someimagingcenter.org/fhir/Binary/A12345")
        self.assertEqual(inst.content[0].attachment.width, 640)
        self.assertEqual(inst.content[0].id, "a1")
        self.assertEqual(inst.context.event[0].coding[0].code, "39714003")
        self.assertEqual(inst.context.event[0].coding[0].display, "Skeletal X-ray of wrist and hand")
        self.assertEqual(inst.context.event[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.context.event[1].coding[0].code, "85151006")
        self.assertEqual(inst.context.event[1].coding[0].display, "Structure of left hand (body structure)")
        self.assertEqual(inst.context.event[1].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "xray")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Xray of left hand for Patient Henry Levin (MRN 12345) 2016-03-15</div>")
        self.assertEqual(inst.text.status, "generated")

    def testDocumentReference3(self):
        inst = self.instantiate_from("documentreference-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DocumentReference instance")
        self.implDocumentReference3(inst)

        js = inst.as_json()
        self.assertEqual("DocumentReference", js["resourceType"])
        inst2 = documentreference.DocumentReference(js)
        self.implDocumentReference3(inst2)

    def implDocumentReference3(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "History and Physical")
        self.assertEqual(inst.category[0].coding[0].display, "History and Physical")
        self.assertEqual(inst.category[0].coding[0].system, "http://ihe.net/xds/connectathon/classCodes")
        self.assertEqual(inst.contained[0].id, "a2")
        self.assertEqual(inst.content[0].attachment.contentType, "application/hl7-v3+xml")
        self.assertEqual(inst.content[0].attachment.creation.date, FHIRDate("2005-12-24T09:35:00+11:00").date)
        self.assertEqual(inst.content[0].attachment.creation.as_json(), "2005-12-24T09:35:00+11:00")
        self.assertEqual(inst.content[0].attachment.hash, "2jmj7l5rSw0yVb/vlWAYkK/YBwk=")
        self.assertEqual(inst.content[0].attachment.language, "en-US")
        self.assertEqual(inst.content[0].attachment.size, 3654)
        self.assertEqual(inst.content[0].attachment.title, "Physical")
        self.assertEqual(inst.content[0].attachment.url, "http://example.org/xds/mhd/Binary/07a6483f-732b-461e-86b6-edb665c45510")
        self.assertEqual(inst.content[0].format.code, "urn:ihe:pcc:handp:2008")
        self.assertEqual(inst.content[0].format.display, "History and Physical Specification")
        self.assertEqual(inst.content[0].format.system, "urn:oid:1.3.6.1.4.1.19376.1.2.3")
        self.assertEqual(inst.context.event[0].coding[0].code, "T-D8200")
        self.assertEqual(inst.context.event[0].coding[0].display, "Arm")
        self.assertEqual(inst.context.event[0].coding[0].system, "http://ihe.net/xds/connectathon/eventCodes")
        self.assertEqual(inst.context.facilityType.coding[0].code, "Outpatient")
        self.assertEqual(inst.context.facilityType.coding[0].display, "Outpatient")
        self.assertEqual(inst.context.facilityType.coding[0].system, "http://www.ihe.net/xds/connectathon/healthcareFacilityTypeCodes")
        self.assertEqual(inst.context.period.end.date, FHIRDate("2004-12-23T08:01:00+11:00").date)
        self.assertEqual(inst.context.period.end.as_json(), "2004-12-23T08:01:00+11:00")
        self.assertEqual(inst.context.period.start.date, FHIRDate("2004-12-23T08:00:00+11:00").date)
        self.assertEqual(inst.context.period.start.as_json(), "2004-12-23T08:00:00+11:00")
        self.assertEqual(inst.context.practiceSetting.coding[0].code, "General Medicine")
        self.assertEqual(inst.context.practiceSetting.coding[0].display, "General Medicine")
        self.assertEqual(inst.context.practiceSetting.coding[0].system, "http://www.ihe.net/xds/connectathon/practiceSettingCodes")
        self.assertEqual(inst.date.date, FHIRDate("2005-12-24T09:43:41+11:00").date)
        self.assertEqual(inst.date.as_json(), "2005-12-24T09:43:41+11:00")
        self.assertEqual(inst.description, "Physical")
        self.assertEqual(inst.docStatus, "preliminary")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234")
        self.assertEqual(inst.masterIdentifier.system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.masterIdentifier.value, "urn:oid:1.3.6.1.4.1.21367.2005.3.7")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.relatesTo[0].code, "appends")
        self.assertEqual(inst.securityLabel[0].coding[0].code, "V")
        self.assertEqual(inst.securityLabel[0].coding[0].display, "very restricted")
        self.assertEqual(inst.securityLabel[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-Confidentiality")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "34108-1")
        self.assertEqual(inst.type.coding[0].display, "Outpatient Note")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")

    def testDocumentReference4(self):
        inst = self.instantiate_from("documentreference-example-diagram.json")
        self.assertIsNotNone(inst, "Must have instantiated a DocumentReference instance")
        self.implDocumentReference4(inst)

        js = inst.as_json()
        self.assertEqual("DocumentReference", js["resourceType"])
        inst2 = documentreference.DocumentReference(js)
        self.implDocumentReference4(inst2)

    def implDocumentReference4(self, inst):
        self.assertEqual(inst.content[0].attachment.contentType, "image/gif")
        self.assertEqual(inst.content[0].attachment.creation.date, FHIRDate("2009-09-03").date)
        self.assertEqual(inst.content[0].attachment.creation.as_json(), "2009-09-03")
        self.assertEqual(inst.content[0].attachment.frames, 1)
        self.assertEqual(inst.content[0].attachment.height, 145)
        self.assertEqual(inst.content[0].attachment.width, 126)
        self.assertEqual(inst.content[0].id, "a1")
        self.assertEqual(inst.date.date, FHIRDate("2017-12-17T14:56:18Z").date)
        self.assertEqual(inst.date.as_json(), "2017-12-17T14:56:18Z")
        self.assertEqual(inst.id, "example-diagram")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "image")
        self.assertEqual(inst.type.coding[0].display, "Image")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/media-type")

    def testDocumentReference5(self):
        inst = self.instantiate_from("documentreference-example-sound.json")
        self.assertIsNotNone(inst, "Must have instantiated a DocumentReference instance")
        self.implDocumentReference5(inst)

        js = inst.as_json()
        self.assertEqual("DocumentReference", js["resourceType"])
        inst2 = documentreference.DocumentReference(js)
        self.implDocumentReference5(inst2)

    def implDocumentReference5(self, inst):
        self.assertEqual(inst.content[0].attachment.contentType, "audio/mpeg")
        self.assertEqual(inst.content[0].attachment.data, "dG9vIGJpZyB0b28gaW5jbHVkZSB0aGUgd2hvbGU=")
        self.assertEqual(inst.content[0].attachment.duration, 65)
        self.assertEqual(inst.id, "sound")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Sound recording of speech example for Patient Henry Levin (MRN 12345):<br/><img src=\"#11\" alt=\"diagram\"/></div>")
        self.assertEqual(inst.text.status, "generated")

if __name__ == '__main__':
    unittest.main()