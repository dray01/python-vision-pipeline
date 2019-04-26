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

# DO NOT EDIT! This is a generated sample ("RequestPagedAll",  "job_search_list_jobs")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-talent

import sys

# [START job_search_list_jobs]

from google.cloud import talent_v4beta1
import six


def sample_list_jobs(project_id, tenant_id, filter_):
    """List Jobs"""
    # [START job_search_list_jobs_core]

    client = talent_v4beta1.JobServiceClient()

    # project_id = 'Your Google Cloud Project ID'
    # tenant_id = 'Your Tenant ID (using tenancy is optional)'
    # filter_ = 'companyName=projects/my-project/companies/company-id'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    if isinstance(tenant_id, six.binary_type):
        tenant_id = tenant_id.decode('utf-8')
    if isinstance(filter_, six.binary_type):
        filter_ = filter_.decode('utf-8')
    parent = client.tenant_path(project_id, tenant_id)

    # Iterate over all results
    for response_item in client.list_jobs(parent, filter_):
        print('Job name: {}'.format(response_item.name))
        print('Job requisition ID: {}'.format(response_item.requisition_id))
        print('Job title: {}'.format(response_item.title))
        print('Job description: {}'.format(response_item.description))

    # [END job_search_list_jobs_core]


# [END job_search_list_jobs]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--project_id',
                        type=str,
                        default='Your Google Cloud Project ID')
    parser.add_argument('--tenant_id',
                        type=str,
                        default='Your Tenant ID (using tenancy is optional)')
    parser.add_argument(
        '--filter',
        type=str,
        default='companyName=projects/my-project/companies/company-id')
    args = parser.parse_args()

    sample_list_jobs(args.project_id, args.tenant_id, args.filter)


if __name__ == '__main__':
    main()
