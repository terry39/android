#!/usr/bin/env python

# -*- coding: utf-8 -*-
#+---------------------------------------------------------------------------+
#|                                                                           |
#|                          Android's Hooker                                 |
#|                                                                           |
#+---------------------------------------------------------------------------+
#| Copyright (C) 2011 Georges Bossert and Dimitri Kirchner                   |
#| This program is free software: you can redistribute it and/or modify      |
#| it under the terms of the GNU General Public License as published by      |
#| the Free Software Foundation, either version 3 of the License, or         |
#| (at your option) any later version.                                       |
#|                                                                           |
#| This program is distributed in the hope that it will be useful,           |
#| but WITHOUT ANY WARRANTY; without even the implied warranty of            |
#| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              |
#| GNU General Public License for more details.                              |
#|                                                                           |
#| You should have received a copy of the GNU General Public License         |
#| along with this program. If not, see <http://www.gnu.org/licenses/>.      |
#+---------------------------------------------------------------------------+
#| @url      : http://www.amossys.fr                                         |
#| @contact  : android-hooker@amossys.fr                                     |
#| @sponsors : Amossys, http://www.amossys.fr                                |
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+
# Imports
#+---------------------------------------------------------------------------+
from setuptools import setup, find_packages
from apk_retriever import release


#+---------------------------------------------------------------------------+
# Definition of the project
#+---------------------------------------------------------------------------+
setup(
    name = release.name,
    packages = find_packages(where='apk_retriever'),
    scripts = ["apk_retriever.py"],
    version = release.version,
    license = release.licenseName,
    description = release.description,
    author = release.author,
    author_email = release.author_email,
    url = release.url,
    download_url = release.download_url,
    keywords = release.keywords
)
    
    

