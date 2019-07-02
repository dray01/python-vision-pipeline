#!/bin/python
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.rom googleapiclient import discovery

"""Use a service account and GCP metadata service to access an
   IAP-protected resource"""


def build_claim(client_id, service_account):
    """Creates the necessary claim to request access to an IAP-protected URL

    Args:
        client_id: the OAuth client ID. Available from API/Credentials console
        service_account: the service account email

    Returns:
        The claim
    """
    import time

    oauth_endpoint = 'https://www.googleapis.com/oauth2/v4/token'
    now = int(time.time())

    claim = {
        'iss': service_account,
        'target_audience': client_id,
        'iat': now,
        'exp': now + 3600,
        'aud': oauth_endpoint
    }

    return claim


def create_assertion(claim):
    """Creates an assertion - a signed claim of authorization

    Args:
        claim: the claim to send to the OAuth2 service

    Returns:
        The assertion
    """

    def encode_dict(dictionary):
        """Encodes a dictionary to the form needed for a JWT

        Args:
            dictionary: the dictionary to encode

        Returns:
            the encoded dictionary (bytes)
        """
        import base64
        import json

        json_dict_string = json.dumps(dictionary)
        json_dict_bytes = json_dict_string.encode()

        encoded_bytes = base64.urlsafe_b64encode(json_dict_bytes)
        encoded_bytes = encoded_bytes.replace(b'=', b'')

        return encoded_bytes

    def signByteString(byteString, service_account):
        """Signs a byte string by the specified service account

        Args:
            byteString: the bytes to sign
            service_account: the email of the service account that will sign

        Returns:
            the signature (bytes)
        """
        import base64

        from googleapiclient import discovery
        from oauth2client.client import GoogleCredentials

        credentials = GoogleCredentials.get_application_default()
        service = discovery.build('iam', 'v1', credentials=credentials)

        name = 'projects/-/serviceAccounts/{}'.format(service_account)
        request = service.projects().serviceAccounts().signBlob(
            name=name,
            body={
                'bytesToSign': base64.urlsafe_b64encode(byteString).decode()
            }
        )
        response = request.execute()
        signature = response['signature']
        
        signature = signature.replace('+', '-').replace('/', '_')
        signature = signature.replace('=', '')
        signature = signature.encode()

        return signature

    header = {"alg":"RS256","typ":"JWT"}
    to_sign = encode_dict(header) + b'.' + encode_dict(claim)
    service_account = claim['iss']
    signature = signByteString(to_sign, service_account)

    assertion = to_sign + b'.' + signature
    return assertion


def get_id_token(assertion):
    """Gets an OpenID Connect token for the given private key

    Args:
        claim: the claim to send to the OAuth2 service
        private_key: the service account's private key (in PEM format)

    Returns:
        An OpenID connect token to authenticate requests from the service acct
    """
    import json
    import requests

    oauth_endpoint = 'https://www.googleapis.com/oauth2/v4/token'
    grant_type = 'urn:ietf:params:oauth:grant-type:jwt-bearer'

    response = requests.post(
        oauth_endpoint,
        data = {
            'grant_type': grant_type,
            'assertion': assertion
        }
    )

    id_token = response.json()['id_token']
    return id_token


def request(client_id, service_account, method, url, **kwargs):
    """Acts like requests.request, but includes IAP required authentication

    Args:
        client_id: the OAuth client ID. Available from API/Credentials console
        service_account: the service account email

        Remaining arguments are passed through to requests.request
            method: the HTTP method
            url: the address to access
            kwargs: other arguments to pass to requests.request

    Returns:
        The requests Response object from the request
    """
    import requests

    claim = build_claim(client_id, service_account)
    assertion = create_assertion(claim)
    id_token = get_id_token(assertion)

    if 'headers' not in kwargs:
        kwargs['headers'] = {}
    kwargs['headers']['Authorization'] = 'Bearer {}'.format(id_token)

    return requests.request(method, url, **kwargs)


def main():
    """Make a GET request to the IAP-protected URL using service account key
    """

    import argparse

    parser = argparse.ArgumentParser(
        description='Call IAP protected resource with service account'
    )
    parser.add_argument('client_id', help="The protected site's client ID")
    parser.add_argument('service_account', help="The service account's email")
    parser.add_argument('url', help="URL to access")
    args = parser.parse_args()

    response = request(
        args.client_id, args.service_account, 'GET', args.url
    )

    print('Status code: {} {}'.format(response.status_code, response.reason))
    print('Headers:')
    for key in response.headers:
        print('    {}: {}'.format(key, response.headers[key]))
    print('Body:')
    print(response.text)


if __name__ == '__main__':
    main()
