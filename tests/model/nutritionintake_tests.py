#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 on 2019-11-18.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from model import nutritionintake
from model.fhirdate import FHIRDate


class NutritionIntakeTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("NutritionIntake", js["resourceType"])
        return nutritionintake.NutritionIntake(js)

    def testNutritionIntake1(self):
        inst = self.instantiate_from("nutritionintake-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionIntake instance")
        self.implNutritionIntake1(inst)

        js = inst.as_json()
        self.assertEqual("NutritionIntake", js["resourceType"])
        inst2 = nutritionintake.NutritionIntake(js)
        self.implNutritionIntake1(inst2)

    def implNutritionIntake1(self, inst):
        self.assertEqual(inst.category[0].text, "Inpatient")
        self.assertEqual(inst.consumedItem[0].amount.code, "%")
        self.assertEqual(inst.consumedItem[0].amount.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.consumedItem[0].amount.unit, "percent")
        self.assertEqual(inst.consumedItem[0].amount.value, 100)
        self.assertEqual(inst.consumedItem[0].nutritionProduct.text, "Grill Sandwich")
        self.assertEqual(inst.consumedItem[0].type.text, "food")
        self.assertEqual(inst.consumedItem[1].amount.code, "%")
        self.assertEqual(inst.consumedItem[1].amount.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.consumedItem[1].amount.unit, "percent")
        self.assertEqual(inst.consumedItem[1].amount.value, 100)
        self.assertEqual(inst.consumedItem[1].nutritionProduct.text, "French Fries Spiral Battered")
        self.assertEqual(inst.consumedItem[1].type.text, "food")
        self.assertEqual(inst.consumedItem[2].amount.code, "%")
        self.assertEqual(inst.consumedItem[2].amount.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.consumedItem[2].amount.unit, "percent")
        self.assertEqual(inst.consumedItem[2].amount.value, 50)
        self.assertEqual(inst.consumedItem[2].nutritionProduct.text, "Tomato Soup Healthy Request")
        self.assertEqual(inst.consumedItem[2].type.text, "food")
        self.assertEqual(inst.consumedItem[3].amount.code, "%")
        self.assertEqual(inst.consumedItem[3].amount.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.consumedItem[3].amount.unit, "percent")
        self.assertEqual(inst.consumedItem[3].amount.value, 50)
        self.assertEqual(inst.consumedItem[3].nutritionProduct.text, "Side Garden Salad")
        self.assertEqual(inst.consumedItem[3].type.text, "food")
        self.assertEqual(inst.consumedItem[4].amount.code, "%")
        self.assertEqual(inst.consumedItem[4].amount.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.consumedItem[4].amount.unit, "percent")
        self.assertEqual(inst.consumedItem[4].amount.value, 100)
        self.assertEqual(inst.consumedItem[4].nutritionProduct.text, "Ice Tea Unsweetened")
        self.assertEqual(inst.consumedItem[4].type.text, "fluid")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2019-08-02T12:45:18+04:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2019-08-02T12:45:18+04:00")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.ingredientLabel[0].amount.code, "kcal")
        self.assertEqual(inst.ingredientLabel[0].amount.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.ingredientLabel[0].amount.unit, "kilocalorie")
        self.assertEqual(inst.ingredientLabel[0].amount.value, 313)
        self.assertEqual(inst.ingredientLabel[0].nutrient.text, "Total Calories")
        self.assertEqual(inst.ingredientLabel[1].amount.code, "g")
        self.assertEqual(inst.ingredientLabel[1].amount.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.ingredientLabel[1].amount.unit, "grams")
        self.assertEqual(inst.ingredientLabel[1].amount.value, 10.4)
        self.assertEqual(inst.ingredientLabel[1].nutrient.text, "Protein")
        self.assertEqual(inst.ingredientLabel[2].amount.code, "g")
        self.assertEqual(inst.ingredientLabel[2].amount.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.ingredientLabel[2].amount.unit, "grams")
        self.assertEqual(inst.ingredientLabel[2].amount.value, 18.0)
        self.assertEqual(inst.ingredientLabel[2].nutrient.text, "Fat (Total)")
        self.assertEqual(inst.ingredientLabel[3].amount.code, "g")
        self.assertEqual(inst.ingredientLabel[3].amount.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.ingredientLabel[3].amount.unit, "grams")
        self.assertEqual(inst.ingredientLabel[3].amount.value, 26.47)
        self.assertEqual(inst.ingredientLabel[3].nutrient.text, "Carbohydrate")
        self.assertEqual(inst.ingredientLabel[4].amount.code, "mg")
        self.assertEqual(inst.ingredientLabel[4].amount.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.ingredientLabel[4].amount.unit, "Milligrams")
        self.assertEqual(inst.ingredientLabel[4].amount.value, 770)
        self.assertEqual(inst.ingredientLabel[4].nutrient.text, "Sodium")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")

if __name__ == '__main__':
    unittest.main()