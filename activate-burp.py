import sys, pexpect.popen_spawn, signal

if len(sys.argv) != 3:
    print('Usage: activate-burp [yes/no] [license-file]')
    sys.exit(1)

if sys.argv[1] != 'yes':
    print('You must accept the license to use Burp')
    sys.exit(1)

license = open(sys.argv[2]).read()

child = pexpect.popen_spawn.PopenSpawn('java -Djava.awt.headless=true -jar "burpsuite_pro_v2024.6.6.jar"', encoding='cp437')
#child.logfile = sys.stdout

child.expect('Do you accept the license agreement\\? \\(y/n\\)')
child.sendline('y')

child.expect('please paste your license key below.')
child.sendline(license)

child.expect('Enter preferred activation method')
child.sendline('o')

child.expect('Your license is successfully installed and activated.')
child.kill(signal.SIGTERM)
print('Your license is successfully installed and activated.')