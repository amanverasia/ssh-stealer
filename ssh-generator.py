import subprocess

try:
    subprocess.run([
        'ssh-keygen', 
        '-t', 'rsa', 
        '-b', '4096',
        '-f', 'id_rsa',
        '-N', ''
    ], input='\n\n\n', text=True, check=True)
    print('SSH key pair generated successfully!')
except subprocess.CalledProcessError:
    print('Error generating SSH keys.')
