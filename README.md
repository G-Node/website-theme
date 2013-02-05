website-theme
=============

A Plone theme for the G-Node website

Plone 3 to 4: migration log
===========================

- fresh 4.2 installation (http://plone.org/documentation/manual/installing-plone/installation-quick-guide). Verify installation works
- install plone.app.ldap (http://pypi.python.org/pypi/plone.app.ldap) and re-run buildout (sudo ./bin/buildout)
- pack the old Zope database using ZMI (http://<zope-root>/manage, user/password is in <instance>/adminPassword.txt) control panel -> Database -> main -> pack
- stop old Plone 3 site (sudo ./bin/plonectl stop). Backup old DB (<instance>/var/filestorage/Data.fs)
- remoe LDAP plugin using ZMI from the old site (delete /<site-name>/acl_users/PloneLDAP)
- export plone site (<instance>/current/zeocluster/var/client2/Plone.zexp)
- place exported file to the <instance>/zinstance/var/instance/import
- import plone site to the fresh Plone 4 installation in the ZMI root
- go to the site page in the ZMI, upgrade from the ZMI (should be an upgrade button)
- go to the imported site/acl_users in the ZMI and add 'Plone LDAP plugin'
- configure this plugin to work with gate.g-node.org from the ZMI
  - http://<site-url>/acl_users/G-Node-LDAP/acl_users/manage_main
  - use gate.g-node.org:389 for servers outside g-node, and ds.g-node.pri:389 inside G-Node network
- validate LDAP auth works
- make changes to the theme (commit f0ab7fb4c2615b6f3733d3c97a02c3fc05dd0537 Tue Feb 5 12:31:30 2013)
- stop the Zope server
- re-run buildout, restart the Zope server
- hide unused viewlets: http://<site-url>/@@manage-viewlets
- validate site is fully functional

Useful links
============

updating theme
- http://plone.org/documentation/manual/upgrade-guide/version/upgrading-plone-3-x-to-4.0/updating-add-on-products-for-plone-4.0/updating-plone-3-themes-for-plone-4
- http://plone.org/documentation/kb/how-to-write-templates-for-plone-4

copying site
- http://plone.org/documentation/kb/copying-a-plone-site
- http://plone.org/documentation/manual/installing-plone/installation-quick-guide
