# -*- coding: utf-8 -*-


import os
import io
import json
import shutil
from pprint import pprint
from typing import List, Optional, Tuple

from tests import server
import unittest
import model.fhirabstractbase as fabst

filedir = os.path.dirname(__file__)


class TestServer(unittest.TestCase):
    
    def tearDown(self):
        if os.path.exists('metadata'):
            os.remove('metadata')
    
    def testValidCapabilityStatement(self):
        shutil.copyfile(os.path.join(filedir, 'test_metadata_valid.json'), 'metadata')
        mock = MockServer()
        mock.get_capability()
        
        self.assertIsNotNone(mock.auth._registration_uri)
        self.assertIsNotNone(mock.auth._authorize_uri)
        self.assertIsNotNone(mock.auth._token_uri)
    
    def testStateConservation(self):
        shutil.copyfile(os.path.join(filedir, 'test_metadata_valid.json'), 'metadata')
        mock = MockServer()
        self.assertIsNotNone(mock.capabilityStatement)
        
        fhir = server.FHIRServer(None, state=mock.state)
        self.assertIsNotNone(fhir.auth._registration_uri)
        self.assertIsNotNone(fhir.auth._authorize_uri)
        self.assertIsNotNone(fhir.auth._token_uri)
    
    def testInvalidCapabilityStatement(self):
        def build_error_tree(errors: List) -> List[Tuple[str, Optional[List]]]:
            return [(str(e).strip()[:76], build_error_tree(e.errors) if getattr(e, 'errors', None) is not None else None) for e in errors]
        shutil.copyfile(os.path.join(filedir, 'test_metadata_invalid.json'), 'metadata')
        mock = MockServer()
        try:
            mock.get_capability()
            self.assertTrue(False, "Must have thrown exception")
        except fabst.FHIRValidationError as e:
            self.assertListEqual(
                [('date:\n'
                  '  Wrong type <class \'list\'> for property "date" on <class \'model.capab',
                  [('Wrong type <class \'list\'> for property "date" on <class '
                    "'model.capabilitysta",
                    None)]),
                 ('format:\n'
                  '  Wrong type <class \'int\'> for list property "format" on <class \'mod',
                  [('Wrong type <class \'int\'> for list property "format" on <class '
                    "'model.capabil",
                    None)]),
                 ('rest.0:\n'
                  '  security:\n'
                  '    service.0:\n'
                  '      coding.0:\n'
                  '        Superfluous entry',
                  [('security:\n'
                    '  service.0:\n'
                    '    coding.0:\n'
                    '      Superfluous entry "systems" in da',
                    [('service.0:\n'
                      '  coding.0:\n'
                      '    Superfluous entry "systems" in data for Coding(id',
                      [('coding.0:\n'
                        '  Superfluous entry "systems" in data for Coding(id=None, extensio',
                        [('Superfluous entry "systems" in data for Coding(id=None, '
                          'extension=None, syst',
                          None)])])]),
                   ('operation.1:\n'
                    '  definition:\n'
                    '    Wrong type <class \'dict\'> for property "defin',
                    [('definition:\n'
                      '  Wrong type <class \'dict\'> for property "definition" on <class ',
                      [('Wrong type <class \'dict\'> for property "definition" on <class '
                        "'model.capabil",
                        None)])])]),
                 ('Superfluous entry "formats" in data for CapabilityStatement(id=None, '
                  'meta=No',
                  None)], build_error_tree(e.errors))


class MockServer(server.FHIRServer):
    """ Reads local files.
    """
    
    def __init__(self):
        super().__init__(None, base_uri='https://fhir.smarthealthit.org')
    
    def request_json(self, path, nosign=False):
        assert path
        with io.open(path, encoding='utf-8') as handle:
            return json.load(handle)
        
        return None
