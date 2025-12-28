
def test_plugin_load():
    """Test that the plugin can be imported."""
    from src.my_plugin import classFactory
    assert classFactory is not None

def test_qgis_environment(qgis_iface):
    """Test that QGIS environment is available."""
    assert qgis_iface is not None
