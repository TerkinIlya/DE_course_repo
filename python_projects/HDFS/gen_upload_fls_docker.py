import os
import shutil
import csv
import paramiko
from scp import SCPClient

data_folder = '/home/ilya/github/DE_course_repo/python_projects/HDFS/data'
file_path = os.path.join(data_folder, 'file_to_upload.txt')
prefix = 'letter_'
upload_folder = os.path.join(data_folder, 'files_to_upload')
if os.path.exists(upload_folder):
    shutil.rmtree(upload_folder)
os.makedirs(upload_folder)

with open(file_path) as fl:
    file = fl.read()

for letter in file:
    if letter.isalpha():
        letter = letter.lower()
        with open(f'{upload_folder}/{prefix}{letter}.csv',
                  'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([letter])

# Подключение к удаленной машине
remote_host = '158.160.170.94'
remote_user = 'ilya'
ssh_key_path = '/home/ilya/.ssh/id_rsa'
remote_tmp_path = '/home/ilya'
remote_upload_path = f'{remote_tmp_path}/files_to_upload'
container_name_filter = 'namenode'
container_target_path = '/tmp/'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(remote_host, username=remote_user, key_filename=ssh_key_path)

# Копирование на удалённую ВМ
with SCPClient(ssh.get_transport()) as scp:
    scp.put(upload_folder, recursive=True, remote_path=remote_tmp_path)

# Поиск контейнера
find_container_cmd = (f"docker ps --filter 'name={container_name_filter}' "
                      f"--format '{{{{.ID}}}}'")
stdin, stdout, stderr = ssh.exec_command(find_container_cmd)
container_id = stdout.read().decode().strip()

if not container_id:
    print("Контейнер с namenode не найден.")
else:
    print(f"Найден контейнер: {container_id}")

    # Копирование в контейнер
    copy_cmd = (f"docker cp {remote_upload_path} {container_id}:"
                f"{container_target_path}")
    stdin, stdout, stderr = ssh.exec_command(copy_cmd)
    print("STDOUT:", stdout.read().decode())
    print("STDERR:", stderr.read().decode())

hdfs_path = '/opt/hadoop-2.7.4/bin//hdfs'

exec_hdfs_put = (
    f'docker exec {container_id} bash -c '
    f'"{hdfs_path} dfs -mkdir -p /letters && '
    f'{hdfs_path} dfs -put -f /tmp/files_to_upload/* /letters/"'
)

stdin, stdout, stderr = ssh.exec_command(exec_hdfs_put)
print(stdout.read().decode())
print(stderr.read().decode())

ssh.close()
