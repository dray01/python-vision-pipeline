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

# DO NOT EDIT! This is a generated sample ("RequestPagedAll",  "job_search_list_tenants")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-talent

import sys

# [START job_search_list_tenants]

from google.cloud import talent_v4beta1
import six


def sample_list_tenants(project_id):
    """List Tenants"""
    # [START job_search_list_tenants_core]

    client = talent_v4beta1.TenantServiceClient()

    # project_id = 'Your Google Cloud Project ID'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    parent = client.project_path(project_id)

    # Iterate over all results
    for response_item in client.list_tenants(parent):
        print('Tenant Name: {}'.format(response_item.name))
        print('External ID: {}'.format(response_item.external_id))

    # [END job_search_list_tenants_core]


# [END job_search_list_tenants]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--project_id',
                        type=str,
                        default='Your Google Cloud Project ID')
    args = parser.parse_args()

    sample_list_tenants(args.project_id)


if __name__ == '__main__':
    main()
