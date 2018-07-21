



MyDict={'TCPMUX':1,'RJE':5,'PING':7,'DAYTIME':13,'MSP':18,'FTP-Data':20,'FTP-Control':21,'SSH':22,'Telnet':23,'SMTP':25,'MSG ICP':29,'TIME':37,'Nameserv':42,'Whois':43,'Login':49,'DNS':53,'DHCP-server':67,'DHCP-client':68,'TFTP':69,'Gopher':70,'Finger':79,'HTTP':80,'Kerberos':88,'X.400':103,'SNA':108,'POP2':109,'POP3':110,'SFTP':115,'SQL':118,'NNTP':119,'NetBIOS':137,'IMAP':143,'SNMP':161,'BGP':179,'GACP':190,'IRC':194,'DLS':197,'IPX':213,'LDAP':389,'HTTPS':443,'SNPP':444,'DHCPv6-client':546,'DHCPv6-server':547,'NTTPS':563,'MSN':569,'LDAPS':636,'FTPS-DATA':989,'FTPS':990,'TenetS':992,'IMAP4S':993,'IRCS':994,'POP3S':995}
f=0
while f == 0:
    UInput = input("Enter Port Name: ")
    if UInput in MyDict:
        print("{key} port number is {value}".format(key=UInput, value=MyDict[UInput]))
    else:
        print("This is not a protocol")