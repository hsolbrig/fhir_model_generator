#!/bin/bash

pipenv install -d

# set this to a relative path, from inside the fhirclient/models directory, to the downloaded FHIR spec directory
export FHIR_UNITTEST_DATADIR="downloads"

if [ ! -e $FHIR_UNITTEST_DATADIR ]; then
	echo Unit tests depend on the downloaded FHIR spec, which is not present at $FHIR_UNITTEST_DATADIR. Cannot run unit tests.
	exit 1
fi

#python -m unittest discover ./models '*_tests.py'		# ImportError
tests=(tests/model/*_tests.py)
pipenv run python -m unittest "${tests[@]}"

# couple of custom tests
pipenv run python -m unittest tests/server_tests.py tests/fhirreference_tests.py
