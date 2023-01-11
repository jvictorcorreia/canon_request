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
request_method = "POST"

# Create the canonical URI
canonical_uri = f"/GetSecretValue"

# Create the canonical query string
canonical_query_string = ""

# Create the canonical headers
algorithim_header = "aws4_request"
authorization_header = f"AWS4-HMAC-SHA256 Credential={secret_key}/20130524/{region}/{service}/{algorithim_header},SignedHeaders=accept-encoding;content-type;host;x-amz-content-sha256;x-amz-date;x-amz-target, Signature=<signature>"
accept_encoding_header = "identity"
content_type_header = "application/x-amz-json-1.1"
host_header = "secretsmanager.sa-east-1.amazonaws.com"
x_amz_content_sha256 = "beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3"
x_amz_date_header = "20230111T145646Z"
x_amz_target_header = "secretsmanager.getsecretvalue"
range = "bytes=0-9"

canonical_headers = f"accept-encoding:{accept_encoding_header}\ncontent-type:{content_type_header}\nhost:{host_header}\nx-amz-content-sha256:beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3\nx-amz-date:{x_amz_date_header}\nx-amz-target:{x_amz_target_header}\n"

# Create the signed headers
signed_headers = "accept-encoding;content-type;host;x-amz-content-sha256;x-amz-date;x-amz-target"

# Create the hashed payload
request_payload = '{\n  "SecretId": "'+ secret_id +'",\n}'
print(request_payload+'\n')
hashed_payload = hashlib.sha256(request_payload.encode("ascii")).hexdigest()
print('hash payload:\n'+hashed_payload+'\n')
# Create the canonical request
canonical_request = f"{request_method}\n{canonical_uri}\n{canonical_query_string}\n{canonical_headers}\n{signed_headers}\nbeaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3"
print(f"{canonical_request}\n\n")
hashed_canonical_request = hashlib.sha256(canonical_request.encode("ascii")).hexdigest()
#print(canonical_request.lower())
print("CANONICAL REQUEST\n"+hashed_canonical_request+"\n") #OKAY

