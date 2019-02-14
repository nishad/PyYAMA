# Development Repository for YAMA Python Toolkit

**YAMA (Yet Another Metadata Application Profile)** is a user-friendly interoperable preprocessor for creating, maintaining and publishing Metadata Application Profiles. YAMA helps to produce various formats and standards to express the Metadata Application Profiles, change-logs, and different versions, with an expectation of simplifying Metadata Application Profile creation process for domain experts. YAMA includes an integrated syntax for recording application profiles as well as changes between different versions.

### Python Development environment for YAMA

Development environment is Anaconda Python with Python 3.7
Python virtual environment named `yama-dev` can be created via

``` bash
conda env create -f dev/yama-dev_conda_environment.yaml
```

To activate this environment, use:
    
    source activate yama-dev

To deactivate an active environment, use:

    source deactivate
    
To install requirements

    pip install -r requirements.txt

To install development requirements

    pip install -r dev/requirements-dev.txt