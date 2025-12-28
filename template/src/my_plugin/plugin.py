from qgis.PyQt.QtWidgets import QAction, QMessageBox


class MyPlugin:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        self.iface = iface
        self.action = None

    def initGui(self):  # noqa: N802
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        self.action = QAction("My Plugin", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu("&My Plugin", self.action)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        if self.action:
            self.iface.removePluginMenu("&My Plugin", self.action)
            self.iface.removeToolBarIcon(self.action)

    def run(self):
        """Run method that performs all the real work."""
        QMessageBox.information(
            self.iface.mainWindow(),
            "My Plugin",
            "Plugin running successfully!",
        )
