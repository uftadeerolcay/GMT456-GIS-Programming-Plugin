# -*- coding: utf-8 -*-
"""
/***************************************************************************
 group10
                                 A QGIS plugin
 group10
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-12-24
        copyright            : (C) 2021 by group10
        email                : emreabaogluu@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

from .group10 import group10
# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load group10 class from file group10.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    return group10(iface)