import unittest

from ner_client import NamedEntityClient

from test_doubles import NerModelTestDouble


class TestNerClient(unittest.TestCase):

    def test_get_ents_returns_dict_given_empty_str_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dict_given_nonempty_str_causes_empty_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Bordeaux is in Nouvelle-Aquitaine")
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_returned_serialized_to_Person(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Laurent Fressinet', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)   
        ner = NamedEntityClient(model)
        ents = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'Laurent Fressinet', 'label': 'Person'}], 'html': ""}   
        self.assertListEqual(ents['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_NORP_is_returned_serialized_to_Group(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'French', 'label_': 'NORP'}]
        model.returns_doc_ents(doc_ents)   
        ner = NamedEntityClient(model)
        ents = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'French', 'label': 'Group'}], 'html': ""}   
        self.assertListEqual(ents['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_LOC_is_returned_serialized_to_Location(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Bordeaux', 'label_': 'LOC'}]
        model.returns_doc_ents(doc_ents)   
        ner = NamedEntityClient(model)
        ents = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'Bordeaux', 'label': 'Location'}], 'html': ""}   
        self.assertListEqual(ents['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_LANGUAGE_is_returned_serialized_to_Language(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'ASL', 'label_': 'LANGUAGE'}]
        model.returns_doc_ents(doc_ents)   
        ner = NamedEntityClient(model)
        ents = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'ASL', 'label': 'Language'}], 'html': ""}   
        self.assertListEqual(ents['ents'], expected_result['ents'])

    def test_get_ents_given_multiple_ents_serializes_all(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'ASL', 'label_': 'LANGUAGE'}, {'text': 'Bordeaux', 'label_': 'LOC'}]
        model.returns_doc_ents(doc_ents)   
        ner = NamedEntityClient(model)
        ents = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'ASL', 'label': 'Language'}, {'ent': 'Bordeaux', 'label': 'Location'}], 'html': ""}   
        self.assertListEqual(ents['ents'], expected_result['ents'])
