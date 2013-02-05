"""

# from Plone 3:

from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    # Marker interface that defines a Zope 3 browser layer.
    # If you need to register a viewlet only for the
    # "gnode2010" theme, this interface must be its layer
    # (in gnode2010/viewlets/configure.zcml).

"""

from plonetheme.classic.browser.interfaces import IThemeSpecific as IClassicTheme

class IThemeSpecific(IClassicTheme):
    """theme-specific layer"""
