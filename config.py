"""
 The config module contains the Config class, which is passed to
the Welkin V8 API calls. It stores useful information such as your API client name, tenant name,
instance name, secret and environment(stg/live).

This file holds various configuration options used for all of the examples.
You will need to change the values below.
"""


class Config(object):
    """common configuration"""

    # organization (Tenant)
    tenantName = ""
    # API Client name
    apiClientName = ""
    SECRET = ""

    # Instance (Environment)
    instanceName = ""
       # stg/live
    ENV = ""
