"""
 The config module contains the Config class, which is passed to
the Welkin V8 API calls. It stores useful information such as your API client name, tenant name,
instance name, secret and environment(stg/live).

It is suggested that you create a single Config object in
your project and pass that to the various API calls, rather than create new
Config objects. This is merely a design suggestion, treat it as such.
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
