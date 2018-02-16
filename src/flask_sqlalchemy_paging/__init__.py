"""
Define a configuration and import top-level functions/classes
"""
SETTINGS = {
  'DEFAULT_PAGE_SIZE': None,
  'ALLOW_PAGE_SIZE_QUERY_PARAM': True,
  'ALLOW_UNLIMITED_PAGE_SIZE': True
}

def configure(configuration):
    """
    Configures the package with a dictionary of key/value
    settings.
    :param configuration: The settings to apply
    :type configuration: dict
    """
    global SETTINGS
    SETTINGS = {**SETTINGS, **configuration}

