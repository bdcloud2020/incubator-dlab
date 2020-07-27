#!/usr/bin/python
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

import requests
import sys
import time
import urllib.parse

time.sleep(30)  # wait for new code to be analyzed by SonarQube

PROJECT_KEY = urllib.parse.quote(sys.argv[1])
print(PROJECT_KEY)
TOKEN = sys.argv[2]


def get_sonarqube_status():
    response = requests.get('http://localhost:9000/sonar/api/qualitygates/project_status?projectKey=' + PROJECT_KEY,
                            auth=(TOKEN, '')).json()
    return response['projectStatus']['status']


print(get_sonarqube_status())
