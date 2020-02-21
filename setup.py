from setuptools import setup, find_packages
from glob import glob
import os
import sys
from os.path import join, abspath, dirname, isfile, isdir

local_path = dirname(abspath(__file__))
# setup.py can be called from outside the oniapostproc directory
os.chdir(local_path)
sys.path.insert(0, local_path)

setup(
        name="wickpy",
        version="0.1",
        packages=find_packages(),

        # Project uses reStructuredText, so ensure that the docutils get
        # installed or upgraded on the target machine
        install_requires=['numpy', 'cv2', 'sympy', 'PIL'],

        package_data={
            # If any package contains *.txt or *.rst files, include them:
            '': ['*.txt', '*.rst'],
            },
        #data_files=[
            #('plotstyle', glob('plotstyle/*')),
            #('.',['config.yml']),
            #],
        #scripts=glob('scripts/*'),

        # metadata to display on PyPI
        author="Bakar Chargeishvili",
        author_email="bakar.chargeishvili@physnet.uni-hamburg.de",
        description="Wick contraction demonstration, correlation function calculator, feynman diagrams",
        url="https://github.com/rakab/wickpy",   # project home page, if any
        license = "BSD",
        classifiers=[
            'License :: OSI Approved :: BSD License'
            ]

        # could also include long_description, download_url, etc.
        )
