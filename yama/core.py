# -*- coding: utf-8 -*-

from ruamel.yaml import YAML
import copy
from jinja2 import Template


def expand_namespace(namespaces, description_property):
    """Function to expand namespaces

    Args:
        namespaces (dict): namespaces dictionary
        description_property (str): Exapanded namespace for property.

    Returns:
        uri+property(str): Returns an expanded property string with URI.

    """
    property_prefix, property_property = description_property.split(":")
    for prefix, uri in namespaces.items():
        if prefix == property_prefix:
            return uri + property_property


def generate_statements(statements_dictionary, namespaces):
    """Function to generate statements

    Args:
        namespaces (dict): namespaces dictionary
        statements_dictionary (dict): Dictionary of statements.

    Returns:
        statemets(dict): Updated statements dictionary.

    """
    statements = {}
    for statement_id, statement in statements_dictionary.items():
        statement['property'] = expand_namespace(
            namespaces, statement['property'])
        statements[statement_id] = statement
    return statements


def generate_descriptions(descriptions_dictionary, statements_dictionary):
    """Function to generate description

    Args:
        descriptions_dictionary (dict): Dictionary of statements
        statements_dictionary (dict): Dictionary of statements.

    Returns:
        descriptions (dict): Updated descriptions dictionary.

    """
    descriptions = {}
    for description_id, description in descriptions_dictionary.items():
        statement_list = description['statements']
        description['statements'] = {}
        for statement in statement_list:
            description['statements'][statement] = copy.deepcopy(
                statements_dictionary[statement])
        descriptions[description_id] = description
    return descriptions


def generate_description_set(description_set, descriptions_dictionary):
    """Function to generate description set

    Args:
        descriptions_set (dict): Dictionary of description set
        descriptions_dictionary (dict): Dictionary of descriptions.

    Returns:
        descriptionset(dict): Updated description set dictionary.

    """
    descriptionset = {}
    description_list = description_set['descriptions']
    description_set['descriptions'] = {}
    for description in description_list:
        description_set['descriptions'][description] = copy.deepcopy(
            descriptions_dictionary[description])
    descriptionset = description_set
    return descriptionset


class YAMA:
    """YAMA Core class.

    `YAMA` call is used to handle YAMA docuemnts through a
    YAMA object. This object can be hadled Application Profiles
    programatically.

    Args:
        yama_file (str): Accessible location of a YAMA file, this YAMA docuemnt
        will be parsed and the Application Profile object will be returend.

    Returns:
        YAMA (object): Extandable Application Profile object is
        returned.
    """
    def __init__(self, yama_file):
        yaml = YAML(typ='safe')
        with open(yama_file, 'r') as ymlfile:
            dsp = yaml.load(ymlfile)
        dspm = {}
        dspm['description_set'] = copy.deepcopy(dsp['description_set'])
        namespaces = dsp['namespaces']
        statements_dictionary = copy.deepcopy(dsp['statements'])
        descriptions_dictionary = copy.deepcopy(dsp['descriptions'])
        statements = generate_statements(statements_dictionary, namespaces)
        descriptions = generate_descriptions(
            descriptions_dictionary, statements)
        description_set = copy.deepcopy(dsp['description_set'])
        new_dsp = generate_description_set(description_set, descriptions)
        self.dsp = new_dsp

    def render(self, template_file):
        """A renderer for Application Profile Object, which will render
        any given template to specific output.

        Note:
            At this stage of development, only Jinja2 templates are
            supported.

        Args:
            template_file: Location of the template file.

        Returns:
            A rendered output of the DSP using provided template.
        """
        with open(template_file) as file_:
            template = Template(file_.read())
        return (template.render(dsp=self.dsp))

    def version(self):
        """Access the version number of DSP, if the version is declared
        in the YAMA docuemnt.

        Note:
            This methode will be expanded to deal with automatic
            versioning.

        Returns:
            Version of the Application Profile declared in the
            YAMA docuemnt.

        """
        return self.dsp.get('version')
