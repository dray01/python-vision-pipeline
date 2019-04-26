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

# DO NOT EDIT! This is a generated sample ("Request",  "job_search_autocomplete_job_title")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-talent

import sys

# [START job_search_autocomplete_job_title]

from google.cloud import talent_v4beta1
from google.cloud.talent_v4beta1 import enums
import six


def sample_complete_query(project_id, tenant_id, query, num_results,
                          language_code):
    """Complete job title given partial text (autocomplete)"""
    # [START job_search_autocomplete_job_title_core]

    client = talent_v4beta1.CompletionClient()

    # project_id = 'Your Google Cloud Project ID'
    # tenant_id = 'Your Tenant ID (using tenancy is optional)'
    # query = '[partially typed job title]'
    # num_results = 5
    # language_code = 'en-US'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    if isinstance(tenant_id, six.binary_type):
        tenant_id = tenant_id.decode('utf-8')
    if isinstance(query, six.binary_type):
        query = query.decode('utf-8')

    if isinstance(language_code, six.binary_type):
        language_code = language_code.decode('utf-8')
    parent = client.tenant_path(project_id, tenant_id)
    language_codes = [language_code]

    response = client.complete_query(parent,
                                     query,
                                     num_results,
                                     language_codes=language_codes)
    for result in response.completion_results:
        print('Suggested title: {}'.format(result.suggestion))
        # Suggestion type is JOB_TITLE or COMPANY_TITLE
        print('Suggestion type: {}'.format(
            enums.CompleteQueryRequest.CompletionType(result.type).name))

    # [END job_search_autocomplete_job_title_core]


# [END job_search_autocomplete_job_title]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--project_id',
                        type=str,
                        default='Your Google Cloud Project ID')
    parser.add_argument('--tenant_id',
                        type=str,
                        default='Your Tenant ID (using tenancy is optional)')
    parser.add_argument('--query',
                        type=str,
                        default='[partially typed job title]')
    parser.add_argument('--num_results', type=int, default=5)
    parser.add_argument('--language_code', type=str, default='en-US')
    args = parser.parse_args()

    sample_complete_query(args.project_id, args.tenant_id, args.query,
                          args.num_results, args.language_code)


if __name__ == '__main__':
    main()
