from CloudStack import BaseClient


class Client(BaseClient.BaseClient):

    def createNetworkOffering(self, displayText, guestIpType, name, supportedServices, trafficType, availability = "", conserveMode = "", networkRate = "", serviceCapabilityList = "", serviceOfferingId = "", serviceProviderList = "", specifyIpRanges = "", specifyVlan = "", tags = ""):
        '''
        Creates a network offering.
        '''

        return self.request("createNetworkOffering", {
            'displaytext' : displayText,
            'guestiptype' : guestIpType,
            'name' : name,
            'supportedservices' : supportedServices,
            'traffictype' : trafficType,
            'availability' : availability,
            'conservemode' : conserveMode,
            'networkrate' : networkRate,
            'servicecapabilitylist' : serviceCapabilityList,
            'serviceofferingid' : serviceOfferingId,
            'serviceproviderlist' : serviceProviderList,
            'specifyipranges' : specifyIpRanges,
            'specifyvlan' : specifyVlan,
            'tags' : tags,
        })
    
    def updateNetworkOffering(self, availability = "", displayText = "", id = "", name = "", sortKey = "", state = ""):
        '''
        Updates a network offering.
        '''

        return self.request("updateNetworkOffering", {
            'availability' : availability,
            'displaytext' : displayText,
            'id' : id,
            'name' : name,
            'sortkey' : sortKey,
            'state' : state,
        })
    
    def deleteNetworkOffering(self, id):
        '''
        Deletes a network offering.
        '''

        return self.request("deleteNetworkOffering", {
            'id' : id,
        })
    
    def listNetworkOfferings(self, availability = "", displayText = "", guestIpType = "", id = "", isDefault = "", isTagged = "", keyword = "", name = "", networkId = "", page = "", pageSize = "", sourceNatSupported = "", specifyIpRanges = "", specifyVlan = "", state = "", supportedServices = "", tags = "", trafficType = "", zoneId = ""):
        '''
        Lists all available network offerings.
        '''

        return self.request("listNetworkOfferings", {
            'availability' : availability,
            'displaytext' : displayText,
            'guestiptype' : guestIpType,
            'id' : id,
            'isdefault' : isDefault,
            'istagged' : isTagged,
            'keyword' : keyword,
            'name' : name,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'sourcenatsupported' : sourceNatSupported,
            'specifyipranges' : specifyIpRanges,
            'specifyvlan' : specifyVlan,
            'state' : state,
            'supportedservices' : supportedServices,
            'tags' : tags,
            'traffictype' : trafficType,
            'zoneid' : zoneId,
        })
    
    def createNetwork(self, displayText, name, networkOfferingId, zoneId, account = "", aclType = "", domainId = "", endIp = "", gateway = "", netmask = "", networkDomain = "", physicalNetworkId = "", projectId = "", startIp = "", subDomainAccess = "", vlan = ""):
        '''
        Creates a network
        '''

        return self.request("createNetwork", {
            'displaytext' : displayText,
            'name' : name,
            'networkofferingid' : networkOfferingId,
            'zoneid' : zoneId,
            'account' : account,
            'acltype' : aclType,
            'domainid' : domainId,
            'endip' : endIp,
            'gateway' : gateway,
            'netmask' : netmask,
            'networkdomain' : networkDomain,
            'physicalnetworkid' : physicalNetworkId,
            'projectid' : projectId,
            'startip' : startIp,
            'subdomainaccess' : subDomainAccess,
            'vlan' : vlan,
        })
    
    def deleteNetwork(self, id):
        '''
        Deletes a network
        '''

        return self.request("deleteNetwork", {
            'id' : id,
        })
    
    def listNetworks(self, account = "", aclType = "", domainId = "", id = "", isRecursive = "", isSystem = "", keyword = "", listAll = "", page = "", pageSize = "", physicalNetworkId = "", projectId = "", restartRequired = "", specifyIpRanges = "", supportedServices = "", trafficType = "", type = "", zoneId = ""):
        '''
        Lists all available networks.
        '''

        return self.request("listNetworks", {
            'account' : account,
            'acltype' : aclType,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'issystem' : isSystem,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'physicalnetworkid' : physicalNetworkId,
            'projectid' : projectId,
            'restartrequired' : restartRequired,
            'specifyipranges' : specifyIpRanges,
            'supportedservices' : supportedServices,
            'traffictype' : trafficType,
            'type' : type,
            'zoneid' : zoneId,
        })
    
    def restartNetwork(self, id, cleanup = ""):
        '''
        Restarts the network; includes 1) restarting network elements - virtual routers, dhcp servers 2) reapplying all public ips 3) reapplying loadBalancing/portForwarding rules
        '''

        return self.request("restartNetwork", {
            'id' : id,
            'cleanup' : cleanup,
        })
    
    def updateNetwork(self, id, changeCidr = "", displayText = "", name = "", networkDomain = "", networkOfferingId = ""):
        '''
        Updates a network
        '''

        return self.request("updateNetwork", {
            'id' : id,
            'changecidr' : changeCidr,
            'displaytext' : displayText,
            'name' : name,
            'networkdomain' : networkDomain,
            'networkofferingid' : networkOfferingId,
        })
    
    def createPhysicalNetwork(self, name, zoneId, broadcastDomainRange = "", domainId = "", isolationMethods = "", networkSpeed = "", tags = "", vlan = ""):
        '''
        Creates a physical network
        '''

        return self.request("createPhysicalNetwork", {
            'name' : name,
            'zoneid' : zoneId,
            'broadcastdomainrange' : broadcastDomainRange,
            'domainid' : domainId,
            'isolationmethods' : isolationMethods,
            'networkspeed' : networkSpeed,
            'tags' : tags,
            'vlan' : vlan,
        })
    
    def deletePhysicalNetwork(self, id):
        '''
        Deletes a Physical Network.
        '''

        return self.request("deletePhysicalNetwork", {
            'id' : id,
        })
    
    def listPhysicalNetworks(self, id = "", keyword = "", name = "", page = "", pageSize = "", zoneId = ""):
        '''
        Lists physical networks
        '''

        return self.request("listPhysicalNetworks", {
            'id' : id,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'zoneid' : zoneId,
        })
    
    def updatePhysicalNetwork(self, id, networkSpeed = "", state = "", tags = "", vlan = ""):
        '''
        Updates a physical network
        '''

        return self.request("updatePhysicalNetwork", {
            'id' : id,
            'networkspeed' : networkSpeed,
            'state' : state,
            'tags' : tags,
            'vlan' : vlan,
        })
    
    def listSupportedNetworkServices(self, keyword = "", page = "", pageSize = "", provider = "", service = ""):
        '''
        Lists all network services provided by CloudStack or for the given Provider.
        '''

        return self.request("listSupportedNetworkServices", {
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'provider' : provider,
            'service' : service,
        })
    
    def addNetworkServiceProvider(self, name, physicalNetworkId, destinationPhysicalNetworkId = "", serviceList = ""):
        '''
        Adds a network serviceProvider to a physical network
        '''

        return self.request("addNetworkServiceProvider", {
            'name' : name,
            'physicalnetworkid' : physicalNetworkId,
            'destinationphysicalnetworkid' : destinationPhysicalNetworkId,
            'servicelist' : serviceList,
        })
    
    def deleteNetworkServiceProvider(self, id):
        '''
        Deletes a Network Service Provider.
        '''

        return self.request("deleteNetworkServiceProvider", {
            'id' : id,
        })
    
    def listNetworkServiceProviders(self, keyword = "", name = "", page = "", pageSize = "", physicalNetworkId = "", state = ""):
        '''
        Lists network serviceproviders for a given physical network.
        '''

        return self.request("listNetworkServiceProviders", {
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'physicalnetworkid' : physicalNetworkId,
            'state' : state,
        })
    
    def updateNetworkServiceProvider(self, id, serviceList = "", state = ""):
        '''
        Updates a network serviceProvider of a physical network
        '''

        return self.request("updateNetworkServiceProvider", {
            'id' : id,
            'servicelist' : serviceList,
            'state' : state,
        })
    
    def createStorageNetworkIpRange(self, gateway, netmask, podId, startIp, endIp = "", vlan = ""):
        '''
        Creates a Storage network IP range.
        '''

        return self.request("createStorageNetworkIpRange", {
            'gateway' : gateway,
            'netmask' : netmask,
            'podid' : podId,
            'startip' : startIp,
            'endip' : endIp,
            'vlan' : vlan,
        })
    
    def deleteStorageNetworkIpRange(self, id):
        '''
        Deletes a storage network IP Range.
        '''

        return self.request("deleteStorageNetworkIpRange", {
            'id' : id,
        })
    
    def listStorageNetworkIpRange(self, id = "", keyword = "", page = "", pageSize = "", podId = "", zoneId = ""):
        '''
        List a storage network IP range.
        '''

        return self.request("listStorageNetworkIpRange", {
            'id' : id,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'podid' : podId,
            'zoneid' : zoneId,
        })
    
    def updateStorageNetworkIpRange(self, id, endIp = "", netmask = "", startIp = "", vlan = ""):
        '''
        Update a Storage network IP range, only allowed when no IPs in this range have been allocated.
        '''

        return self.request("updateStorageNetworkIpRange", {
            'id' : id,
            'endip' : endIp,
            'netmask' : netmask,
            'startip' : startIp,
            'vlan' : vlan,
        })
    
    def addNetworkDevice(self, networkDeviceParameterList = "", networkDeviceType = ""):
        '''
        Adds a network device of one of the following types: ExternalDhcp, ExternalFirewall, ExternalLoadBalancer, PxeServer
        '''

        return self.request("addNetworkDevice", {
            'networkdeviceparameterlist' : networkDeviceParameterList,
            'networkdevicetype' : networkDeviceType,
        })
    
    def listNetworkDevice(self, keyword = "", networkDeviceParameterList = "", networkDeviceType = "", page = "", pageSize = ""):
        '''
        List network devices
        '''

        return self.request("listNetworkDevice", {
            'keyword' : keyword,
            'networkdeviceparameterlist' : networkDeviceParameterList,
            'networkdevicetype' : networkDeviceType,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def deleteNetworkDevice(self, id):
        '''
        Deletes network device.
        '''

        return self.request("deleteNetworkDevice", {
            'id' : id,
        })
    
    def listF5LoadBalancerNetworks(self, lbDeviceId, keyword = "", page = "", pageSize = ""):
        '''
        lists network that are using a F5 load balancer device
        '''

        return self.request("listF5LoadBalancerNetworks", {
            'lbdeviceid' : lbDeviceId,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listSrxFirewallNetworks(self, lbDeviceId, keyword = "", page = "", pageSize = ""):
        '''
        lists network that are using SRX firewall device
        '''

        return self.request("listSrxFirewallNetworks", {
            'lbdeviceid' : lbDeviceId,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listNetscalerLoadBalancerNetworks(self, lbDeviceId, keyword = "", page = "", pageSize = ""):
        '''
        lists network that are using a netscaler load balancer device
        '''

        return self.request("listNetscalerLoadBalancerNetworks", {
            'lbdeviceid' : lbDeviceId,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def createLoadBalancerRule(self, algorithm, name, privatePort, publicPort, account = "", cidrList = "", description = "", domainId = "", networkId = "", openFirewall = "", publicIpId = "", zoneId = ""):
        '''
        Creates a load balancer rule
        '''

        return self.request("createLoadBalancerRule", {
            'algorithm' : algorithm,
            'name' : name,
            'privateport' : privatePort,
            'publicport' : publicPort,
            'account' : account,
            'cidrlist' : cidrList,
            'description' : description,
            'domainid' : domainId,
            'networkid' : networkId,
            'openfirewall' : openFirewall,
            'publicipid' : publicIpId,
            'zoneid' : zoneId,
        })
    
    def deleteLoadBalancerRule(self, id):
        '''
        Deletes a load balancer rule.
        '''

        return self.request("deleteLoadBalancerRule", {
            'id' : id,
        })
    
    def removeFromLoadBalancerRule(self, id, virtualMachineIds):
        '''
        Removes a virtual machine or a list of virtual machines from a load balancer rule.
        '''

        return self.request("removeFromLoadBalancerRule", {
            'id' : id,
            'virtualmachineids' : virtualMachineIds,
        })
    
    def assignToLoadBalancerRule(self, id, virtualMachineIds):
        '''
        Assigns virtual machine or a list of virtual machines to a load balancer rule.
        '''

        return self.request("assignToLoadBalancerRule", {
            'id' : id,
            'virtualmachineids' : virtualMachineIds,
        })
    
    def createLBStickinessPolicy(self, lbruleId, methodName, name, description = "", param = ""):
        '''
        Creates a Load Balancer stickiness policy
        '''

        return self.request("createLBStickinessPolicy", {
            'lbruleid' : lbruleId,
            'methodname' : methodName,
            'name' : name,
            'description' : description,
            'param' : param,
        })
    
    def deleteLBStickinessPolicy(self, id):
        '''
        Deletes a LB stickiness policy.
        '''

        return self.request("deleteLBStickinessPolicy", {
            'id' : id,
        })
    
    def listLoadBalancerRules(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = "", publicIpId = "", virtualMachineId = "", zoneId = ""):
        '''
        Lists load balancer rules.
        '''

        return self.request("listLoadBalancerRules", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'publicipid' : publicIpId,
            'virtualmachineid' : virtualMachineId,
            'zoneid' : zoneId,
        })
    
    def listLBStickinessPolicies(self, lbruleId, keyword = "", page = "", pageSize = ""):
        '''
        Lists LBStickiness policies.
        '''

        return self.request("listLBStickinessPolicies", {
            'lbruleid' : lbruleId,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listLoadBalancerRuleInstances(self, id, applied = "", keyword = "", page = "", pageSize = ""):
        '''
        List all virtual machine instances that are assigned to a load balancer rule.
        '''

        return self.request("listLoadBalancerRuleInstances", {
            'id' : id,
            'applied' : applied,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def updateLoadBalancerRule(self, id, algorithm = "", description = "", name = ""):
        '''
        Updates load balancer
        '''

        return self.request("updateLoadBalancerRule", {
            'id' : id,
            'algorithm' : algorithm,
            'description' : description,
            'name' : name,
        })
    
    def addF5LoadBalancer(self, networkDeviceType, password, physicalNetworkId, url, userName):
        '''
        Adds a F5 BigIP load balancer device
        '''

        return self.request("addF5LoadBalancer", {
            'networkdevicetype' : networkDeviceType,
            'password' : password,
            'physicalnetworkid' : physicalNetworkId,
            'url' : url,
            'username' : userName,
        })
    
    def configureF5LoadBalancer(self, lbDeviceId, lbDeviceCapacity = ""):
        '''
        configures a F5 load balancer device
        '''

        return self.request("configureF5LoadBalancer", {
            'lbdeviceid' : lbDeviceId,
            'lbdevicecapacity' : lbDeviceCapacity,
        })
    
    def deleteF5LoadBalancer(self, lbDeviceId):
        '''
        delete a F5 load balancer device
        '''

        return self.request("deleteF5LoadBalancer", {
            'lbdeviceid' : lbDeviceId,
        })
    
    def listF5LoadBalancers(self, keyword = "", lbDeviceId = "", page = "", pageSize = "", physicalNetworkId = ""):
        '''
        lists F5 load balancer devices
        '''

        return self.request("listF5LoadBalancers", {
            'keyword' : keyword,
            'lbdeviceid' : lbDeviceId,
            'page' : page,
            'pagesize' : pageSize,
            'physicalnetworkid' : physicalNetworkId,
        })
    
    def addNetscalerLoadBalancer(self, networkDeviceType, password, physicalNetworkId, url, userName):
        '''
        Adds a netscaler load balancer device
        '''

        return self.request("addNetscalerLoadBalancer", {
            'networkdevicetype' : networkDeviceType,
            'password' : password,
            'physicalnetworkid' : physicalNetworkId,
            'url' : url,
            'username' : userName,
        })
    
    def deleteNetscalerLoadBalancer(self, lbDeviceId):
        '''
        delete a netscaler load balancer device
        '''

        return self.request("deleteNetscalerLoadBalancer", {
            'lbdeviceid' : lbDeviceId,
        })
    
    def configureNetscalerLoadBalancer(self, lbDeviceId, inline = "", lbDeviceCapacity = "", lbDeviceDedicated = ""):
        '''
        configures a netscaler load balancer device
        '''

        return self.request("configureNetscalerLoadBalancer", {
            'lbdeviceid' : lbDeviceId,
            'inline' : inline,
            'lbdevicecapacity' : lbDeviceCapacity,
            'lbdevicededicated' : lbDeviceDedicated,
        })
    
    def listNetscalerLoadBalancers(self, keyword = "", lbDeviceId = "", page = "", pageSize = "", physicalNetworkId = ""):
        '''
        lists netscaler load balancer devices
        '''

        return self.request("listNetscalerLoadBalancers", {
            'keyword' : keyword,
            'lbdeviceid' : lbDeviceId,
            'page' : page,
            'pagesize' : pageSize,
            'physicalnetworkid' : physicalNetworkId,
        })
    
    def deployVirtualMachine(self, serviceOfferingId, templateId, zoneId, account = "", diskOfferingId = "", displayName = "", domainId = "", group = "", hostId = "", hypervisor = "", ipAddress = "", ipToNetWorkList = "", keyboard = "", keyPair = "", name = "", networkIds = "", projectId = "", securityGroupIds = "", securityGroupNames = "", size = "", userData = ""):
        '''
        Creates and automatically starts a virtual machine based on a service offering, disk offering, and template.
        '''

        return self.request("deployVirtualMachine", {
            'serviceofferingid' : serviceOfferingId,
            'templateid' : templateId,
            'zoneid' : zoneId,
            'account' : account,
            'diskofferingid' : diskOfferingId,
            'displayname' : displayName,
            'domainid' : domainId,
            'group' : group,
            'hostid' : hostId,
            'hypervisor' : hypervisor,
            'ipaddress' : ipAddress,
            'iptonetworklist' : ipToNetWorkList,
            'keyboard' : keyboard,
            'keypair' : keyPair,
            'name' : name,
            'networkids' : networkIds,
            'projectid' : projectId,
            'securitygroupids' : securityGroupIds,
            'securitygroupnames' : securityGroupNames,
            'size' : size,
            'userdata' : userData,
        })
    
    def destroyVirtualMachine(self, id):
        '''
        Destroys a virtual machine. Once destroyed, only the administrator can recover it.
        '''

        return self.request("destroyVirtualMachine", {
            'id' : id,
        })
    
    def rebootVirtualMachine(self, id):
        '''
        Reboots a virtual machine.
        '''

        return self.request("rebootVirtualMachine", {
            'id' : id,
        })
    
    def startVirtualMachine(self, id):
        '''
        Starts a virtual machine.
        '''

        return self.request("startVirtualMachine", {
            'id' : id,
        })
    
    def stopVirtualMachine(self, id, forced = ""):
        '''
        Stops a virtual machine.
        '''

        return self.request("stopVirtualMachine", {
            'id' : id,
            'forced' : forced,
        })
    
    def resetPasswordForVirtualMachine(self, id):
        '''
        Resets the password for virtual machine. The virtual machine must be in a "Stopped" state and the template must already support this feature for this command to take effect. [async]
        '''

        return self.request("resetPasswordForVirtualMachine", {
            'id' : id,
        })
    
    def changeServiceForVirtualMachine(self, id, serviceOfferingId):
        '''
        Changes the service offering for a virtual machine. The virtual machine must be in a "Stopped" state for this command to take effect.
        '''

        return self.request("changeServiceForVirtualMachine", {
            'id' : id,
            'serviceofferingid' : serviceOfferingId,
        })
    
    def updateVirtualMachine(self, id, displayName = "", group = "", haEnable = "", osTypeId = "", userData = ""):
        '''
        Updates parameters of a virtual machine.
        '''

        return self.request("updateVirtualMachine", {
            'id' : id,
            'displayname' : displayName,
            'group' : group,
            'haenable' : haEnable,
            'ostypeid' : osTypeId,
            'userdata' : userData,
        })
    
    def recoverVirtualMachine(self, id):
        '''
        Recovers a virtual machine.
        '''

        return self.request("recoverVirtualMachine", {
            'id' : id,
        })
    
    def listVirtualMachines(self, account = "", details = "", domainId = "", forVirtualNetwork = "", groupId = "", hostId = "", hypervisor = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", networkId = "", page = "", pageSize = "", podId = "", projectId = "", state = "", storageId = "", zoneId = ""):
        '''
        List the virtual machines owned by the account.
        '''

        return self.request("listVirtualMachines", {
            'account' : account,
            'details' : details,
            'domainid' : domainId,
            'forvirtualnetwork' : forVirtualNetwork,
            'groupid' : groupId,
            'hostid' : hostId,
            'hypervisor' : hypervisor,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'podid' : podId,
            'projectid' : projectId,
            'state' : state,
            'storageid' : storageId,
            'zoneid' : zoneId,
        })
    
    def getVMPassword(self, id):
        '''
        Returns an encrypted password for the VM
        '''

        return self.request("getVMPassword", {
            'id' : id,
        })
    
    def migrateVirtualMachine(self, virtualMachineId, hostId = "", storageId = ""):
        '''
        Attempts Migration of a VM to a different host or Root volume of the vm to a different storage pool
        '''

        return self.request("migrateVirtualMachine", {
            'virtualmachineid' : virtualMachineId,
            'hostid' : hostId,
            'storageid' : storageId,
        })
    
    def assignVirtualMachine(self, account, domainId, virtualMachineId, networkIds = "", securityGroupIds = ""):
        '''
        Move a user VM to another user under same domain.
        '''

        return self.request("assignVirtualMachine", {
            'account' : account,
            'domainid' : domainId,
            'virtualmachineid' : virtualMachineId,
            'networkids' : networkIds,
            'securitygroupids' : securityGroupIds,
        })
    
    def restoreVirtualMachine(self, virtualMachineId):
        '''
        Restore a VM to original template or specific snapshot
        '''

        return self.request("restoreVirtualMachine", {
            'virtualmachineid' : virtualMachineId,
        })
    
    def addTrafficType(self, physicalNetworkId, trafficType, kvmNetworkLabel = "", vlan = "", vmwareNetworkLabel = "", xenNetworkLabel = ""):
        '''
        Adds traffic type to a physical network
        '''

        return self.request("addTrafficType", {
            'physicalnetworkid' : physicalNetworkId,
            'traffictype' : trafficType,
            'kvmnetworklabel' : kvmNetworkLabel,
            'vlan' : vlan,
            'vmwarenetworklabel' : vmwareNetworkLabel,
            'xennetworklabel' : xenNetworkLabel,
        })
    
    def deleteTrafficType(self, id):
        '''
        Deletes traffic type of a physical network
        '''

        return self.request("deleteTrafficType", {
            'id' : id,
        })
    
    def listTrafficTypes(self, physicalNetworkId, keyword = "", page = "", pageSize = ""):
        '''
        Lists traffic types of a given physical network.
        '''

        return self.request("listTrafficTypes", {
            'physicalnetworkid' : physicalNetworkId,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def updateTrafficType(self, id, kvmNetworkLabel = "", vmwareNetworkLabel = "", xenNetworkLabel = ""):
        '''
        Updates traffic type of a physical network
        '''

        return self.request("updateTrafficType", {
            'id' : id,
            'kvmnetworklabel' : kvmNetworkLabel,
            'vmwarenetworklabel' : vmwareNetworkLabel,
            'xennetworklabel' : xenNetworkLabel,
        })
    
    def listTrafficTypeImplementors(self, keyword = "", page = "", pageSize = "", trafficType = ""):
        '''
        Lists implementors of implementor of a network traffic type or implementors of all network traffic types
        '''

        return self.request("listTrafficTypeImplementors", {
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'traffictype' : trafficType,
        })
    
    def generateUsageRecords(self, endDate, startDate, domainId = ""):
        '''
        Generates usage records. This will generate records only if there any records to be generated, i.e if the scheduled usage job was not run or failed
        '''

        return self.request("generateUsageRecords", {
            'enddate' : endDate,
            'startdate' : startDate,
            'domainid' : domainId,
        })
    
    def listUsageRecords(self, endDate, startDate, account = "", accountId = "", domainId = "", keyword = "", page = "", pageSize = "", projectId = "", type = ""):
        '''
        Lists usage records for accounts
        '''

        return self.request("listUsageRecords", {
            'enddate' : endDate,
            'startdate' : startDate,
            'account' : account,
            'accountid' : accountId,
            'domainid' : domainId,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'type' : type,
        })
    
    def listUsageTypes(self, ):
        '''
        List Usage Types
        '''

        return self.request("listUsageTypes", {
        })
    
    def addTrafficMonitor(self, url, zoneId):
        '''
        Adds Traffic Monitor Host for Direct Network Usage
        '''

        return self.request("addTrafficMonitor", {
            'url' : url,
            'zoneid' : zoneId,
        })
    
    def deleteTrafficMonitor(self, id):
        '''
        Deletes an traffic monitor host.
        '''

        return self.request("deleteTrafficMonitor", {
            'id' : id,
        })
    
    def listTrafficMonitors(self, zoneId, keyword = "", page = "", pageSize = ""):
        '''
        List traffic monitor Hosts.
        '''

        return self.request("listTrafficMonitors", {
            'zoneid' : zoneId,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def attachVolume(self, id, virtualMachineId, deviceId = ""):
        '''
        Attaches a disk volume to a virtual machine.
        '''

        return self.request("attachVolume", {
            'id' : id,
            'virtualmachineid' : virtualMachineId,
            'deviceid' : deviceId,
        })
    
    def detachVolume(self, deviceId = "", id = "", virtualMachineId = ""):
        '''
        Detaches a disk volume from a virtual machine.
        '''

        return self.request("detachVolume", {
            'deviceid' : deviceId,
            'id' : id,
            'virtualmachineid' : virtualMachineId,
        })
    
    def createVolume(self, name, account = "", diskOfferingId = "", domainId = "", projectId = "", size = "", snapshotId = "", zoneId = ""):
        '''
        Creates a disk volume from a disk offering. This disk volume must still be attached to a virtual machine to make use of it.
        '''

        return self.request("createVolume", {
            'name' : name,
            'account' : account,
            'diskofferingid' : diskOfferingId,
            'domainid' : domainId,
            'projectid' : projectId,
            'size' : size,
            'snapshotid' : snapshotId,
            'zoneid' : zoneId,
        })
    
    def deleteVolume(self, id):
        '''
        Deletes a detached disk volume.
        '''

        return self.request("deleteVolume", {
            'id' : id,
        })
    
    def listVolumes(self, account = "", domainId = "", hostId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", podId = "", projectId = "", type = "", virtualMachineId = "", zoneId = ""):
        '''
        Lists all volumes.
        '''

        return self.request("listVolumes", {
            'account' : account,
            'domainid' : domainId,
            'hostid' : hostId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'podid' : podId,
            'projectid' : projectId,
            'type' : type,
            'virtualmachineid' : virtualMachineId,
            'zoneid' : zoneId,
        })
    
    def extractVolume(self, id, mode, zoneId, url = ""):
        '''
        Extracts volume
        '''

        return self.request("extractVolume", {
            'id' : id,
            'mode' : mode,
            'zoneid' : zoneId,
            'url' : url,
        })
    
    def migrateVolume(self, storageId, volumeId):
        '''
        Migrate volume
        '''

        return self.request("migrateVolume", {
            'storageid' : storageId,
            'volumeid' : volumeId,
        })
    
    def createVolumeOnFiler(self, aggregateName, ipAddress, password, poolName, size, userName, volumeName, snapshotPolicy = "", snapshotReservation = ""):
        '''
        Create a volume
        '''

        return self.request("createVolumeOnFiler", {
            'aggregatename' : aggregateName,
            'ipaddress' : ipAddress,
            'password' : password,
            'poolname' : poolName,
            'size' : size,
            'username' : userName,
            'volumename' : volumeName,
            'snapshotpolicy' : snapshotPolicy,
            'snapshotreservation' : snapshotReservation,
        })
    
    def destroyVolumeOnFiler(self, aggregateName, ipAddress, volumeName):
        '''
        Destroy a Volume
        '''

        return self.request("destroyVolumeOnFiler", {
            'aggregatename' : aggregateName,
            'ipaddress' : ipAddress,
            'volumename' : volumeName,
        })
    
    def listVolumesOnFiler(self, poolName):
        '''
        List Volumes
        '''

        return self.request("listVolumesOnFiler", {
            'poolname' : poolName,
        })
    
    def createUser(self, account, email, firstName, lastname, password, userName, domainId = "", timezone = ""):
        '''
        Creates a user for an account that already exists
        '''

        return self.request("createUser", {
            'account' : account,
            'email' : email,
            'firstname' : firstName,
            'lastname' : lastname,
            'password' : password,
            'username' : userName,
            'domainid' : domainId,
            'timezone' : timezone,
        })
    
    def deleteUser(self, id):
        '''
        Creates a user for an account
        '''

        return self.request("deleteUser", {
            'id' : id,
        })
    
    def updateUser(self, id, email = "", firstName = "", lastname = "", password = "", timezone = "", userApiKey = "", userName = "", userSecretKey = ""):
        '''
        Updates a user account
        '''

        return self.request("updateUser", {
            'id' : id,
            'email' : email,
            'firstname' : firstName,
            'lastname' : lastname,
            'password' : password,
            'timezone' : timezone,
            'userapikey' : userApiKey,
            'username' : userName,
            'usersecretkey' : userSecretKey,
        })
    
    def listUsers(self, account = "", accountType = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", state = "", userName = ""):
        '''
        Lists user accounts
        '''

        return self.request("listUsers", {
            'account' : account,
            'accounttype' : accountType,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'state' : state,
            'username' : userName,
        })
    
    def disableUser(self, id):
        '''
        Disables a user account
        '''

        return self.request("disableUser", {
            'id' : id,
        })
    
    def enableUser(self, id):
        '''
        Enables a user account
        '''

        return self.request("enableUser", {
            'id' : id,
        })
    
    def registerUserKeys(self, id):
        '''
        This command allows a user to register for the developer API, returning a secret key and an API key. This request is made through the integration API port, so it is a privileged command and must be made on behalf of a user. It is up to the implementer just how the username and password are entered, and then how that translates to an integration API request. Both secret key and API key should be returned to the user
        '''

        return self.request("registerUserKeys", {
            'id' : id,
        })
    
    def addVpnUser(self, password, userName, account = "", domainId = "", projectId = ""):
        '''
        Adds vpn users
        '''

        return self.request("addVpnUser", {
            'password' : password,
            'username' : userName,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def removeVpnUser(self, userName, account = "", domainId = "", projectId = ""):
        '''
        Removes vpn user
        '''

        return self.request("removeVpnUser", {
            'username' : userName,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def listVpnUsers(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", userName = ""):
        '''
        Lists vpn users
        '''

        return self.request("listVpnUsers", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'username' : userName,
        })
    
    def createTemplate(self, displayText, name, osTypeId, bits = "", details = "", isFeatured = "", isPublic = "", passwordEnabled = "", requireShvm = "", snapshotId = "", templateTag = "", url = "", virtualMachineId = "", volumeId = ""):
        '''
        Creates a template of a virtual machine. The virtual machine must be in a STOPPED state. A template created from this command is automatically designated as a private template visible to the account that created it.
        '''

        return self.request("createTemplate", {
            'displaytext' : displayText,
            'name' : name,
            'ostypeid' : osTypeId,
            'bits' : bits,
            'details' : details,
            'isfeatured' : isFeatured,
            'ispublic' : isPublic,
            'passwordenabled' : passwordEnabled,
            'requireshvm' : requireShvm,
            'snapshotid' : snapshotId,
            'templatetag' : templateTag,
            'url' : url,
            'virtualmachineid' : virtualMachineId,
            'volumeid' : volumeId,
        })
    
    def registerTemplate(self, displayText, format, hypervisor, name, osTypeId, url, zoneId, account = "", bits = "", checksum = "", details = "", domainId = "", isExtractable = "", isFeatured = "", isPublic = "", passwordEnabled = "", projectId = "", requireShvm = "", sshkeyEnabled = "", templateTag = ""):
        '''
        Registers an existing template into the Cloud.com cloud.
        '''

        return self.request("registerTemplate", {
            'displaytext' : displayText,
            'format' : format,
            'hypervisor' : hypervisor,
            'name' : name,
            'ostypeid' : osTypeId,
            'url' : url,
            'zoneid' : zoneId,
            'account' : account,
            'bits' : bits,
            'checksum' : checksum,
            'details' : details,
            'domainid' : domainId,
            'isextractable' : isExtractable,
            'isfeatured' : isFeatured,
            'ispublic' : isPublic,
            'passwordenabled' : passwordEnabled,
            'projectid' : projectId,
            'requireshvm' : requireShvm,
            'sshkeyenabled' : sshkeyEnabled,
            'templatetag' : templateTag,
        })
    
    def updateTemplate(self, id, bootable = "", displayText = "", format = "", name = "", osTypeId = "", passwordEnabled = "", sortKey = ""):
        '''
        Updates attributes of a template.
        '''

        return self.request("updateTemplate", {
            'id' : id,
            'bootable' : bootable,
            'displaytext' : displayText,
            'format' : format,
            'name' : name,
            'ostypeid' : osTypeId,
            'passwordenabled' : passwordEnabled,
            'sortkey' : sortKey,
        })
    
    def copyTemplate(self, id, destzoneId, sourceZoneId):
        '''
        Copies a template from one zone to another.
        '''

        return self.request("copyTemplate", {
            'id' : id,
            'destzoneid' : destzoneId,
            'sourcezoneid' : sourceZoneId,
        })
    
    def deleteTemplate(self, id, zoneId = ""):
        '''
        Deletes a template from the system. All virtual machines using the deleted template will not be affected.
        '''

        return self.request("deleteTemplate", {
            'id' : id,
            'zoneid' : zoneId,
        })
    
    def listTemplates(self, templateFilter, account = "", domainId = "", hypervisor = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = "", zoneId = ""):
        '''
        List all public, private, and privileged templates.
        '''

        return self.request("listTemplates", {
            'templatefilter' : templateFilter,
            'account' : account,
            'domainid' : domainId,
            'hypervisor' : hypervisor,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'zoneid' : zoneId,
        })
    
    def updateTemplatePermissions(self, id, accounts = "", isExtractable = "", isFeatured = "", isPublic = "", op = "", projectids = ""):
        '''
        Updates a template visibility permissions. A public template is visible to all accounts within the same domain. A private template is visible only to the owner of the template. A priviledged template is a private template with account permissions added. Only accounts specified under the template permissions are visible to them.
        '''

        return self.request("updateTemplatePermissions", {
            'id' : id,
            'accounts' : accounts,
            'isextractable' : isExtractable,
            'isfeatured' : isFeatured,
            'ispublic' : isPublic,
            'op' : op,
            'projectids' : projectids,
        })
    
    def listTemplatePermissions(self, id):
        '''
        List template visibility and all accounts that have permissions to view this template.
        '''

        return self.request("listTemplatePermissions", {
            'id' : id,
        })
    
    def extractTemplate(self, id, mode, url = "", zoneId = ""):
        '''
        Extracts a template
        '''

        return self.request("extractTemplate", {
            'id' : id,
            'mode' : mode,
            'url' : url,
            'zoneid' : zoneId,
        })
    
    def prepareTemplate(self, templateId, zoneId):
        '''
        load template into primary storage
        '''

        return self.request("prepareTemplate", {
            'templateid' : templateId,
            'zoneid' : zoneId,
        })
    
    def attachIso(self, id, virtualMachineId):
        '''
        Attaches an ISO to a virtual machine.
        '''

        return self.request("attachIso", {
            'id' : id,
            'virtualmachineid' : virtualMachineId,
        })
    
    def detachIso(self, virtualMachineId):
        '''
        Detaches any ISO file (if any) currently attached to a virtual machine.
        '''

        return self.request("detachIso", {
            'virtualmachineid' : virtualMachineId,
        })
    
    def listIsos(self, account = "", bootable = "", domainId = "", hypervisor = "", id = "", isoFilter = "", isPublic = "", isReady = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = "", zoneId = ""):
        '''
        Lists all available ISO files.
        '''

        return self.request("listIsos", {
            'account' : account,
            'bootable' : bootable,
            'domainid' : domainId,
            'hypervisor' : hypervisor,
            'id' : id,
            'isofilter' : isoFilter,
            'ispublic' : isPublic,
            'isready' : isReady,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'zoneid' : zoneId,
        })
    
    def registerIso(self, displayText, name, url, zoneId, account = "", bootable = "", checksum = "", domainId = "", isExtractable = "", isFeatured = "", isPublic = "", osTypeId = "", projectId = ""):
        '''
        Registers an existing ISO into the Cloud.com Cloud.
        '''

        return self.request("registerIso", {
            'displaytext' : displayText,
            'name' : name,
            'url' : url,
            'zoneid' : zoneId,
            'account' : account,
            'bootable' : bootable,
            'checksum' : checksum,
            'domainid' : domainId,
            'isextractable' : isExtractable,
            'isfeatured' : isFeatured,
            'ispublic' : isPublic,
            'ostypeid' : osTypeId,
            'projectid' : projectId,
        })
    
    def updateIso(self, id, bootable = "", displayText = "", format = "", name = "", osTypeId = "", passwordEnabled = "", sortKey = ""):
        '''
        Updates an ISO file.
        '''

        return self.request("updateIso", {
            'id' : id,
            'bootable' : bootable,
            'displaytext' : displayText,
            'format' : format,
            'name' : name,
            'ostypeid' : osTypeId,
            'passwordenabled' : passwordEnabled,
            'sortkey' : sortKey,
        })
    
    def deleteIso(self, id, zoneId = ""):
        '''
        Deletes an ISO file.
        '''

        return self.request("deleteIso", {
            'id' : id,
            'zoneid' : zoneId,
        })
    
    def copyIso(self, id, destzoneId, sourceZoneId):
        '''
        Copies a template from one zone to another.
        '''

        return self.request("copyIso", {
            'id' : id,
            'destzoneid' : destzoneId,
            'sourcezoneid' : sourceZoneId,
        })
    
    def updateIsoPermissions(self, id, accounts = "", isExtractable = "", isFeatured = "", isPublic = "", op = "", projectids = ""):
        '''
        Updates iso permissions
        '''

        return self.request("updateIsoPermissions", {
            'id' : id,
            'accounts' : accounts,
            'isextractable' : isExtractable,
            'isfeatured' : isFeatured,
            'ispublic' : isPublic,
            'op' : op,
            'projectids' : projectids,
        })
    
    def listIsoPermissions(self, id):
        '''
        List template visibility and all accounts that have permissions to view this template.
        '''

        return self.request("listIsoPermissions", {
            'id' : id,
        })
    
    def extractIso(self, id, mode, url = "", zoneId = ""):
        '''
        Extracts an ISO
        '''

        return self.request("extractIso", {
            'id' : id,
            'mode' : mode,
            'url' : url,
            'zoneid' : zoneId,
        })
    
    def listPortForwardingRules(self, account = "", domainId = "", id = "", ipAddressId = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = ""):
        '''
        Lists all port forwarding rules for an IP address.
        '''

        return self.request("listPortForwardingRules", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'ipaddressid' : ipAddressId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
        })
    
    def createPortForwardingRule(self, ipAddressId, privatePort, protocol, publicPort, virtualMachineId, cidrList = "", openFirewall = ""):
        '''
        Creates a port forwarding rule
        '''

        return self.request("createPortForwardingRule", {
            'ipaddressid' : ipAddressId,
            'privateport' : privatePort,
            'protocol' : protocol,
            'publicport' : publicPort,
            'virtualmachineid' : virtualMachineId,
            'cidrlist' : cidrList,
            'openfirewall' : openFirewall,
        })
    
    def deletePortForwardingRule(self, id):
        '''
        Deletes a port forwarding rule
        '''

        return self.request("deletePortForwardingRule", {
            'id' : id,
        })
    
    def createFirewallRule(self, protocol, cidrList = "", endPort = "", icmpCode = "", icmpType = "", ipAddressId = "", startPort = "", type = ""):
        '''
        Creates a firewall rule for a given ip address
        '''

        return self.request("createFirewallRule", {
            'protocol' : protocol,
            'cidrlist' : cidrList,
            'endport' : endPort,
            'icmpcode' : icmpCode,
            'icmptype' : icmpType,
            'ipaddressid' : ipAddressId,
            'startport' : startPort,
            'type' : type,
        })
    
    def deleteFirewallRule(self, id):
        '''
        Deletes a firewall rule
        '''

        return self.request("deleteFirewallRule", {
            'id' : id,
        })
    
    def listFirewallRules(self, account = "", domainId = "", id = "", ipAddressId = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = ""):
        '''
        Lists all firewall rules for an IP address.
        '''

        return self.request("listFirewallRules", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'ipaddressid' : ipAddressId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
        })
    
    def addSrxFirewall(self, networkDeviceType, password, physicalNetworkId, url, userName):
        '''
        Adds a SRX firewall device
        '''

        return self.request("addSrxFirewall", {
            'networkdevicetype' : networkDeviceType,
            'password' : password,
            'physicalnetworkid' : physicalNetworkId,
            'url' : url,
            'username' : userName,
        })
    
    def deleteSrxFirewall(self, fwDeviceId):
        '''
        delete a SRX firewall device
        '''

        return self.request("deleteSrxFirewall", {
            'fwdeviceid' : fwDeviceId,
        })
    
    def configureSrxFirewall(self, fwDeviceId, fwDeviceCapacity = ""):
        '''
        Configures a SRX firewall device
        '''

        return self.request("configureSrxFirewall", {
            'fwdeviceid' : fwDeviceId,
            'fwdevicecapacity' : fwDeviceCapacity,
        })
    
    def listSrxFirewalls(self, fwDeviceId = "", keyword = "", page = "", pageSize = "", physicalNetworkId = ""):
        '''
        lists SRX firewall devices in a physical network
        '''

        return self.request("listSrxFirewalls", {
            'fwdeviceid' : fwDeviceId,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'physicalnetworkid' : physicalNetworkId,
        })
    
    def startRouter(self, id):
        '''
        Starts a router.
        '''

        return self.request("startRouter", {
            'id' : id,
        })
    
    def rebootRouter(self, id):
        '''
        Starts a router.
        '''

        return self.request("rebootRouter", {
            'id' : id,
        })
    
    def stopRouter(self, id, forced = ""):
        '''
        Stops a router.
        '''

        return self.request("stopRouter", {
            'id' : id,
            'forced' : forced,
        })
    
    def destroyRouter(self, id):
        '''
        Destroys a router.
        '''

        return self.request("destroyRouter", {
            'id' : id,
        })
    
    def changeServiceForRouter(self, id, serviceOfferingId):
        '''
        Upgrades domain router to a new service offering
        '''

        return self.request("changeServiceForRouter", {
            'id' : id,
            'serviceofferingid' : serviceOfferingId,
        })
    
    def listRouters(self, account = "", domainId = "", hostId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", networkId = "", page = "", pageSize = "", podId = "", projectId = "", state = "", zoneId = ""):
        '''
        List routers.
        '''

        return self.request("listRouters", {
            'account' : account,
            'domainid' : domainId,
            'hostid' : hostId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'podid' : podId,
            'projectid' : projectId,
            'state' : state,
            'zoneid' : zoneId,
        })
    
    def createVirtualRouterElement(self, nspId):
        '''
        Create a virtual router element.
        '''

        return self.request("createVirtualRouterElement", {
            'nspid' : nspId,
        })
    
    def configureVirtualRouterElement(self, id, enabled):
        '''
        Configures a virtual router element.
        '''

        return self.request("configureVirtualRouterElement", {
            'id' : id,
            'enabled' : enabled,
        })
    
    def listVirtualRouterElements(self, enabled = "", id = "", keyword = "", nspId = "", page = "", pageSize = ""):
        '''
        Lists all available virtual router elements.
        '''

        return self.request("listVirtualRouterElements", {
            'enabled' : enabled,
            'id' : id,
            'keyword' : keyword,
            'nspid' : nspId,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def createProject(self, displayText, name, account = "", domainId = ""):
        '''
        Creates a project
        '''

        return self.request("createProject", {
            'displaytext' : displayText,
            'name' : name,
            'account' : account,
            'domainid' : domainId,
        })
    
    def deleteProject(self, id):
        '''
        Deletes a project
        '''

        return self.request("deleteProject", {
            'id' : id,
        })
    
    def updateProject(self, id, account = "", displayText = ""):
        '''
        Updates a project
        '''

        return self.request("updateProject", {
            'id' : id,
            'account' : account,
            'displaytext' : displayText,
        })
    
    def activateProject(self, id):
        '''
        Activates a project
        '''

        return self.request("activateProject", {
            'id' : id,
        })
    
    def suspendProject(self, id):
        '''
        Suspends a project
        '''

        return self.request("suspendProject", {
            'id' : id,
        })
    
    def listProjects(self, account = "", displayText = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", state = ""):
        '''
        Lists projects and provides detailed information for listed projects
        '''

        return self.request("listProjects", {
            'account' : account,
            'displaytext' : displayText,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'state' : state,
        })
    
    def listProjectInvitations(self, account = "", activeOnly = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", state = ""):
        '''
        Lists projects and provides detailed information for listed projects
        '''

        return self.request("listProjectInvitations", {
            'account' : account,
            'activeonly' : activeOnly,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'state' : state,
        })
    
    def updateProjectInvitation(self, projectId, accept = "", account = "", token = ""):
        '''
        Accepts or declines project invitation
        '''

        return self.request("updateProjectInvitation", {
            'projectid' : projectId,
            'accept' : accept,
            'account' : account,
            'token' : token,
        })
    
    def deleteProjectInvitation(self, id):
        '''
        Accepts or declines project invitation
        '''

        return self.request("deleteProjectInvitation", {
            'id' : id,
        })
    
    def addHost(self, hypervisor, password, url, userName, zoneId, allocationState = "", clusterId = "", clusterName = "", hosttags = "", podId = ""):
        '''
        Adds a new host.
        '''

        return self.request("addHost", {
            'hypervisor' : hypervisor,
            'password' : password,
            'url' : url,
            'username' : userName,
            'zoneid' : zoneId,
            'allocationstate' : allocationState,
            'clusterid' : clusterId,
            'clustername' : clusterName,
            'hosttags' : hosttags,
            'podid' : podId,
        })
    
    def reconnectHost(self, id):
        '''
        Reconnects a host.
        '''

        return self.request("reconnectHost", {
            'id' : id,
        })
    
    def updateHost(self, id, allocationState = "", hosttags = "", osCategoryId = "", url = ""):
        '''
        Updates a host.
        '''

        return self.request("updateHost", {
            'id' : id,
            'allocationstate' : allocationState,
            'hosttags' : hosttags,
            'oscategoryid' : osCategoryId,
            'url' : url,
        })
    
    def deleteHost(self, id, forced = "", forceDestroyLocalStorage = ""):
        '''
        Deletes a host.
        '''

        return self.request("deleteHost", {
            'id' : id,
            'forced' : forced,
            'forcedestroylocalstorage' : forceDestroyLocalStorage,
        })
    
    def prepareHostForMaintenance(self, id):
        '''
        Prepares a host for maintenance.
        '''

        return self.request("prepareHostForMaintenance", {
            'id' : id,
        })
    
    def cancelHostMaintenance(self, id):
        '''
        Cancels host maintenance.
        '''

        return self.request("cancelHostMaintenance", {
            'id' : id,
        })
    
    def listHosts(self, clusterId = "", details = "", id = "", keyword = "", name = "", page = "", pageSize = "", podId = "", resourcestate = "", state = "", type = "", virtualMachineId = "", zoneId = ""):
        '''
        Lists hosts.
        '''

        return self.request("listHosts", {
            'clusterid' : clusterId,
            'details' : details,
            'id' : id,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'podid' : podId,
            'resourcestate' : resourcestate,
            'state' : state,
            'type' : type,
            'virtualmachineid' : virtualMachineId,
            'zoneid' : zoneId,
        })
    
    def addSecondaryStorage(self, url, zoneId = ""):
        '''
        Adds secondary storage.
        '''

        return self.request("addSecondaryStorage", {
            'url' : url,
            'zoneid' : zoneId,
        })
    
    def updateHostPassword(self, password, userName, clusterId = "", hostId = ""):
        '''
        Update password of a host/pool on management server.
        '''

        return self.request("updateHostPassword", {
            'password' : password,
            'username' : userName,
            'clusterid' : clusterId,
            'hostid' : hostId,
        })
    
    def createAccount(self, accountType, email, firstName, lastname, password, userName, account = "", accountDetails = "", domainId = "", networkDomain = "", timezone = ""):
        '''
        Creates an account
        '''

        return self.request("createAccount", {
            'accounttype' : accountType,
            'email' : email,
            'firstname' : firstName,
            'lastname' : lastname,
            'password' : password,
            'username' : userName,
            'account' : account,
            'accountdetails' : accountDetails,
            'domainid' : domainId,
            'networkdomain' : networkDomain,
            'timezone' : timezone,
        })
    
    def deleteAccount(self, id):
        '''
        Deletes a account, and all users associated with this account
        '''

        return self.request("deleteAccount", {
            'id' : id,
        })
    
    def updateAccount(self, newName, account = "", accountDetails = "", domainId = "", id = "", networkDomain = ""):
        '''
        Updates account information for the authenticated user
        '''

        return self.request("updateAccount", {
            'newname' : newName,
            'account' : account,
            'accountdetails' : accountDetails,
            'domainid' : domainId,
            'id' : id,
            'networkdomain' : networkDomain,
        })
    
    def disableAccount(self, lock, account = "", domainId = "", id = ""):
        '''
        Disables an account
        '''

        return self.request("disableAccount", {
            'lock' : lock,
            'account' : account,
            'domainid' : domainId,
            'id' : id,
        })
    
    def enableAccount(self, account = "", domainId = "", id = ""):
        '''
        Enables an account
        '''

        return self.request("enableAccount", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
        })
    
    def listAccounts(self, accountType = "", domainId = "", id = "", isCleanUpRequired = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", state = ""):
        '''
        Lists accounts and provides detailed account information for listed accounts
        '''

        return self.request("listAccounts", {
            'accounttype' : accountType,
            'domainid' : domainId,
            'id' : id,
            'iscleanuprequired' : isCleanUpRequired,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'state' : state,
        })
    
    def addAccountToProject(self, projectId, account = "", email = ""):
        '''
        Adds acoount to a project
        '''

        return self.request("addAccountToProject", {
            'projectid' : projectId,
            'account' : account,
            'email' : email,
        })
    
    def deleteAccountFromProject(self, account, projectId):
        '''
        Deletes account from the project
        '''

        return self.request("deleteAccountFromProject", {
            'account' : account,
            'projectid' : projectId,
        })
    
    def listProjectAccounts(self, projectId, account = "", keyword = "", page = "", pageSize = "", role = ""):
        '''
        Lists project's accounts
        '''

        return self.request("listProjectAccounts", {
            'projectid' : projectId,
            'account' : account,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'role' : role,
        })
    
    def listStoragePools(self, clusterId = "", id = "", ipAddress = "", keyword = "", name = "", page = "", pageSize = "", path = "", podId = "", zoneId = ""):
        '''
        Lists storage pools.
        '''

        return self.request("listStoragePools", {
            'clusterid' : clusterId,
            'id' : id,
            'ipaddress' : ipAddress,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'path' : path,
            'podid' : podId,
            'zoneid' : zoneId,
        })
    
    def createStoragePool(self, name, url, zoneId, clusterId = "", details = "", podId = "", tags = ""):
        '''
        Creates a storage pool.
        '''

        return self.request("createStoragePool", {
            'name' : name,
            'url' : url,
            'zoneid' : zoneId,
            'clusterid' : clusterId,
            'details' : details,
            'podid' : podId,
            'tags' : tags,
        })
    
    def updateStoragePool(self, id, tags = ""):
        '''
        Updates a storage pool.
        '''

        return self.request("updateStoragePool", {
            'id' : id,
            'tags' : tags,
        })
    
    def deleteStoragePool(self, id):
        '''
        Deletes a storage pool.
        '''

        return self.request("deleteStoragePool", {
            'id' : id,
        })
    
    def createPool(self, algorithm, name):
        '''
        Create a pool
        '''

        return self.request("createPool", {
            'algorithm' : algorithm,
            'name' : name,
        })
    
    def deletePool(self, poolName):
        '''
        Delete a pool
        '''

        return self.request("deletePool", {
            'poolname' : poolName,
        })
    
    def modifyPool(self, algorithm, poolName):
        '''
        Modify pool
        '''

        return self.request("modifyPool", {
            'algorithm' : algorithm,
            'poolname' : poolName,
        })
    
    def listPools(self, ):
        '''
        List Pool
        '''

        return self.request("listPools", {
        })
    
    def createSecurityGroup(self, name, account = "", description = "", domainId = "", projectId = ""):
        '''
        Creates a security group
        '''

        return self.request("createSecurityGroup", {
            'name' : name,
            'account' : account,
            'description' : description,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def deleteSecurityGroup(self, account = "", domainId = "", id = "", name = "", projectId = ""):
        '''
        Deletes security group
        '''

        return self.request("deleteSecurityGroup", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'name' : name,
            'projectid' : projectId,
        })
    
    def authorizeSecurityGroupIngress(self, account = "", cidrList = "", domainId = "", endPort = "", icmpCode = "", icmpType = "", projectId = "", protocol = "", securityGroupId = "", securityGroupName = "", startPort = "", userSecurityGroupList = ""):
        '''
        Authorizes a particular ingress rule for this security group
        '''

        return self.request("authorizeSecurityGroupIngress", {
            'account' : account,
            'cidrlist' : cidrList,
            'domainid' : domainId,
            'endport' : endPort,
            'icmpcode' : icmpCode,
            'icmptype' : icmpType,
            'projectid' : projectId,
            'protocol' : protocol,
            'securitygroupid' : securityGroupId,
            'securitygroupname' : securityGroupName,
            'startport' : startPort,
            'usersecuritygrouplist' : userSecurityGroupList,
        })
    
    def revokeSecurityGroupIngress(self, id):
        '''
        Deletes a particular ingress rule from this security group
        '''

        return self.request("revokeSecurityGroupIngress", {
            'id' : id,
        })
    
    def authorizeSecurityGroupEgress(self, account = "", cidrList = "", domainId = "", endPort = "", icmpCode = "", icmpType = "", projectId = "", protocol = "", securityGroupId = "", securityGroupName = "", startPort = "", userSecurityGroupList = ""):
        '''
        Authorizes a particular egress rule for this security group
        '''

        return self.request("authorizeSecurityGroupEgress", {
            'account' : account,
            'cidrlist' : cidrList,
            'domainid' : domainId,
            'endport' : endPort,
            'icmpcode' : icmpCode,
            'icmptype' : icmpType,
            'projectid' : projectId,
            'protocol' : protocol,
            'securitygroupid' : securityGroupId,
            'securitygroupname' : securityGroupName,
            'startport' : startPort,
            'usersecuritygrouplist' : userSecurityGroupList,
        })
    
    def revokeSecurityGroupEgress(self, id):
        '''
        Deletes a particular egress rule from this security group
        '''

        return self.request("revokeSecurityGroupEgress", {
            'id' : id,
        })
    
    def listSecurityGroups(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", securityGroupName = "", virtualMachineId = ""):
        '''
        Lists security groups
        '''

        return self.request("listSecurityGroups", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'securitygroupname' : securityGroupName,
            'virtualmachineid' : virtualMachineId,
        })
    
    def startSystemVm(self, id):
        '''
        Starts a system virtual machine.
        '''

        return self.request("startSystemVm", {
            'id' : id,
        })
    
    def rebootSystemVm(self, id):
        '''
        Reboots a system VM.
        '''

        return self.request("rebootSystemVm", {
            'id' : id,
        })
    
    def stopSystemVm(self, id, forced = ""):
        '''
        Stops a system VM.
        '''

        return self.request("stopSystemVm", {
            'id' : id,
            'forced' : forced,
        })
    
    def destroySystemVm(self, id):
        '''
        Destroyes a system virtual machine.
        '''

        return self.request("destroySystemVm", {
            'id' : id,
        })
    
    def listSystemVms(self, hostId = "", id = "", keyword = "", name = "", page = "", pageSize = "", podId = "", state = "", systemVmType = "", zoneId = ""):
        '''
        List system virtual machines.
        '''

        return self.request("listSystemVms", {
            'hostid' : hostId,
            'id' : id,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'podid' : podId,
            'state' : state,
            'systemvmtype' : systemVmType,
            'zoneid' : zoneId,
        })
    
    def migrateSystemVm(self, hostId, virtualMachineId):
        '''
        Attempts Migration of a system virtual machine to the host specified.
        '''

        return self.request("migrateSystemVm", {
            'hostid' : hostId,
            'virtualmachineid' : virtualMachineId,
        })
    
    def createSnapshot(self, volumeId, account = "", domainId = "", policyId = ""):
        '''
        Creates an instant snapshot of a volume.
        '''

        return self.request("createSnapshot", {
            'volumeid' : volumeId,
            'account' : account,
            'domainid' : domainId,
            'policyid' : policyId,
        })
    
    def listSnapshots(self, account = "", domainId = "", id = "", intervalType = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = "", snapshotType = "", volumeId = ""):
        '''
        Lists all available snapshots for the account.
        '''

        return self.request("listSnapshots", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'intervaltype' : intervalType,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'snapshottype' : snapshotType,
            'volumeid' : volumeId,
        })
    
    def deleteSnapshot(self, id):
        '''
        Deletes a snapshot of a disk volume.
        '''

        return self.request("deleteSnapshot", {
            'id' : id,
        })
    
    def createSnapshotPolicy(self, intervalType, maxSnaps, schedule, timezone, volumeId):
        '''
        Creates a snapshot policy for the account.
        '''

        return self.request("createSnapshotPolicy", {
            'intervaltype' : intervalType,
            'maxsnaps' : maxSnaps,
            'schedule' : schedule,
            'timezone' : timezone,
            'volumeid' : volumeId,
        })
    
    def deleteSnapshotPolicies(self, id = "", ids = ""):
        '''
        Deletes snapshot policies for the account.
        '''

        return self.request("deleteSnapshotPolicies", {
            'id' : id,
            'ids' : ids,
        })
    
    def listSnapshotPolicies(self, volumeId, keyword = "", page = "", pageSize = ""):
        '''
        Lists snapshot policies.
        '''

        return self.request("listSnapshotPolicies", {
            'volumeid' : volumeId,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def createLunOnFiler(self, name, size):
        '''
        Create a LUN from a pool
        '''

        return self.request("createLunOnFiler", {
            'name' : name,
            'size' : size,
        })
    
    def destroyLunOnFiler(self, path):
        '''
        Destroy a LUN
        '''

        return self.request("destroyLunOnFiler", {
            'path' : path,
        })
    
    def listLunsOnFiler(self, poolName):
        '''
        List LUN
        '''

        return self.request("listLunsOnFiler", {
            'poolname' : poolName,
        })
    
    def associateLun(self, iqn, name):
        '''
        Associate a LUN with a guest IQN
        '''

        return self.request("associateLun", {
            'iqn' : iqn,
            'name' : name,
        })
    
    def dissociateLun(self, iqn, path):
        '''
        Dissociate a LUN
        '''

        return self.request("dissociateLun", {
            'iqn' : iqn,
            'path' : path,
        })
    
    def enableStaticNat(self, ipAddressId, virtualMachineId):
        '''
        Enables static nat for given ip address
        '''

        return self.request("enableStaticNat", {
            'ipaddressid' : ipAddressId,
            'virtualmachineid' : virtualMachineId,
        })
    
    def createIpForwardingRule(self, ipAddressId, protocol, startPort, cidrList = "", endPort = "", openFirewall = ""):
        '''
        Creates an ip forwarding rule
        '''

        return self.request("createIpForwardingRule", {
            'ipaddressid' : ipAddressId,
            'protocol' : protocol,
            'startport' : startPort,
            'cidrlist' : cidrList,
            'endport' : endPort,
            'openfirewall' : openFirewall,
        })
    
    def deleteIpForwardingRule(self, id):
        '''
        Deletes an ip forwarding rule
        '''

        return self.request("deleteIpForwardingRule", {
            'id' : id,
        })
    
    def listIpForwardingRules(self, account = "", domainId = "", id = "", ipAddressId = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", virtualMachineId = ""):
        '''
        List the ip forwarding rules
        '''

        return self.request("listIpForwardingRules", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'ipaddressid' : ipAddressId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'virtualmachineid' : virtualMachineId,
        })
    
    def disableStaticNat(self, ipAddressId):
        '''
        Disables static rule for given ip address
        '''

        return self.request("disableStaticNat", {
            'ipaddressid' : ipAddressId,
        })
    
    def createDomain(self, name, networkDomain = "", parentDomainId = ""):
        '''
        Creates a domain
        '''

        return self.request("createDomain", {
            'name' : name,
            'networkdomain' : networkDomain,
            'parentdomainid' : parentDomainId,
        })
    
    def updateDomain(self, id, name = "", networkDomain = ""):
        '''
        Updates a domain with a new name
        '''

        return self.request("updateDomain", {
            'id' : id,
            'name' : name,
            'networkdomain' : networkDomain,
        })
    
    def deleteDomain(self, id, cleanup = ""):
        '''
        Deletes a specified domain
        '''

        return self.request("deleteDomain", {
            'id' : id,
            'cleanup' : cleanup,
        })
    
    def listDomains(self, id = "", keyword = "", level = "", listAll = "", name = "", page = "", pageSize = ""):
        '''
        Lists domains and provides detailed information for listed domains
        '''

        return self.request("listDomains", {
            'id' : id,
            'keyword' : keyword,
            'level' : level,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listDomainChildren(self, id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = ""):
        '''
        Lists all children domains belonging to a specified domain
        '''

        return self.request("listDomainChildren", {
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def createZone(self, dns1, internalDns1, name, networkType, allocationState = "", dns2 = "", domain = "", domainId = "", guestCidrAddress = "", internalDns2 = "", securityGroupEnabled = ""):
        '''
        Creates a Zone.
        '''

        return self.request("createZone", {
            'dns1' : dns1,
            'internaldns1' : internalDns1,
            'name' : name,
            'networktype' : networkType,
            'allocationstate' : allocationState,
            'dns2' : dns2,
            'domain' : domain,
            'domainid' : domainId,
            'guestcidraddress' : guestCidrAddress,
            'internaldns2' : internalDns2,
            'securitygroupenabled' : securityGroupEnabled,
        })
    
    def updateZone(self, id, allocationState = "", details = "", dhcpProvider = "", dns1 = "", dns2 = "", dnsSearchOrder = "", domain = "", guestCidrAddress = "", internalDns1 = "", internalDns2 = "", isPublic = "", name = ""):
        '''
        Updates a Zone.
        '''

        return self.request("updateZone", {
            'id' : id,
            'allocationstate' : allocationState,
            'details' : details,
            'dhcpprovider' : dhcpProvider,
            'dns1' : dns1,
            'dns2' : dns2,
            'dnssearchorder' : dnsSearchOrder,
            'domain' : domain,
            'guestcidraddress' : guestCidrAddress,
            'internaldns1' : internalDns1,
            'internaldns2' : internalDns2,
            'ispublic' : isPublic,
            'name' : name,
        })
    
    def deleteZone(self, id):
        '''
        Deletes a Zone.
        '''

        return self.request("deleteZone", {
            'id' : id,
        })
    
    def listZones(self, available = "", domainId = "", id = "", keyword = "", page = "", pageSize = "", showCapacities = ""):
        '''
        Lists zones
        '''

        return self.request("listZones", {
            'available' : available,
            'domainid' : domainId,
            'id' : id,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'showcapacities' : showCapacities,
        })
    
    def createInstanceGroup(self, name, account = "", domainId = "", projectId = ""):
        '''
        Creates a vm group
        '''

        return self.request("createInstanceGroup", {
            'name' : name,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def deleteInstanceGroup(self, id):
        '''
        Deletes a vm group
        '''

        return self.request("deleteInstanceGroup", {
            'id' : id,
        })
    
    def updateInstanceGroup(self, id, name = ""):
        '''
        Updates a vm group
        '''

        return self.request("updateInstanceGroup", {
            'id' : id,
            'name' : name,
        })
    
    def listInstanceGroups(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = ""):
        '''
        Lists vm groups
        '''

        return self.request("listInstanceGroups", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
        })
    
    def createServiceOffering(self, cpuNumber, cpuSpeed, displayText, memory, name, domainId = "", hosttags = "", isSystem = "", limitCpuUse = "", networkRate = "", offerHa = "", storageType = "", systemVmType = "", tags = ""):
        '''
        Creates a service offering.
        '''

        return self.request("createServiceOffering", {
            'cpunumber' : cpuNumber,
            'cpuspeed' : cpuSpeed,
            'displaytext' : displayText,
            'memory' : memory,
            'name' : name,
            'domainid' : domainId,
            'hosttags' : hosttags,
            'issystem' : isSystem,
            'limitcpuuse' : limitCpuUse,
            'networkrate' : networkRate,
            'offerha' : offerHa,
            'storagetype' : storageType,
            'systemvmtype' : systemVmType,
            'tags' : tags,
        })
    
    def deleteServiceOffering(self, id):
        '''
        Deletes a service offering.
        '''

        return self.request("deleteServiceOffering", {
            'id' : id,
        })
    
    def updateServiceOffering(self, id, displayText = "", name = "", sortKey = ""):
        '''
        Updates a service offering.
        '''

        return self.request("updateServiceOffering", {
            'id' : id,
            'displaytext' : displayText,
            'name' : name,
            'sortkey' : sortKey,
        })
    
    def listServiceOfferings(self, domainId = "", id = "", isSystem = "", keyword = "", name = "", page = "", pageSize = "", systemVmType = "", virtualMachineId = ""):
        '''
        Lists all available service offerings.
        '''

        return self.request("listServiceOfferings", {
            'domainid' : domainId,
            'id' : id,
            'issystem' : isSystem,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'systemvmtype' : systemVmType,
            'virtualmachineid' : virtualMachineId,
        })
    
    def createPod(self, gateway, name, netmask, startIp, zoneId, allocationState = "", endIp = ""):
        '''
        Creates a new Pod.
        '''

        return self.request("createPod", {
            'gateway' : gateway,
            'name' : name,
            'netmask' : netmask,
            'startip' : startIp,
            'zoneid' : zoneId,
            'allocationstate' : allocationState,
            'endip' : endIp,
        })
    
    def updatePod(self, id, allocationState = "", endIp = "", gateway = "", name = "", netmask = "", startIp = ""):
        '''
        Updates a Pod.
        '''

        return self.request("updatePod", {
            'id' : id,
            'allocationstate' : allocationState,
            'endip' : endIp,
            'gateway' : gateway,
            'name' : name,
            'netmask' : netmask,
            'startip' : startIp,
        })
    
    def deletePod(self, id):
        '''
        Deletes a Pod.
        '''

        return self.request("deletePod", {
            'id' : id,
        })
    
    def listPods(self, allocationState = "", id = "", keyword = "", name = "", page = "", pageSize = "", showCapacities = "", zoneId = ""):
        '''
        Lists all Pods.
        '''

        return self.request("listPods", {
            'allocationstate' : allocationState,
            'id' : id,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'showcapacities' : showCapacities,
            'zoneid' : zoneId,
        })
    
    def createDiskOffering(self, displayText, name, customized = "", diskSize = "", domainId = "", tags = ""):
        '''
        Creates a disk offering.
        '''

        return self.request("createDiskOffering", {
            'displaytext' : displayText,
            'name' : name,
            'customized' : customized,
            'disksize' : diskSize,
            'domainid' : domainId,
            'tags' : tags,
        })
    
    def updateDiskOffering(self, id, displayText = "", name = "", sortKey = ""):
        '''
        Updates a disk offering.
        '''

        return self.request("updateDiskOffering", {
            'id' : id,
            'displaytext' : displayText,
            'name' : name,
            'sortkey' : sortKey,
        })
    
    def deleteDiskOffering(self, id):
        '''
        Updates a disk offering.
        '''

        return self.request("deleteDiskOffering", {
            'id' : id,
        })
    
    def listDiskOfferings(self, domainId = "", id = "", keyword = "", name = "", page = "", pageSize = ""):
        '''
        Lists all available disk offerings.
        '''

        return self.request("listDiskOfferings", {
            'domainid' : domainId,
            'id' : id,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def addCluster(self, clusterName, clusterType, hypervisor, zoneId, allocationState = "", password = "", podId = "", url = "", userName = ""):
        '''
        Adds a new cluster
        '''

        return self.request("addCluster", {
            'clustername' : clusterName,
            'clustertype' : clusterType,
            'hypervisor' : hypervisor,
            'zoneid' : zoneId,
            'allocationstate' : allocationState,
            'password' : password,
            'podid' : podId,
            'url' : url,
            'username' : userName,
        })
    
    def deleteCluster(self, id):
        '''
        Deletes a cluster.
        '''

        return self.request("deleteCluster", {
            'id' : id,
        })
    
    def updateCluster(self, id, allocationState = "", clusterName = "", clusterType = "", hypervisor = "", managedState = ""):
        '''
        Updates an existing cluster
        '''

        return self.request("updateCluster", {
            'id' : id,
            'allocationstate' : allocationState,
            'clustername' : clusterName,
            'clustertype' : clusterType,
            'hypervisor' : hypervisor,
            'managedstate' : managedState,
        })
    
    def listClusters(self, allocationState = "", clusterType = "", hypervisor = "", id = "", keyword = "", managedState = "", name = "", page = "", pageSize = "", podId = "", showCapacities = "", zoneId = ""):
        '''
        Lists clusters.
        '''

        return self.request("listClusters", {
            'allocationstate' : allocationState,
            'clustertype' : clusterType,
            'hypervisor' : hypervisor,
            'id' : id,
            'keyword' : keyword,
            'managedstate' : managedState,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'podid' : podId,
            'showcapacities' : showCapacities,
            'zoneid' : zoneId,
        })
    
    def createRemoteAccessVpn(self, publicIpId, account = "", domainId = "", ipRange = "", openFirewall = ""):
        '''
        Creates a l2tp/ipsec remote access vpn
        '''

        return self.request("createRemoteAccessVpn", {
            'publicipid' : publicIpId,
            'account' : account,
            'domainid' : domainId,
            'iprange' : ipRange,
            'openfirewall' : openFirewall,
        })
    
    def deleteRemoteAccessVpn(self, publicIpId):
        '''
        Destroys a l2tp/ipsec remote access vpn
        '''

        return self.request("deleteRemoteAccessVpn", {
            'publicipid' : publicIpId,
        })
    
    def listRemoteAccessVpns(self, publicIpId, account = "", domainId = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = ""):
        '''
        Lists remote access vpns
        '''

        return self.request("listRemoteAccessVpns", {
            'publicipid' : publicIpId,
            'account' : account,
            'domainid' : domainId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
        })
    
    def createVlanIpRange(self, startIp, account = "", domainId = "", endIp = "", forVirtualNetwork = "", gateway = "", netmask = "", networkId = "", physicalNetworkId = "", podId = "", projectId = "", vlan = "", zoneId = ""):
        '''
        Creates a VLAN IP range.
        '''

        return self.request("createVlanIpRange", {
            'startip' : startIp,
            'account' : account,
            'domainid' : domainId,
            'endip' : endIp,
            'forvirtualnetwork' : forVirtualNetwork,
            'gateway' : gateway,
            'netmask' : netmask,
            'networkid' : networkId,
            'physicalnetworkid' : physicalNetworkId,
            'podid' : podId,
            'projectid' : projectId,
            'vlan' : vlan,
            'zoneid' : zoneId,
        })
    
    def deleteVlanIpRange(self, id):
        '''
        Creates a VLAN IP range.
        '''

        return self.request("deleteVlanIpRange", {
            'id' : id,
        })
    
    def listVlanIpRanges(self, account = "", domainId = "", forVirtualNetwork = "", id = "", keyword = "", networkId = "", page = "", pageSize = "", physicalNetworkId = "", podId = "", projectId = "", vlan = "", zoneId = ""):
        '''
        Lists all VLAN IP ranges.
        '''

        return self.request("listVlanIpRanges", {
            'account' : account,
            'domainid' : domainId,
            'forvirtualnetwork' : forVirtualNetwork,
            'id' : id,
            'keyword' : keyword,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'physicalnetworkid' : physicalNetworkId,
            'podid' : podId,
            'projectid' : projectId,
            'vlan' : vlan,
            'zoneid' : zoneId,
        })
    
    def createSSHKeyPair(self, name, account = "", domainId = "", projectId = ""):
        '''
        Create a new keypair and returns the private key
        '''

        return self.request("createSSHKeyPair", {
            'name' : name,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def deleteSSHKeyPair(self, name, account = "", domainId = "", projectId = ""):
        '''
        Deletes a keypair by name
        '''

        return self.request("deleteSSHKeyPair", {
            'name' : name,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def listSSHKeyPairs(self, account = "", domainId = "", fingerprint = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = ""):
        '''
        List registered keypairs
        '''

        return self.request("listSSHKeyPairs", {
            'account' : account,
            'domainid' : domainId,
            'fingerprint' : fingerprint,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
        })
    
    def updateResourceLimit(self, resourceType, account = "", domainId = "", max = "", projectId = ""):
        '''
        Updates resource limits for an account or domain.
        '''

        return self.request("updateResourceLimit", {
            'resourcetype' : resourceType,
            'account' : account,
            'domainid' : domainId,
            'max' : max,
            'projectid' : projectId,
        })
    
    def updateResourceCount(self, domainId, account = "", projectId = "", resourceType = ""):
        '''
        Recalculate and update resource count for an account or domain.
        '''

        return self.request("updateResourceCount", {
            'domainid' : domainId,
            'account' : account,
            'projectid' : projectId,
            'resourcetype' : resourceType,
        })
    
    def listResourceLimits(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", resourceType = ""):
        '''
        Lists resource limits.
        '''

        return self.request("listResourceLimits", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'resourcetype' : resourceType,
        })
    
    def listHypervisors(self, zoneId = ""):
        '''
        List hypervisors
        '''

        return self.request("listHypervisors", {
            'zoneid' : zoneId,
        })
    
    def updateHypervisorCapabilities(self, id = "", maxGuestsLimit = "", securityGroupEnabled = ""):
        '''
        Updates a hypervisor capabilities.
        '''

        return self.request("updateHypervisorCapabilities", {
            'id' : id,
            'maxguestslimit' : maxGuestsLimit,
            'securitygroupenabled' : securityGroupEnabled,
        })
    
    def listHypervisorCapabilities(self, hypervisor = "", id = "", keyword = "", page = "", pageSize = ""):
        '''
        Lists all hypervisor capabilities.
        '''

        return self.request("listHypervisorCapabilities", {
            'hypervisor' : hypervisor,
            'id' : id,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def addExternalLoadBalancer(self, password, url, userName, zoneId):
        '''
        Adds F5 external load balancer appliance.
        '''

        return self.request("addExternalLoadBalancer", {
            'password' : password,
            'url' : url,
            'username' : userName,
            'zoneid' : zoneId,
        })
    
    def deleteExternalLoadBalancer(self, id):
        '''
        Deletes a F5 external load balancer appliance added in a zone.
        '''

        return self.request("deleteExternalLoadBalancer", {
            'id' : id,
        })
    
    def listExternalLoadBalancers(self, keyword = "", page = "", pageSize = "", zoneId = ""):
        '''
        Lists F5 external load balancer appliances added in a zone.
        '''

        return self.request("listExternalLoadBalancers", {
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'zoneid' : zoneId,
        })
    
    def addExternalFirewall(self, password, url, userName, zoneId):
        '''
        Adds an external firewall appliance
        '''

        return self.request("addExternalFirewall", {
            'password' : password,
            'url' : url,
            'username' : userName,
            'zoneid' : zoneId,
        })
    
    def deleteExternalFirewall(self, id):
        '''
        Deletes an external firewall appliance.
        '''

        return self.request("deleteExternalFirewall", {
            'id' : id,
        })
    
    def listExternalFirewalls(self, zoneId, keyword = "", page = "", pageSize = ""):
        '''
        List external firewall appliances.
        '''

        return self.request("listExternalFirewalls", {
            'zoneid' : zoneId,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def updateConfiguration(self, name, value = ""):
        '''
        Updates a configuration.
        '''

        return self.request("updateConfiguration", {
            'name' : name,
            'value' : value,
        })
    
    def listConfigurations(self, category = "", keyword = "", name = "", page = "", pageSize = ""):
        '''
        Lists all configurations.
        '''

        return self.request("listConfigurations", {
            'category' : category,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listCapabilities(self, ):
        '''
        Lists capabilities
        '''

        return self.request("listCapabilities", {
        })
    
    def associateIpAddress(self, account = "", domainId = "", networkId = "", projectId = "", zoneId = ""):
        '''
        Acquires and associates a public IP to an account.
        '''

        return self.request("associateIpAddress", {
            'account' : account,
            'domainid' : domainId,
            'networkid' : networkId,
            'projectid' : projectId,
            'zoneid' : zoneId,
        })
    
    def disassociateIpAddress(self, id):
        '''
        Disassociates an ip address from the account.
        '''

        return self.request("disassociateIpAddress", {
            'id' : id,
        })
    
    def listPublicIpAddresses(self, account = "", allocatedOnly = "", associatedNetworkId = "", domainId = "", forLoadBalancing = "", forVirtualNetwork = "", id = "", ipAddress = "", isRecursive = "", isSourceNat = "", isStaticNat = "", keyword = "", listAll = "", page = "", pageSize = "", physicalNetworkId = "", projectId = "", vlanId = "", zoneId = ""):
        '''
        Lists all public ip addresses
        '''

        return self.request("listPublicIpAddresses", {
            'account' : account,
            'allocatedonly' : allocatedOnly,
            'associatednetworkid' : associatedNetworkId,
            'domainid' : domainId,
            'forloadbalancing' : forLoadBalancing,
            'forvirtualnetwork' : forVirtualNetwork,
            'id' : id,
            'ipaddress' : ipAddress,
            'isrecursive' : isRecursive,
            'issourcenat' : isSourceNat,
            'isstaticnat' : isStaticNat,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'physicalnetworkid' : physicalNetworkId,
            'projectid' : projectId,
            'vlanid' : vlanId,
            'zoneid' : zoneId,
        })
    
    def addSwift(self, url, account = "", key = "", userName = ""):
        '''
        Adds Swift.
        '''

        return self.request("addSwift", {
            'url' : url,
            'account' : account,
            'key' : key,
            'username' : userName,
        })
    
    def listSwifts(self, id = "", keyword = "", page = "", pageSize = ""):
        '''
        List Swift.
        '''

        return self.request("listSwifts", {
            'id' : id,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def enableStorageMaintenance(self, id):
        '''
        Puts storage pool into maintenance state
        '''

        return self.request("enableStorageMaintenance", {
            'id' : id,
        })
    
    def cancelStorageMaintenance(self, id):
        '''
        Cancels maintenance for primary storage
        '''

        return self.request("cancelStorageMaintenance", {
            'id' : id,
        })
    
    def listOsTypes(self, id = "", keyword = "", osCategoryId = "", page = "", pageSize = ""):
        '''
        Lists all supported OS types for this cloud.
        '''

        return self.request("listOsTypes", {
            'id' : id,
            'keyword' : keyword,
            'oscategoryid' : osCategoryId,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listOsCategories(self, id = "", keyword = "", page = "", pageSize = ""):
        '''
        Lists all supported OS categories for this cloud.
        '''

        return self.request("listOsCategories", {
            'id' : id,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listEvents(self, account = "", domainId = "", duration = "", endDate = "", entryTime = "", id = "", isRecursive = "", keyword = "", level = "", listAll = "", page = "", pageSize = "", projectId = "", startDate = "", type = ""):
        '''
        A command to list events.
        '''

        return self.request("listEvents", {
            'account' : account,
            'domainid' : domainId,
            'duration' : duration,
            'enddate' : endDate,
            'entrytime' : entryTime,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'level' : level,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'startdate' : startDate,
            'type' : type,
        })
    
    def listEventTypes(self, ):
        '''
        List Event Types
        '''

        return self.request("listEventTypes", {
        })
    
    def queryAsyncJobResult(self, jobId):
        '''
        Retrieves the current status of asynchronous job.
        '''

        return self.request("queryAsyncJobResult", {
            'jobid' : jobId,
        })
    
    def listAsyncJobs(self, account = "", domainId = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", startDate = ""):
        '''
        Lists all pending asynchronous jobs for the account.
        '''

        return self.request("listAsyncJobs", {
            'account' : account,
            'domainid' : domainId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'startdate' : startDate,
        })
    
    def listCapacity(self, clusterId = "", fetchLatest = "", keyword = "", page = "", pageSize = "", podId = "", sortBy = "", type = "", zoneId = ""):
        '''
        Lists all the system wide capacities.
        '''

        return self.request("listCapacity", {
            'clusterid' : clusterId,
            'fetchlatest' : fetchLatest,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'podid' : podId,
            'sortby' : sortBy,
            'type' : type,
            'zoneid' : zoneId,
        })
    
    def registerSSHKeyPair(self, name, publicKey, account = "", domainId = "", projectId = ""):
        '''
        Register a public key in a keypair under a certain name
        '''

        return self.request("registerSSHKeyPair", {
            'name' : name,
            'publickey' : publicKey,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def logout(self, ):
        '''
        Logs out the user
        '''

        return self.request("logout", {
        })
    
    def login(self, userName, password, domain = "", domainId = ""):
        '''
        Logs a user into the CloudStack. A successful login attempt will generate a JSESSIONID cookie value that can be passed in subsequent Query command calls until the "logout" command has been issued or the session has expired.
        '''

        return self.request("login", {
            'username' : userName,
            'password' : password,
            'domain' : domain,
            'domainId' : domainId,
        })
    
    def ldapConfig(self, hostname, queryFilter, searchBase, bindDN = "", bindPass = "", port = "", ssl = "", trustStore = "", trustStorePass = ""):
        '''
        Configure the LDAP context for this site.
        '''

        return self.request("ldapConfig", {
            'hostname' : hostname,
            'queryfilter' : queryFilter,
            'searchbase' : searchBase,
            'binddn' : bindDN,
            'bindpass' : bindPass,
            'port' : port,
            'ssl' : ssl,
            'truststore' : trustStore,
            'truststorepass' : trustStorePass,
        })
    
    def getCloudIdentifier(self, userId):
        '''
        Retrieves a cloud identifier.
        '''

        return self.request("getCloudIdentifier", {
            'userid' : userId,
        })
    
    def uploadCustomCertificate(self, certificate, domainSuffix, id = "", name = "", privateKey = ""):
        '''
        Uploads custom certificate
        '''

        return self.request("uploadCustomCertificate", {
            'certificate' : certificate,
            'domainsuffix' : domainSuffix,
            'id' : id,
            'name' : name,
            'privatekey' : privateKey,
        })
    
    def listAlerts(self, id = "", keyword = "", page = "", pageSize = "", type = ""):
        '''
        Lists all alerts.
        '''

        return self.request("listAlerts", {
            'id' : id,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'type' : type,
        })
    
