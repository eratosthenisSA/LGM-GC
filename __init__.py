# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoCoding
                                 A QGIS plugin
 Machine Learning Geocoding
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-12-18
        copyright            : (C) 2019 by Eratosthenis SA 2019
        email                : iliasvrk@gmail.com
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GeoCoding class from file GeoCoding.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .geocoding import GeoCoding
    return GeoCoding(iface)
