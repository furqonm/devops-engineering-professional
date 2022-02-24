# Masukan dependency Boto3 yang merupakan AWS SDK untuk Python dan OS untuk mengambil environment variable
import boto3, os

# Untuk mencari informasi semua EC2 instances yang running dengan tag tertentu.
filters = [{
            'Name': 'tag:' + os.environ['tag'],
            'Values': [os.environ['value']]
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]

# Menggunakan Boto3 agar aplikasi bisa komunikasi dengan service AWS.
ec2 = boto3.resource('ec2')

# Fungsi main/default dari Lambda function
def lambda_handler(event, context):

    # Mengkoleksi semua instance yang jalan.
    instances = ec2.instances.filter(Filters=filters)
    runningInstances = [instance.id for instance in instances]

# Memastikan apakah ada instance yang akan dimatikan. 
    if len(runningInstances) > 0:
# Mencoba mematikan beberapa instance berdasarkan filter
        try:
          turnOff = ec2.instances.filter(InstanceIds=runningInstances).stop()
          print(turnOff)
        except:
# Rekam kedalam log jika instance gagal untuk dimatikan. Periksa IAM Policy pada Role yang diberikan kepada AWS Lambda.
          print('You have failed to stopped an EC2 instance')
# Rekam kedalam log jika tidak ada instance yang bisa dimatikan.
    else:
        print('EC2 instances not found')