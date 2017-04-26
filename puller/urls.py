"""puller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('scraper.urls')),
]


{u'status': u'RUNNING', u'cpuPlatform': u'Intel Ivy Bridge', u'kind': u'compute#instance', u'machineType': u'https://www.googleapis.com/compute/v1/projects/mbexam-2017/zones/asia-east1-c/machineTypes/n1-standard-1', u'description': u'', u'zone': u'https://www.googleapis.com/compute/v1/projects/mbexam-2017/zones/asia-east1-c', u'tags': {u'fingerprint': u'42WmSpB8rSM='}, u'disks': [{u'index': 0, u'kind': u'compute#attachedDisk', u'autoDelete': False, u'deviceName': u'exam-instance-1-dashboard', u'boot': True, u'source': u'https://www.googleapis.com/compute/v1/projects/mbexam-2017/zones/asia-east1-c/disks/exam-instance-1-dashboard', u'interface': u'SCSI', u'mode': u'READ_WRITE', u'licenses': [u'https://www.googleapis.com/compute/v1/projects/debian-cloud/global/licenses/debian-8-jessie'], u'type': u'PERSISTENT'}], u'metadata': {u'kind': u'compute#metadata', u'fingerprint': u'mhb7iQcxNxI='}, u'scheduling': {u'automaticRestart': True, u'preemptible': False, u'onHostMaintenance': u'MIGRATE'}, u'canIpForward': False, u'serviceAccounts': [{u'scopes': [u'https://www.googleapis.com/auth/devstorage.read_only', u'https://www.googleapis.com/auth/logging.write', u'https://www.googleapis.com/auth/monitoring.write', u'https://www.googleapis.com/auth/servicecontrol', u'https://www.googleapis.com/auth/service.management.readonly', u'https://www.googleapis.com/auth/trace.append'], u'email': u'813772737879-compute@developer.gserviceaccount.com'}], u'networkInterfaces': [{u'kind': u'compute#networkInterface', u'network': u'https://www.googleapis.com/compute/v1/projects/mbexam-2017/global/networks/default', u'accessConfigs': [{u'kind': u'compute#accessConfig', u'type': u'ONE_TO_ONE_NAT', u'name': u'External NAT', u'natIP': u'130.211.248.91'}], u'networkIP': u'10.140.0.2', u'subnetwork': u'https://www.googleapis.com/compute/v1/projects/mbexam-2017/regions/asia-east1/subnetworks/default', u'name': u'nic0'}], u'creationTimestamp': u'2017-04-22T23:54:19.125-07:00', u'id': u'1530374863604281717', u'selfLink': u'https://www.googleapis.com/compute/v1/projects/mbexam-2017/zones/asia-east1-c/instances/exam-instance-1-dashboard', u'name': u'exam-instance-1-dashboard'}
