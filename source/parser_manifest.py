
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
AndroidManifest.xml Parser
'''

def get_package(manifest_xml):
    '''
    Get APK package from AndroidManifest.xml

    @param manifest_xml: manifest xml dom
    @type  manifest_xml: xml dom

    @return: package name
    @rtype: str
    '''
    manifest = get_manifest_element(manifest_xml)
    packagename = manifest.getAttribute('package')
    return packagename


def get_version_code(manifest_xml):
    '''
    Get APK versionCode from AndroidManifest.xml

    @param manifest_xml: manifest xml dom
    @type  manifest_xml: xml dom

    @return: version code
    @rtype: str
    '''
    manifest = get_manifest_element(manifest_xml)
    versioncode = manifest.getAttribute('android:versionCode')
    return versioncode


def get_version_name(manifest_xml):
    '''
    Get APK versionName from AndroidManifest.xml

    @param manifest_xml: manifest xml dom
    @type  manifest_xml: xml dom

    @return: version name
    @rtype: str
    '''
    manifest = get_manifest_element(manifest_xml)
    versionname = manifest.getAttribute('android:versionName')
    return versionname


def get_uses_feature(manifest_xml):
    '''
    Get APK <uses-feature> attributes from AndroidManifest.xml
    See: https://developer.android.com/guide/topics/manifest/uses-feature-element

    @param manifest_xml: manifest xml dom
    @type  manifest_xml: xml dom

    @return: uses-feature
    @rtype: list
    '''
    uses_feature_list = []
    uses_features = manifest_xml.getElementsByTagName('uses-feature')
    if uses_features:
        for uses_feature in uses_features:
            # uses-feature attributes
            name = uses_feature.getAttribute('android:name')
            required = uses_feature.getAttribute('android:required')
            gles_version = uses_feature.getAttribute('android:glEsVersion')

            # uses-feature information list
            uses_feature_info = (name,
                                 required,
                                 gles_version)
            uses_feature_list.append(uses_feature_info)

    return uses_feature_list


def get_uses_sdk(manifest_xml):
    '''
    Get APK <uses-sdk> attributes from AndroidManifest.xml
    See: https://developer.android.com/guide/topics/manifest/uses-sdk-element

    @param manifest_xml: manifest xml dom
    @type  manifest_xml: xml dom

    @return: uses-sdk
    @rtype: list
    '''
    uses_sdk_list = []
    uses_sdks = manifest_xml.getElementsByTagName('uses-sdk')
    if uses_sdks:
        for uses_feature in uses_sdks:
            # uses-sdk attributes
            minsdkversion = uses_feature.getAttribute('android:minSdkVersion')
            targetsdkversion = uses_feature.getAttribute('android:targetSdkVersion')
            maxsdkversion = uses_feature.getAttribute('android:maxSdkVersion')

            # uses-sdk information list
            uses_sdk_info = (minsdkversion,
                             targetsdkversion,
                             maxsdkversion)
            uses_sdk_list.append(uses_sdk_info)

    return uses_sdk_list


def get_permission(manifest_xml):
    '''
    Get APK <permission> attributes from AndroidManifest.xml
    See: https://developer.android.com/guide/topics/manifest/permission-element

    @param manifest_xml: manifest xml dom
    @type  manifest_xml: xml dom

    @return: permission
    @rtype: list
    '''
    permission_list = []
    permissions = manifest_xml.getElementsByTagName('permission')
    if permissions:
        for permission in permissions:
            # permission attributes
            name = permission.getAttribute('android:name')
            description = permission.getAttribute('android:description')
            permissiongroup = permission.getAttribute('android:permissionGroup')
            protectionlevel = permission.getAttribute('android:protectionLevel')

            # permission information list
            permission_info = (name,
                               description,
                               permissiongroup,
                               protectionlevel)
            permission_list.append(permission_info)

    return permission_list


def get_uses_permission(manifest_xml):
    '''
    Get APK <uses-permission> attributes from AndroidManifest.xml
    See: https://developer.android.com/guide/topics/manifest/uses-permission-element

    @param manifest_xml: manifest xml dom
    @type  manifest_xml: xml dom

    @return: uses-permission
    @rtype: list
    '''
    uses_permission_list = []
    uses_permissions = manifest_xml.getElementsByTagName('uses-permission')
    if uses_permissions:
        for uses_perm in uses_permissions:
            # uses-permission attributes
            name = uses_perm.getAttribute('android:name')
            maxsdkversion = uses_perm.getAttribute('android:maxSdkVersion')

            # uses-permission information list
            usespermission_info = (name,
                                   maxsdkversion)
            uses_permission_list.append(usespermission_info)

    return uses_permission_list


def get_uses_permission_sdk23(manifest_xml):
    '''
    Get APK <uses-permission-sdk-23> attributes from AndroidManifest.xml
    See: https://developer.android.com/guide/topics/manifest/uses-permission-sdk-23-element

    @param manifest_xml: manifest xml dom
    @type  manifest_xml: xml dom

    @return: uses-permission-sdk-23
    @rtype: list
    '''
    uses_permission_list = []
    uses_permissions = manifest_xml.getElementsByTagName('uses-permission-sdk-23')
    if uses_permissions:
        for uses_perm in uses_permissions:
            # uses-permission-23 attributes
            name = uses_perm.getAttribute('android:name')
            maxsdkversion = uses_perm.getAttribute('android:maxSdkVersion')

            # uses-permission-23 information list
            usespermission_info = (name,
                                   maxsdkversion)
            uses_permission_list.append(usespermission_info)

    return uses_permission_list


def get_activities(manifest_xml):
    '''
    Get APK <activity> attributes from AndroidManifest.xml
    See: https://developer.android.com/guide/topics/manifest/activity-element

    @param manifest_xml: manifest xml dom
    @type  manifest_xml: xml dom

    @return: activity
    @rtype: list
    '''
    activities_list = []
    applications = manifest_xml.getElementsByTagName('application')
    for application in applications:
        for app_childnode in application.childNodes:
            manifest_tag_name = ''
            if app_childnode.nodeName == 'activity':
                manifest_tag_name = 'Activity'

            if manifest_tag_name in ['Activity']:
                # activity attributes
                name = app_childnode.getAttribute('android:name')
                allowembedded = app_childnode.getAttribute('android:allowembedded')
                allowtaskreparenting = app_childnode.getAttribute('android:allowTaskReparenting')
                alwaysretaintaskstate = app_childnode.getAttribute('android:alwaysRetainTaskState')
                autoremovefromrecents = app_childnode.getAttribute('android:autoRemoveFromRecents')
                cleartaskonlaunch = app_childnode.getAttribute('android:clearTaskOnLaunch')
                colormode = app_childnode.getAttribute('android:colorMode')
                configchanges = app_childnode.getAttribute('android:configChanges')
                directbootaware = app_childnode.getAttribute('android:directBootAware')
                documentlaunchmode = app_childnode.getAttribute('android:documentLaunchMode')
                enabled = app_childnode.getAttribute('android:enabled')
                excludefromrecents = app_childnode.getAttribute('android:excludeFromRecents')
                exported = app_childnode.getAttribute('android:exported')
                finishontasklaunch = app_childnode.getAttribute('android:finishOnTaskLaunch')
                hardwareaccelerated = app_childnode.getAttribute('android:hardwareAccelerated')
                immersive = app_childnode.getAttribute('android:immersive')
                launchmode = app_childnode.getAttribute('android:launchMode')
                locktaskmode = app_childnode.getAttribute('android:lockTaskMode')
                maxrecents = app_childnode.getAttribute('android:maxRecents')
                maxaspectratio = app_childnode.getAttribute('android:maxAspectRatio')
                multiprocess = app_childnode.getAttribute('android:multiprocess')
                nohistory = app_childnode.getAttribute('android:noHistory')
                parentactivityname = app_childnode.getAttribute('android:parentActivityName')
                persistablemode = app_childnode.getAttribute('android:persistableMode')
                permission = app_childnode.getAttribute('android:permission')
                relinquishtaskidentity = app_childnode.getAttribute('android:relinquishTaskIdentity')
                resizeableactivity = app_childnode.getAttribute('android:resizeableActivity')
                screenorientation = app_childnode.getAttribute('android:screenOrientation')
                showforallusers = app_childnode.getAttribute('android:showForAllUsers')
                statenotneeded = app_childnode.getAttribute('android:stateNotNeeded')
                pictureinpicture = app_childnode.getAttribute('android:supportsPictureInPicture')
                taskaffinity = app_childnode.getAttribute('android:taskAffinity')
                theme = app_childnode.getAttribute('android:theme')
                uioptions = app_childnode.getAttribute('android:uiOptions')
                windowsoftinputmode = app_childnode.getAttribute('android:windowSoftInputMode')

                # activity information list
                activity_info = (name,
                                 allowembedded,
                                 allowtaskreparenting,
                                 alwaysretaintaskstate,
                                 autoremovefromrecents,
                                 cleartaskonlaunch,
                                 colormode,
                                 configchanges,
                                 directbootaware,
                                 documentlaunchmode,
                                 enabled,
                                 excludefromrecents,
                                 exported,
                                 finishontasklaunch,
                                 hardwareaccelerated,
                                 immersive,
                                 launchmode,
                                 locktaskmode,
                                 maxrecents,
                                 maxaspectratio,
                                 multiprocess,
                                 nohistory,
                                 parentactivityname,
                                 persistablemode,
                                 permission,
                                 relinquishtaskidentity,
                                 resizeableactivity,
                                 screenorientation,
                                 showforallusers,
                                 statenotneeded,
                                 pictureinpicture,
                                 taskaffinity,
                                 theme,
                                 uioptions,
                                 windowsoftinputmode)
                activities_list.append(activity_info)

    return activities_list


def get_activities_alias(manifest_xml):
    '''
    Get APK <activity-alias> attributes from AndroidManifest.xml

    @param manifest_xml: manifest xml dom
    @type  manifest_xml: xml dom

    @return: activity-alias
    @rtype: list
    '''
    activities_alias_list = []
    applications = manifest_xml.getElementsByTagName('application')
    for application in applications:
        for app_childnode in application.childNodes:
            manifest_tag_name = ''
            if app_childnode.nodeName == 'activity-alias':
                manifest_tag_name = 'Activity-Alias'

            if manifest_tag_name in ['Activity-Alias']:
                # activity-alias attributes
                name = app_childnode.getAttribute('android:name')
                enabled = app_childnode.getAttribute('android:enabled')
                exported = app_childnode.getAttribute('android:exported')
                permission = app_childnode.getAttribute('android:permission')
                targetactivity = app_childnode.getAttribute('android:targetActivity')

                # activity-alias information list
                activities_alias_list.append(name,
                                             enabled,
                                             exported,
                                             permission,
                                             targetactivity)

    return activities_alias_list


def get_services(manifest_xml):
    '''
    Get APK <services> attributes from AndroidManifest.xml
    See: https://developer.android.com/guide/topics/manifest/service-element

    @param manifest_xml: manifest xml dom
    @type  manifest_xml: xml dom

    @return: service
    @rtype: list
    '''
    services_list = []
    services = manifest_xml.getElementsByTagName('service')
    if services:
        for service in services:
            # services attributes
            name = service.getAttribute('android:name')
            description = service.getAttribute('android:description')
            directbootaware = service.getAttribute('android:directBootAware')
            enabled = service.getAttribute('android:enabled')
            exported = service.getAttribute('android:exported')
            foregroundservicetype = service.getAttribute('android:foregroundServiceType')
            isolatedprocess = service.getAttribute('android:isolatedProcess')
            permission = service.getAttribute('android:permission')
            process = service.getAttribute('android:process')

            # services information list
            service_info = (name,
                            description,
                            directbootaware,
                            enabled,
                            exported,
                            foregroundservicetype,
                            isolatedprocess,
                            permission,
                            process)
            services_list.append(service_info)

    return services_list


def get_receivers(manifest_xml):
    '''
    Get APK <receiver> attributes from AndroidManifest.xml
    See: https://developer.android.com/guide/topics/manifest/receiver-element

    @param manifest_xml: manifest xml dom
    @type  manifest_xml: xml dom

    @return: receiver
    @rtype: list
    '''
    receivers_list = []
    receivers = manifest_xml.getElementsByTagName('receiver')
    if receivers:
        for receiver in receivers:
            # receiver attributes
            name = receiver.getAttribute('android:name')
            directbootaware = receiver.getAttribute('android:directBootAware')
            enabled = receiver.getAttribute('android:enabled')
            exported = receiver.getAttribute('android:exported')
            permission = receiver.getAttribute('android:permission')
            process = receiver.getAttribute('android:process')

            # receiver information list
            receiver_info = (name,
                             directbootaware,
                             enabled,
                             exported,
                             permission,
                             process)
            receivers_list.append(receiver_info)

    return receivers_list


def get_providers(manifest_xml):
    '''
    Get APK <provider> attributes from AndroidManifest.xml

    @param manifest_xml: manifest xml dom
    @type  manifest_xml: xml dom

    @return: provider
    @rtype: list
    '''
    providers_list = []
    providers = manifest_xml.getElementsByTagName('provider')
    if providers:
        for provider in providers:
            # provider attributes
            name = provider.getAttribute('android:name')
            authorities = provider.getAttribute('android:authorities')
            directbootaware = provider.getAttribute('android:directBootAware')
            enabled = provider.getAttribute('android:enabled')
            exported = provider.getAttribute('android:exported')
            granturipermissions = provider.getAttribute('android:grantUriPermissions')
            initorder = provider.getAttribute('android:initOrder')
            multiprocess = provider.getAttribute('android:multiprocess')
            permission = provider.getAttribute('android:permission')
            process = provider.getAttribute('android:process')
            readpermission = provider.getAttribute('android:readPermission')
            syncable = provider.getAttribute('android:syncable')
            writepermission = provider.getAttribute('android:writePermission')

            # provider information list
            providers_info = (name,
                              authorities,
                              directbootaware,
                              enabled,
                              exported,
                              granturipermissions,
                              initorder,
                              multiprocess,
                              permission,
                              process,
                              readpermission,
                              syncable,
                              writepermission)
            providers_list.append(providers_info)

    return providers_list


def get_manifest_element(manifest_xml):
    '''
    APK manifest element

    @param manifest_xml: manifest xml dom
    @type  manifest_xml: xml dom

    @return: manifest xml dom
    @rtype: xml dom
    '''
    manifest = manifest_xml.getElementsByTagName('manifest')
    if not manifest:
        return None

    return manifest[0]
