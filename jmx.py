#!/usr/bin/python

import sys

server = sys.argv[1]
port = sys.argv[2]

userName = sys.argv[5]
passWord = sys.argv[6]
authType = sys.argv[7]
srvurl = "t3://" + str(server) + ":" + str(port)

redirect('/dev/null', 'false')

if authType == "KEY":
	connect(userConfigFile=userName, userKeyFile=passWord, url=srvurl)
	#serverRuntime()
elif authType == "USRPW":
	connect(userName, passWord, url=srvurl)
	#serverRuntime()
else:
	print "No Connection"

state = sys.argv[3]
mgserver = sys.argv[4]

if state =="PermGen":
        domainCustom()
        cd('java.lang/java.lang:Location='+mgserver+',name=Perm Gen,type=MemoryPool')
        hstate = get('CollectionUsage')
        print state + ":"+`hstate`
        exit()
if state == "HealthState":
	domainRuntime()
	hstate = get(state)
	print state + ":"+`hstate`
	##discconect()
	exit()
elif state == "OverallHealthState":
	domainRuntime()
	hstate = get(state)
	print state + ":"+`hstate`
	##discconect()
	exit()
elif state == "ThreadHealthState":
	domainRuntime()
	cd('/ThreadPoolRuntime/ThreadPoolRuntime')
	hstate = get('HealthState')
	print state + ":"+`hstate`
	##discconect()
	exit()
elif state == "JDBCHealthState":
	domainRuntime()
	cd('/JDBCServiceRuntime/' + mgserver)
	hstate = get('HealthState')
	print state + ":"+`hstate`
	##discconect()
	exit()
elif state == "HeapFreePercent":
	domainRuntime()
	cd('/JVMRuntime/' + mgserver)
	hpercent = int(get('HeapFreePercent'))
	##print 'HeapFreePercent:'+ `hpercent`
	print state + ":"+ `hpercent`
	##disconnect()
	exit()
elif state == "StuckThreadCount":
	domainRuntime()
	cd('/ThreadPoolRuntime/ThreadPoolRuntime')
	hsthrd = int(get('StuckThreadCount'))
	print state + ":"+`hsthrd`:wq
	exit()
elif state == "ThreadTotCount":
	domainRuntime()
	cd('/ThreadPoolRuntime/ThreadPoolRuntime')
	hthrdcnt = int(get('ExecuteThreadTotalCount'))
	print state + ":"+`hthrdcnt`
	exit()
else:
	print "Invalid State:", state
	
	
