from pysnmp.smi import builder, view , error

mibBuilder = builder.MibBuilder()
mibViewController = view.MibViewController(mibBuilder)
mibBuilder.loadModules('SNMPv2-MIB', 'SNMP-COMMUNITY-MIB')
mibView = view.MibViewController(mibBuilder)
modName, symName, suffix = mibView.getNodeLocation(('snmpCommunityEntry',))
rowNode, = mibBuilder.importSymbols(modName, symName)
oid = rowNode.getInstIdFromIndices('router')
oid, label, suffix = mibView.getFirstNodeName()
while True:
    try:
        modName, nodeDesc, suffix = mibView.getNodeLocation(oid)
        print('%s::%s == %s' % (modName, nodeDesc, oid))
        oid, label, suffix = mibView.getNextNodeName(oid)

    except error.NoSuchObjectError:
        break

