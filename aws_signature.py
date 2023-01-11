import hmac
import hashlib

# This string to sign taken from: http://docs.amazonwebservices.com/amazonglacier/latest/dev/amazon-glacier-signing-requests.html#example-signature-calculation
sts = "AWS4-HMAC-SHA256\n20130524T000000Z\n20130524/us-east-1/s3/aws4_request\n7344ae5b7ee6c3e7e6b0fe0640412a37625d1fbfff95c48bbb2dc43964946972"
#print(sts)

secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
aws_region = "us-east-1"
aws_service = "s3"
yyyymmdd = "20130524"

date_key = hmac.new(key=("AWS4"+secret_access_key).encode('utf-8'), msg=yyyymmdd.encode('utf-8'), digestmod=hashlib.sha256).digest()
date_region_key = hmac.new(key=date_key, msg=aws_region.encode('utf-8'), digestmod=hashlib.sha256).digest()
date_region_service_key = hmac.new(key=date_region_key, msg=aws_service.encode('utf-8'), digestmod=hashlib.sha256).digest()
signing_key = hmac.new(key=date_region_service_key, msg=b"aws4_request", digestmod=hashlib.sha256).digest()
signature_key = hmac.new(key=signing_key, msg=sts.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
print(signature_key)