from cloudant.client import Cloudant

client = Cloudant.iam('username','apikey',connect=True)

my_database = client.create_database('my_database')
