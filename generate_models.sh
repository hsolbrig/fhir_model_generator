#!/bin/bash

pipenv install

pushd fhir-parser-resources || exit
cp template-codesystems.j2 template-codesystems.py
cp template-elementfactory.j2 template-elementfactory.py
cp template-resource.j2 template-resource.py
cp template-unittest.j2 template-unittest.py
popd || exit

pipenv run generate fhir-parser-resources "$@"

pushd fhir-parser-resources || exit
rm template-codesystems.py
rm template-elementfactory.py
rm template-resource.py
rm template-unittest.py
popd || exit
