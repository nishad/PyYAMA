.. YAMA documentation master file, created by
   sphinx-quickstart on Thu Sep 20 08:49:37 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Yet Another Metadata Application Profile
========================================

YAMA - a simple preprosessor markup for 
Metadata Application Profiles.

Yet Another Metadata Application Profile (YAMA) as a user-friendly 
interoperable preprocessor for creating, maintaining and publishing 
Metadata Application Profiles.  YAMA helps to produce various formats and standards to express the Metadata Application Profiles, change-logs, and different versions, with an expectation of simplifying Metadata Application Profile creation process for domain experts. YAMA includes an integrated syntax for recording application profiles as well as changes between different versions.

YAMA makes it easy to
maintain machine and human friendly metadata specific documets such as
but not limited to `DC Metadata applicaion profile DSP`_. 

Usage:
    YAMA can be accessed as a Python module or easily invoked as a
    commandline tool::

        $ pip install yama
        $ yama --help
        $ yama [command] [options] [attributes]

YAMA can be used within Python scripts to extent the functionality,
and integrate other Python modules to enhance or customize desired operations.

YAMA is proposed as part of various metadata application profile formats and specification
creation workflows.

Commands:
    validate: Validate is a general purpose validation command for YAMA formats.
        If there is no specific type option is defined, yama will attempt to
        identify the type of yama document from ``type`` value declared inside
        given YAMA document.

    render: Render an YAMA document with provided template. YAMA natively
        supports Mustache and Jinja2 templates.

    generate: Generate a predefied output format from given YAMA docuement.
        All available formats can be listed via ``--help`` option.

YAMA CLI::

  Usage: yama [OPTIONS]

  Options:
    -i, --yama-input-file PATH  YAMA Input File  [required]
    -t, --template-file PATH    Template File  [required]
    -o, --output PATH           Save output to file
    --help                      Show this message and exit.


.. _DC Metadata applicaion profile DSP:
   http://dublincore.org/documents/2008/03/31/dc-dsp/
.. _CSVW:
   https://www.w3.org/TR/2016/NOTE-tabular-data-primer-20160225/

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
------------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
