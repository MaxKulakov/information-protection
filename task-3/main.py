import os


ALLOWED_FILES = ['.exe', '.dll']

arr = ['DeleteIPAddress', 'FreeMibTable', 'GetAdaptersAddresses', 'GetAnycastIpAddressEntry', 'GetAnycastIpAddressTable', 
       'GetBestRoute2', 'GetHostNameW', 'GetIpAddrTable', 'GetIpStatisticsEx', 'GetUnicastIpAddressTable', 'IcmpCloseHandle', 
       'IcmpCreateFile', 'IcmpCloseHandle', 'IcmpSendEcho', 'MultinetGetConnectionPerformance', 'MultinetGetConnectionPerformanceW', 
       'NetAlertRaise', 'NetAlertRaiseEx', 'NetApiBufferAllocate', 'NetApiBufferFree', 'NetApiBufferReallocate', 'NetApiBufferSize', 
       'NetFreeAadJoinInformation', 'NetGetAadJoinInformation', 'NetAddAlternateComputerName', 'NetCreateProvisioningPackage',
       'NetEnumerateComputerNames', 'NetGetJoinableOUs', 'NetGetJoinInformation', 'NetJoinDomain', 'NetProvisionComputerAccount', 
       'NetRemoveAlternateComputerName', 'NetRenameMachineInDomain', 'NetRequestOfflineDomainJoin', 'NetRequestProvisioningPackageInstall', 
       'NetSetPrimaryComputerName', 'NetUnjoinDomain', 'NetValidateName', 'NetGetAnyDCName', 'NetGetDCName', 'NetGetDisplayInformationIndex', 
       'NetQueryDisplayInformation', 'NetGroupAdd', 'NetGroupAddUser', 'NetGroupDel', 'NetGroupDelUser', 'NetGroupEnum', 'NetGroupGetInfo', 
       'NetGroupGetUsers', 'NetGroupSetInfo', 'NetGroupSetUsers', 'NetLocalGroupAdd', 'NetLocalGroupAddMembers', 'NetLocalGroupDel', 
       'NetLocalGroupDelMembers', 'NetLocalGroupEnum', 'NetLocalGroupGetInfo', 'NetLocalGroupGetMembers', 'NetLocalGroupSetInfo', 
       'NetLocalGroupSetMembers', 'NetMessageBufferSend', 'NetMessageNameAdd', 'NetMessageNameDel', 'NetMessageNameEnum', 'NetMessageNameGetInfo', 
       'NetFileClose', 'NetFileEnum', 'NetFileGetInfo', 'NetRemoteComputerSupports', 'NetRemoteTOD', 'NetScheduleJobAdd', 'NetScheduleJobDel', 
       'NetScheduleJobEnum', 'NetScheduleJobGetInfo', 'GetNetScheduleAccountInformation', 'SetNetScheduleAccountInformation', 'NetServerDiskEnum', 
       'NetServerEnum', 'NetServerGetInfo', 'NetServerSetInfo', 'NetServerComputerNameAdd', 'NetServerComputerNameDel', 'NetServerTransportAdd', 
       'NetServerTransportAddEx', 'NetServerTransportDel', 'NetServerTransportEnum', 'NetWkstaTransportEnum', 'NetUseAdd', 'NetUseDel', 'NetUseEnum', 
       'NetUseGetInfo', 'NetUserAdd', 'NetUserChangePassword', 'NetUserDel', 'NetUserEnum', 'NetUserGetGroups', 'NetUserGetInfo', 'NetUserGetLocalGroups', 
       'NetUserSetGroups', 'NetUserSetInfo', 'NetUserModalsGet', 'NetUserModalsSet', 'NetValidatePasswordPolicyFree', 'NetValidatePasswordPolicy', 
       'NetWkstaGetInfo', 'NetWkstaSetInfo', 'NetWkstaUserEnum', 'NetWkstaUserGetInfo', 'NetWkstaUserSetInfo', 'NetAccessAdd', 'NetAccessCheck', 
       'NetAccessDel', 'NetAccessEnum', 'NetAccessGetInfo', 'NetAccessGetUserPerms', 'NetAccessSetInfo', 'NetAuditClear', 'NetAuditRead', 
       'NetAuditWrite', 'NetConfigGet', 'NetConfigGetAll', 'NetConfigSet', 'NetErrorLogClear', 'NetErrorLogRead', 'NetErrorLogWrite', 
       'NetLocalGroupAddMember', 'NetLocalGroupDelMember', 'NetServiceControl', 'NetServiceEnum', 'NetServiceGetInfo', 'NetServiceInstall', 
       'NetWkstaTransportAdd', 'NetWkstaTransportDel', 'NetpwNameValidate', 'NetapipBufferAllocate', 'NetpwPathType', 'NetApiBufferFree', 
       'NetApiBufferAllocate', 'NetApiBufferReallocate', 'WNetAddConnection2', 'WNetAddConnection2W', 'WNetAddConnection3', 'WNetAddConnection3W', 
       'WNetCancelConnection', 'WNetCancelConnectionW', 'WNetCancelConnection2', 'WNetCancelConnection2W', 'WNetCloseEnum', 'WNetCloseEnumW', 
       'WNetConnectionDialog', 'WNetConnectionDialogW', 'WNetConnectionDialog1', 'WNetConnectionDialog1W', 'WNetDisconnectDialog', 
       'WNetDisconnectDialogW', 'WNetDisconnectDialog1', 'WNetDisconnectDialog1W', 'WNetEnumResource', 'WNetEnumResourceW', 'WNetGetConnection', 
       'WNetGetConnectionW', 'WNetGetLastError', 'WNetGetLastErrorW', 'WNetGetNetworkInformation', 'WNetGetNetworkInformationW', 'WNetGetProviderName', 
       'WNetGetProviderNameW', 'WNetGetResourceInformation', 'WNetGetResourceInformationW', 'WNetGetResourceParent', 'WNetGetResourceParentW', 
       'WNetGetUniversalName', 'WNetGetUniversalNameW', 'WNetGetUser', 'WNetGetUserW', 'WNetOpenEnum', 'WNetOpenEnumW', 'WNetRestoreConnectionW', 
       'WNetUseConnection', 'WNetUseConnectionW']

def get_path_to_files(path):
    cnt = 0
    os.chdir(path)
    path_to_files = []
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if str(name[-4:]).lower() in ALLOWED_FILES:
                # os.unlink(os.path.join(root, name))
                # print(os.path.join(root, name))
                cnt += 1
    print(cnt)        


# get_path_to_files('./System32')
# str = str.split(' ')
# print(str)

print(arr)