#!/usr/bin/python
#
# Copyright (c) Arnau Sanchez <tokland@gmail.com>

# This script is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>
from setuptools import setup, find_packages
import os
from distutils.cmd import Command

version = '1.10'
url = "https://github.com/kiorky/spynner"

class gen_doc(Command):
    """Generate the HTML API documentation using epydoc

    Output files to docs/api.
    """
    description = "generate the api doc"
    user_options = []
    target_dir = "docs/api"
    source = ["spynner/browser.py"]

    def initialize_options(self):
        self.all = None

    def finalize_options(self):
        pass

    def run(self):
        os.system("epydoc -v --html --fail-on-docstring-warning --no-private " +
                  "--no-sourcecode -n spynner -u %s -o %s %s" %
                  (url, self.target_dir, " ".join(self.source)))


def read(rnames):
    setupdir =  os.path.dirname( os.path.abspath(__file__))
    return open(
        os.path.join(setupdir, rnames)
    ).read()

setup(
    name="spynner",
    version=version,
    description="Programmatic web browsing module with AJAX support for Python",
    author="Arnau Sanchez, Mathieu Le Marec-Pasquet",
    author_email="tokland@gmail.com, kiorky@cryptelium.net",
    url=url,
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires=['BeautifulSoup', 'pyquery'],
    cmdclass={'gen_doc': gen_doc},
    scripts=[],
    license="GPL v3.0",
    long_description = (
        read('README.rst')
        + '\n' +
        read('CHANGES.txt')
        + '\n'
    ),
    include_package_data=True,
    data_files = [
        ('share/doc/spynner/examples',
            ('examples/wordreference.py',
            'examples/webkit_methods.py',
            'examples/native_events.py',
            'examples/google.py',)),
        #('share/spynner/javascript',
        #    ('src/spynner/javascript/jquery.min.js',
        #     'src/spynner/javascript/jquery.simulate.js')),
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
