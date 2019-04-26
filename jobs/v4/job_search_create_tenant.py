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

# DO NOT EDIT! This is a generated sample ("Request",  "job_search_create_tenant")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-talent

import sys

# [START job_search_create_tenant]

from google.cloud import talent_v4beta1
import six


def sample_create_tenant(project_id, external_id):
    """Create Tenant for scoping resources, e.g. companies and jobs"""
    # [START job_search_create_tenant_core]

    client = talent_v4beta1.TenantServiceClient()

    # project_id = 'Your Google Cloud Project ID'
    # external_id = 'Your Unique Identifier for Tenant'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    if isinstance(external_id, six.binary_type):
        external_id = external_id.decode('utf-8')
    parent = client.project_path(project_id)
    tenant = {'external_id': external_id}

    response = client.create_tenant(parent, tenant)
    print('Created Tenant')
    print('Name: {}'.format(response.name))
    print('External ID: {}'.format(response.external_id))

    # [END job_search_create_tenant_core]


# [END job_search_create_tenant]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--project_id',
                        type=str,
                        default='Your Google Cloud Project ID')
    parser.add_argument('--external_id',
                        type=str,
                        default='Your Unique Identifier for Tenant')
    args = parser.parse_args()

    sample_create_tenant(args.project_id, args.external_id)


if __name__ == '__main__':
    main()
