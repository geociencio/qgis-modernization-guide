def classFactory(iface):  # noqa: N802
    """Load QGISPluginClass class from file QGISPluginClass.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .plugin import MyPlugin
    return MyPlugin(iface)
