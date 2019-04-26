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

# DO NOT EDIT! This is a generated sample ("Request",  "job_search_delete_tenant")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-talent

import sys

# [START job_search_delete_tenant]

from google.cloud import talent_v4beta1
import six


def sample_delete_tenant(project_id, tenant_id):
    """Delete Tenant"""
    # [START job_search_delete_tenant_core]

    client = talent_v4beta1.TenantServiceClient()

    # project_id = 'Your Google Cloud Project ID'
    # tenant_id = 'Your Tenant ID)'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    if isinstance(tenant_id, six.binary_type):
        tenant_id = tenant_id.decode('utf-8')
    name = client.tenant_path(project_id, tenant_id)

    client.delete_tenant(name)
    print('Deleted Tenant.')

    # [END job_search_delete_tenant_core]


# [END job_search_delete_tenant]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--project_id',
                        type=str,
                        default='Your Google Cloud Project ID')
    parser.add_argument('--tenant_id', type=str, default='Your Tenant ID)')
    args = parser.parse_args()

    sample_delete_tenant(args.project_id, args.tenant_id)


if __name__ == '__main__':
    main()
