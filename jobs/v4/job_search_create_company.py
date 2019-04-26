# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT EDIT! This is a generated sample ("Request",  "job_search_create_company")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-talent

import sys

# [START job_search_create_company]

from google.cloud import talent_v4beta1
import six


def sample_create_company(project_id, tenant_id, display_name, external_id):
    """Create Company"""
    # [START job_search_create_company_core]

    client = talent_v4beta1.CompanyServiceClient()

    # project_id = 'Your Google Cloud Project ID'
    # tenant_id = 'Your Tenant ID (using tenancy is optional)'
    # display_name = 'My Company Name'
    # external_id = 'Identifier of this company in my system'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    if isinstance(tenant_id, six.binary_type):
        tenant_id = tenant_id.decode('utf-8')
    if isinstance(display_name, six.binary_type):
        display_name = display_name.decode('utf-8')
    if isinstance(external_id, six.binary_type):
        external_id = external_id.decode('utf-8')
    parent = client.tenant_path(project_id, tenant_id)
    company = {'display_name': display_name, 'external_id': external_id}

    response = client.create_company(parent, company)
    print('Created Company')
    print('Name: {}'.format(response.name))
    print('Display Name: {}'.format(response.display_name))
    print('External ID: {}'.format(response.external_id))

    # [END job_search_create_company_core]


# [END job_search_create_company]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--project_id',
                        type=str,
                        default='Your Google Cloud Project ID')
    parser.add_argument('--tenant_id',
                        type=str,
                        default='Your Tenant ID (using tenancy is optional)')
    parser.add_argument('--display_name', type=str, default='My Company Name')
    parser.add_argument('--external_id',
                        type=str,
                        default='Identifier of this company in my system')
    args = parser.parse_args()

    sample_create_company(args.project_id, args.tenant_id, args.display_name,
                          args.external_id)


if __name__ == '__main__':
    main()
