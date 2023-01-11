import hashlib
import hmac
import binascii

# Replace with your own values
sts = "AWS4-HMAC-SHA256\n20130524T000000Z\n20130524/us-east-1/s3/aws4_request\n7344ae5b7ee6c3e7e6b0fe0640412a37625d1fbfff95c48bbb2dc43964946972"

secret_id = "MyTestDatabaseSecret"
secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
region = "us-east-1"
service = "s3"

# Create the request method
request_method = "GET"

# Create the canonical URI
canonical_uri = f"/test.txt"

# Create the canonical query string
canonical_query_string = ""

# Create the canonical headers
algorithim_header = "aws4_request"
#authorization_header = f"AWS4-HMAC-SHA256 Credential={secret_key}/20130524/{region}/{service}/{algorithim_header},SignedHeaders=accept-encoding;content-type;host;x-amz-content-sha256;x-amz-date;x-amz-target, Signature=<signature>"
#accept_encoding_header = "identity"
#content_type_header = "application/x-amz-json-1.1"
host_header = "examplebucket.s3.amazonaws.com"
x_amz_content_sha256 = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
x_amz_date_header = "20130524T000000Z"
#x_amz_target_header = "secretsmanager.getsecretvalue"
range = "bytes=0-9"

canonical_headers = f"host:{host_header}\nrange:{range}\nx-amz-content-sha256:{x_amz_content_sha256}\nx-amz-date:{x_amz_date_header}\n"

# Create the signed headers
signed_headers = "host;range;x-amz-content-sha256;x-amz-date"

# Create the hashed payload
request_payload = f''
print(request_payload+'\n')
hashed_payload = hashlib.sha256(request_payload.encode("ascii")).hexdigest()
print('hash payload:\n'+hashed_payload+'\n')
# Create the canonical request
canonical_request = f"{request_method}\n{canonical_uri}\n{canonical_query_string}\n{canonical_headers}\n{signed_headers}\n{x_amz_content_sha256}"
print(f"{canonical_request}\n\n")
hashed_canonical_request = hashlib.sha256(canonical_request.encode("ascii")).hexdigest()
#print(canonical_request.lower())
print("CANONICAL REQUEST\n"+hashed_canonical_request+"\n") #OKAY
