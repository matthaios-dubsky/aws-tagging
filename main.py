import os
import subprocess
import boto3

regions = [
  "ca-central-1",
]

services = [
  #"ec2",
  "s3"
]

data_dir = "./data"

def fetch_resources(region, dir):
  cmd = f"aws-list-all query --region {region} --directory {dir}"
  os.system(cmd)

def extract(e):
  return {
    ""
  } 

def process_raw_info(raw, service):
  decoded = raw.decode("utf-8").replace("\n", "").split(service)
  get_region = lambda n: n.strip().split(" ")[0]
  get_identifier = lambda x: [n.strip() for n in x.strip().split(" - ")[1:]]
  return [{
      "service": service,
      "region": get_region(n),
      "identifier": get_identifier(n) 
    } for n in decoded if n ]


def get_resource_info(service, dir):
  cmd = f"aws-list-all show --verbose {dir}/{service}*"
  raw = subprocess.check_output(cmd, shell=True)
  return process_raw_info(raw, service) 


def main():
  print("Fetch all aws resources by regions")
  #for region in regions:
  # fetch_resources(region, data_dir)

  print("get resource info by service")
  info = get_resource_info(services[0], data_dir)
  print(info)

if __name__ == "__main__":
    main()