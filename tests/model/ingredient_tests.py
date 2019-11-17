#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 on 2019-11-17.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from model import ingredient
from model.fhirdate import FHIRDate


class IngredientTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Ingredient", js["resourceType"])
        return ingredient.Ingredient(js)

    def testIngredient1(self):
        inst = self.instantiate_from("ingredient-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Ingredient instance")
        self.implIngredient1(inst)

        js = inst.as_json()
        self.assertEqual("Ingredient", js["resourceType"])
        inst2 = ingredient.Ingredient(js)
        self.implIngredient1(inst2)

    def implIngredient1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.role.coding[0].code, "ActiveBase")
        self.assertEqual(inst.role.coding[0].system, "http://ema.europa.eu/example/ingredientRole")
        self.assertEqual(inst.specifiedSubstance[0].codeCodeableConcept.coding[0].code, "equixabanCompanyequixaban1")
        self.assertEqual(inst.specifiedSubstance[0].codeCodeableConcept.coding[0].system, "http://ema.europa.eu/example/specifiedSubstance")
        self.assertEqual(inst.specifiedSubstance[0].group.coding[0].code, "2")
        self.assertEqual(inst.specifiedSubstance[0].group.coding[0].system, "http://ema.europa.eu/example/specifiedSubstanceGroup")
        self.assertEqual(inst.substance.codeCodeableConcept.coding[0].code, "EQUIXABAN")
        self.assertEqual(inst.substance.codeCodeableConcept.coding[0].system, "http://ema.europa.eu/example/substance")
        self.assertEqual(inst.substance.strength[0].presentation.denominator.unit, "{tablet}")
        self.assertEqual(inst.substance.strength[0].presentation.denominator.value, 1)
        self.assertEqual(inst.substance.strength[0].presentation.numerator.unit, "mg")
        self.assertEqual(inst.substance.strength[0].presentation.numerator.value, 2.5)
        self.assertEqual(inst.text.status, "generated")

if __name__ == '__main__':
    unittest.main()