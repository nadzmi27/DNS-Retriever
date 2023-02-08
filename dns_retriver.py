import subprocess
command = ['cmd', '/c', 'ipconfig', '/displaydns']
out = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()
lines = stdout.splitlines()
lst = [str(i)[29:-1].strip() for i in lines if "Record Name" in str(i)]
with open(file="history.txt", mode="w") as f:
    for i in sorted(set(lst)):
        string = i + "\n"
        f.write(string)
