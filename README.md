website-theme
=============

A Plone theme for the G-Node website

Setup of the new site
=====================

1. copy ALL with permissions (scp -rp ..)

2. verify user

3. run ./bin/buildout

4. configure LDAP
 - http://hal10:8080/Plone/acl_users/G-Node-LDAP/acl_users/manage_main
 - use gate.g-node.org:389 for servers outside g-node, and ds.g-node.pri:389

5. start by ./bin/plonectl start


Useful links:
http://plone.org/documentation/kb/copying-a-plone-site
http://plone.org/documentation/manual/installing-plone/installation-quick-guide
