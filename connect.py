import sys
import paramiko

ssh = paramiko.SSHClient()
# Load SSH host keys.
ssh.load_system_host_keys()
# Add SSH host key when missing.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#credentials = get_credentials()
#print(sys.argv)
IP = sys.argv[2]
uname = sys.argv[1]
passw = sys.argv[3]
ssh.connect(IP, username=uname, password=passw)
print("Successfully connected to ", IP)
pmac_shell = ssh.invoke_shell()
