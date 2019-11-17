#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 on 2019-11-17.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from model import packagedproductdefinition
from model.fhirdate import FHIRDate


class PackagedProductDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("PackagedProductDefinition", js["resourceType"])
        return packagedproductdefinition.PackagedProductDefinition(js)

    def testPackagedProductDefinition1(self):
        inst = self.instantiate_from("packagedproductdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PackagedProductDefinition instance")
        self.implPackagedProductDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("PackagedProductDefinition", js["resourceType"])
        inst2 = packagedproductdefinition.PackagedProductDefinition(js)
        self.implPackagedProductDefinition1(inst2)

    def implPackagedProductDefinition1(self, inst):
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.period.end.date, FHIRDate("2016-06-06").date)
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.period.end.as_json(), "2016-06-06")
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.system, "http://ema.europa.eu/example/baid1")
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.value, "AAF5699")
        self.assertEqual(inst.description, "ALU-PVC/PVDC BLISTERS. CARTONS OF 10 FILM-COATED TABLETS. ")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://ema.europa.eu/example/pcid")
        self.assertEqual(inst.identifier[0].value, "{PCID}")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.package[0].characteristic[0].code.coding[0].code, "height")
        self.assertEqual(inst.package[0].characteristic[0].valueQuantity.unit, "mm")
        self.assertEqual(inst.package[0].characteristic[0].valueQuantity.value, 50)
        self.assertEqual(inst.package[0].characteristic[1].code.coding[0].code, "width")
        self.assertEqual(inst.package[0].characteristic[1].valueQuantity.unit, "mm")
        self.assertEqual(inst.package[0].characteristic[1].valueQuantity.value, 136)
        self.assertEqual(inst.package[0].characteristic[2].code.coding[0].code, "width")
        self.assertEqual(inst.package[0].characteristic[2].valueQuantity.unit, "mm")
        self.assertEqual(inst.package[0].characteristic[2].valueQuantity.value, 45)
        self.assertEqual(inst.package[0].characteristic[3].code.coding[0].code, "depth")
        self.assertEqual(inst.package[0].characteristic[3].valueQuantity.unit, "mm")
        self.assertEqual(inst.package[0].characteristic[3].valueQuantity.value, 23.5)
        self.assertEqual(inst.package[0].material[0].coding[0].code, "PVC")
        self.assertEqual(inst.package[0].material[0].coding[0].system, "http://ema.europa.eu/example/packageItemContainerMaterial")
        self.assertEqual(inst.package[0].material[1].coding[0].code, "PVDC")
        self.assertEqual(inst.package[0].material[1].coding[0].system, "http://ema.europa.eu/example/packageItemContainerMaterial")
        self.assertEqual(inst.package[0].material[2].coding[0].code, "alu")
        self.assertEqual(inst.package[0].material[2].coding[0].system, "http://ema.europa.eu/example/packageItemContainerMaterial")
        self.assertEqual(inst.package[0].package[0].characteristic[0].code.coding[0].code, "height")
        self.assertEqual(inst.package[0].package[0].characteristic[0].valueQuantity.unit, "mm")
        self.assertEqual(inst.package[0].package[0].characteristic[0].valueQuantity.value, 125)
        self.assertEqual(inst.package[0].package[0].characteristic[1].code.coding[0].code, "width")
        self.assertEqual(inst.package[0].package[0].characteristic[1].valueQuantity.unit, "mm")
        self.assertEqual(inst.package[0].package[0].characteristic[1].valueQuantity.value, 45)
        self.assertEqual(inst.package[0].package[0].containedItem[0].amountInteger, 12)
        self.assertEqual(inst.package[0].package[0].material[0].coding[0].code, "Paperboard")
        self.assertEqual(inst.package[0].package[0].material[0].coding[0].system, "http://ema.europa.eu/example/packageItemContainerMaterial")
        self.assertEqual(inst.package[0].package[0].quantity.unit, "1")
        self.assertEqual(inst.package[0].package[0].quantity.value, 1)
        self.assertEqual(inst.package[0].package[0].shelfLifeStorage[0].period.unit, "a")
        self.assertEqual(inst.package[0].package[0].shelfLifeStorage[0].period.value, 3)
        self.assertEqual(inst.package[0].package[0].shelfLifeStorage[0].specialPrecautionsForStorage[0].coding[0].code, "Thismedicinalproductdoesnotrequireanyspecialstoragecondition.")
        self.assertEqual(inst.package[0].package[0].shelfLifeStorage[0].specialPrecautionsForStorage[0].coding[0].system, "http://ema.europa.eu/example/specialprecautionsforstorage")
        self.assertEqual(inst.package[0].package[0].shelfLifeStorage[0].type.coding[0].code, "ShelfLifeofPackagedMedicinalProduct")
        self.assertEqual(inst.package[0].package[0].shelfLifeStorage[0].type.coding[0].system, "http://ema.europa.eu/example/shelfLifeTypePlaceHolder")
        self.assertEqual(inst.package[0].package[0].type.coding[0].code, "Blister")
        self.assertEqual(inst.package[0].package[0].type.coding[0].system, "http://ema.europa.eu/example/packageitemcontainertype")
        self.assertEqual(inst.package[0].quantity.unit, "1")
        self.assertEqual(inst.package[0].quantity.value, 1)
        self.assertEqual(inst.package[0].type.coding[0].code, "Carton")
        self.assertEqual(inst.package[0].type.coding[0].system, "http://ema.europa.eu/example/packageitemcontainertype")
        self.assertEqual(inst.text.status, "generated")

if __name__ == '__main__':
    unittest.main()