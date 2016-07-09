
import subprocess
import time
proc = subprocess.Popen(
    ['echo', 'Hello from the child!'],
    stdout=subprocess.PIPE
)
out, err = proc.communicate()
print(out.decode('utf-8'))
# >>>
# Hello from the child!


proc = subprocess.Popen(['sleep', '0.3'])
while proc.poll() is None:
    print('Working...')
    # some time consuming work here
    time.sleep(0.2)
print('Exit status', proc.poll())
# >>>
# Working...
# Working...
# Exit status 0


def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc

start = time.time()
procs = []
for _ in range(10):
    proc = run_sleep(0.1)
    procs.append(proc)

for proc in procs:
    proc.communicate()
end = time.time()
print('Finished in %.3f seconds' % (end - start))
# >>>
# Finished in 0.120 seconds


def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'\xe24U\n\xd0Ql3S\x11'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc

import os
procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    procs.append(proc)

for proc in procs:
    out, err = proc.communicate()
    print(out[-10:])
# >>>
# b'\x9e\xfb\x93\xc9mC#R\x84\xbc'
# b'mPI\xc0\xb8\xa5\x1d\xa83\x8b'
# b'\xcf\xa9\xed9!\x96\xfa\x1e\xff\xe6'


def run_md5(input_stdin):
    proc = subprocess.Popen(
        ['md5'],
        stdin=input_stdin,
        stdout=subprocess.PIPE
    )
    return proc

input_procs = []
hash_procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    input_procs.append(proc) #
    hash_proc = run_md5(proc.stdout)
    hash_procs.append(hash_proc) #

for proc in input_procs:
    proc.communicate()

for proc in hash_procs:
    out, err = proc.communicate()
    print(out.strip())
# >>>
# b'd41d8cd98f00b204e9800998ecf8427e'
# b'd41d8cd98f00b204e9800998ecf8427e'
# b'091f9d7e1fb385829cf747476c6bb63a'


import sys
# above python 3.3 for timeout param
# The belows have to use module select at proc.stdin|stdout|stderr 
if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
    proc = run_sleep(10)
    try:
        proc.communicate(timeout=0.1)
    except subprocess.TimeoutExpired:
        proc.terminate()
        proc.wait()

    print('Exit status', proc.poll())
# >>>
# Exit status -15