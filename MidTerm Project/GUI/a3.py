# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.14.0)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xfd\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x1e\x00\x00\x00\x1e\x08\x06\x00\x00\x00\x3b\x30\xae\xa2\
\x00\x00\x00\x06\x62\x4b\x47\x44\x00\xff\x00\xff\x00\xff\xa0\xbd\
\xa7\x93\x00\x00\x00\xb2\x49\x44\x41\x54\x48\x89\xed\x96\x31\x0e\
\xc2\x30\x0c\x45\x1f\xbd\x03\x88\x5e\x85\x95\x85\x72\x6c\x46\x0a\
\x0b\x0c\xec\x0d\x13\x67\x40\x2a\x03\x8d\x84\xda\xaa\xa4\x4e\x62\
\x24\xe4\x2f\x79\x88\x95\xfc\x67\x45\x71\x12\x30\xfd\x48\x7b\xc0\
\x01\xad\x30\x1c\x50\x49\xc0\x31\x50\x1f\x4d\x08\x68\xd1\x1b\xb7\
\x92\x6a\x03\x7c\x07\x2a\x12\x81\x66\xcb\xc0\x7f\x05\x3e\x00\x27\
\x60\x35\x35\x29\xb6\x95\x7c\x7c\xea\xd8\xe5\xae\x53\xf0\x1c\xe0\
\x25\x70\xe9\xf2\x37\xa0\xd4\x02\x07\xc1\x43\x4c\x37\x63\x15\xcf\
\xf4\xa9\x25\x87\x2b\xcb\x81\xd4\xda\xea\xb5\x06\xf8\x2b\x34\x17\
\xb8\x66\xa4\x9d\x34\x2e\x90\x27\x70\x06\xb6\xc0\xc3\x27\xed\x59\
\x34\xb0\x1a\xf8\x9e\xc0\xd3\x49\x16\x55\xbc\x7f\x89\xd2\xfe\x6d\
\x80\x5d\x64\xe1\xa6\xb4\x7a\x01\x9d\x34\xc9\x08\x48\x16\x77\x60\
\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82\
"

qt_resource_name = b"\
\x00\x02\
\x00\x00\x06\x43\
\x00\x61\
\x00\x33\
\x00\x12\
\x0d\xf3\x22\x27\
\x00\x69\
\x00\x63\x00\x6f\x00\x6e\x00\x73\x00\x38\x00\x2d\x00\x65\x00\x78\x00\x69\x00\x74\x00\x2d\x00\x33\x00\x30\x00\x2e\x00\x70\x00\x6e\
\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x7c\x92\x0e\x17\x27\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()