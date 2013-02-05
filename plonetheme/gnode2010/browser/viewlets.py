from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common
from plone.app.layout.viewlets.common import ViewletBase

# Sample code for a basic viewlet (In order to use it, you'll have to):
# - Un-comment the following useable piece of code (viewlet python class).
# - Rename the viewlet template file ('browser/viewlet.pt') and edit the
#   following python code accordingly.
# - Edit the class and template to make them suit your needs.
# - Make sure your viewlet is correctly registered in 'browser/configure.zcml'.
# - If you need it to appear in a specific order inside its viewlet manager,
#   edit 'profiles/default/viewlets.xml' accordingly.
# - Restart Zope.
# - If you edited any file in 'profiles/default/', reinstall your package.
# - Once you're happy with your viewlet implementation, remove any related
#   (unwanted) inline documentation  ;-p

#class MyViewlet(ViewletBase):
#    render = ViewPageTemplateFile('viewlet.pt')
#
#    def update(self):
#        self.computed_value = 'any output'

#class PersonalBarViewlet(ViewletBase):
class PersonalBarViewlet(common.PersonalBarViewlet):
    """
    A custom version of the personal bar class.
    Just to overwrite the template.
    """
    index = ViewPageTemplateFile('personal_bar.pt')

class LogoGNode(ViewletBase):
    """
    A g-node logo picture with a link to the G-Node homepage.
    """
    index = ViewPageTemplateFile('logo_gnode.pt')

class LogoPartner(ViewletBase):
    """
    A g-node partner logo picture with a link to the G-Node homepage.
    """
    index = ViewPageTemplateFile('logo_partner.pt')
