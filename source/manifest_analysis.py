
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" AndroidManifest.xml analysis module. """

import os
import xml.dom.minidom
from source.settings import DATABASE_DIR
from source.report import generate_report
from source.parser_manifest import (
    get_package,
    get_version_code,
    get_version_name,
    get_uses_feature,
    get_uses_sdk,
    get_permission,
    get_uses_permission,
    get_uses_permission_sdk23,
    get_services,
    get_receivers,
    get_providers
)


def manifest_analysis():
    """
    Android Manifest Analysis.
    
    Tags:
    - <uses-sdk>
    - <uses-feature>
    - <permission>
    - <uses-permission>
    - <uses-permission-sdk23>
    - <service>
    - <receiver>
    - <provider>    
    """
    database = os.listdir(DATABASE_DIR)
    for app_folder in database:
        manifest_xml = xml.dom.minidom.parse(DATABASE_DIR + app_folder + '/AndroidManifest.xml')

        # app basic information
        app_basic_info_list = []
        package_name = get_package(manifest_xml)
        version_code = get_version_code(manifest_xml)
        version_name = get_version_name(manifest_xml)
        app_basic_info = (package_name, version_code, version_name)
        app_basic_info_list.append(app_basic_info)

        # get <uses-sdk> data
        uses_sdk = get_uses_sdk(manifest_xml)

        # get <uses-feature> data
        uses_feature = get_uses_feature(manifest_xml)

        # get <permission> data
        permission = get_permission(manifest_xml)

        # get <uses-permission> data
        uses_permission = get_uses_permission(manifest_xml)

        # get <uses-permission-sdk23> data
        uses_permission_sdk23 = get_uses_permission_sdk23(manifest_xml)

        # get <service> data
        services = get_services(manifest_xml)

        # get <receiver> data
        receivers = get_receivers(manifest_xml)

        # get <provider> data
        providers = get_providers(manifest_xml)

        # Generate report
        generate_report(app_folder,                 # APK filename
                        app_basic_info_list,        # Basic information of an APK
                        uses_sdk,                   # <uses-sdk>
                        uses_feature,               # <uses-feature>
                        permission,                 # <permission>
                        uses_permission,            # <uses-permission>
                        uses_permission_sdk23,      # <uses-permission-sdk23>
                        services,                   # <service>
                        receivers,                  # <receiver>
                        providers)                  # <provider>
