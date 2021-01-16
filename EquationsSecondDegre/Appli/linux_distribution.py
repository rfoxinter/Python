def id_like():
    linux_distribution=''
    os_dict={}
    with open('/etc/os-release','r') as f:
        for line in f:
            line=line.split('=')
            os_dict[line[0]]=line[1].replace('\n','').replace('"','')
    try:
        linux_distribution=os_dict['ID_LIKE']
    except:
        linux_distribution=os_dict['ID']
    return linux_distribution

def id():
    linux_distribution=''
    os_dict={}
    with open('/etc/os-release','r') as f:
        for line in f:
            line=line.split('=')
            os_dict[line[0]]=line[1].replace('\n','').replace('"','')
    linux_distribution=os_dict['ID']
    return linux_distribution
