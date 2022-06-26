# coding= utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at
     http=//www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

from os import path

from setuptools import setup, find_packages

NAME = "netbox-juniper-srx"
VERSION = "0.0.3"
AUTHOR = "Calvin Remsburg"
AUTHOR_EMAIL = "cremsburg.dev@gmail.com"
URL = "https://github.com/cdot65/netbox-juniper-srx"

DESCRIPTION = "Juniper SRX NetBox Plugin"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = []

OPTIONS = {"bdist_wheel": {"universal": True}}

setup(
    name=NAME,
    version=VERSION,
    options=OPTIONS,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache LICENSE 2.0",
    url=URL,
    keywords=["netbox", "juniper", "firewall", "srx", "all"],
    packages=find_packages(),
    platforms=["any"],
    install_requires=INSTALL_REQUIRES,
    python_requires=">=3.7.*",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Networking :: Firewalls",
        "Topic :: System :: Systems Administration",
    ],
)
