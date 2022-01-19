# using python

## app.py

example focused on being minimal

```bash
$ python app.py
Status: True, Message:
Removing /var/log/wtmp.0.gz
Removing /var/log/messages.0.gz
Removing /var/log/interactive-commands.0.gz
Removing /var/log/escript.log.0.gz
Removing /var/log/op-script.log.0.gz
Removing /var/log/snapshot.0.gz
Removing /packages/sets/active/jdocs-ex
setting unlink by default.
setting unlink by default.
Verified junos-arm-32-21.4R1.12 signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Verified deebe signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Verified dsa signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding dsa-arm-32-21.4R1.12 ...
Verified fips-mode signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding fips-mode-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified jail-runtime signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding jail-runtime-arm-32-20211117.16f0122_builder_stable_12 ...
Verified jdocs-ex signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding jdocs-ex-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified jpfe-EX34XX signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding jpfe-EX34XX-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified jphone-home signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding jphone-home-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified jsd-jet-1 signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding jsd-arm-32-21.4R1.12-jet-1 ...
Verified jsdn signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding jsdn-arm-32-21.4R1.12 ...
Verified junos-daemons signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-daemons-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified junos-dp-crypto-support-ex signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-dp-crypto-support-ex-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified junos-libs-ex signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-libs-ex-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified junos-libs signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-libs-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified junos-modules-ex signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-modules-ex-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified junos-modules signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-modules-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified junos-net-dcp-prd signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-net-dcp-prd-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified junos-net-prd signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-net-prd-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified junos-openconfig signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-openconfig-arm-32-21.4R1.12 ...
Verified junos-platform-ex signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-platform-ex-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified junos-probe signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-probe-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified junos-routing-aggregated signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-routing-aggregated-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified junos-runtime-ex signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-runtime-ex-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified junos-runtime signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-runtime-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified jweb-ex signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding jweb-ex-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified na-telemetry signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding na-telemetry-arm-32-21.4R1.12 ...
Verified oam-ve signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Installing OAM volume contents ...
The OAM volume is now installed
Updating OAM boot
Verified os-boot-junos-ve signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Updating /boot junos-boot.tar ...
Updating /boot loader-ve-boot.tar ...
Adding os-boot-junos-ve-arm-32-20211117.16f0122_builder_stable_12 ...
Verified os-crypto signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding os-crypto-arm-32-20211117.16f0122_builder_stable_12 ...
Verified os-kernel-prd signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding os-kernel-prd-arm-32-20211117.16f0122_builder_stable_12 ...
Verified os-libs signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding os-libs-12-arm-32-20211117.16f0122_builder_stable_12 ...
Verified os-runtime signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding os-runtime-arm-32-20211117.16f0122_builder_stable_12 ...
Verified os-zoneinfo signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding os-zoneinfo-20211117.16f0122_builder_stable_12 ...
Verified py-base signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding py-base-arm-32-20211217.124458_builder_junos_214_r1 ...
Verified py-extensions signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding py-extensions-arm-32-20211217.124458_builder_junos_214_r1 ...
NOTICE: 'pending' set will be activated at next reboot...

$
```

## upgrade.py

example with more features

```bash
$ python upgrade.py
Information logged in ./install.log
Connected (version 2.0, client OpenSSH_7.5)
Authentication (publickey) failed.
Authentication (password) successful!
[host office session 0x7f5f02b0a610] Sending:
<?xml version="1.0" encoding="UTF-8"?><nc:hello xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:capabilities><nc:capability>urn:ietf:params:netconf:base:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:base:1.1</nc:capability><nc:capability>urn:ietf:params:netconf:capability:writable-running:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:candidate:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:confirmed-commit:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:rollback-on-error:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:startup:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:url:1.0?scheme=http,ftp,file,https,sftp</nc:capability><nc:capability>urn:ietf:params:netconf:capability:validate:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:xpath:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:notification:1.0</nc:capability><nc:capability>urn:liberouter:params:netconf:capability:power-control:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:interleave:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:with-defaults:1.0</nc:capability></nc:capabilities></nc:hello>]]>]]>
[host office session 0x7f5f02b0a610] Received message from host
[host office session-id 16496] initialized: session-id=16496 | server_capabilities=<dict_keyiterator object at 0x7f5f02a68040>
[host office session-id 16496] Requesting 'ExecuteRpc'
[host office session-id 16496] Sending:
<?xml version="1.0" encoding="UTF-8"?><nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:73e1c5ed-8317-4cc7-8164-68ec9a852c23"><command>show version invoke-on all-routing-engines</command></nc:rpc>]]>]]>
[host office session-id 16496] Received message from host
[host office session-id 16496] Requesting 'ExecuteRpc'
[host office session-id 16496] Sending:
<?xml version="1.0" encoding="UTF-8"?><nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:5585cd9d-e9f7-416e-b17a-0f27a8f3fcc7"><file-show><filename>/usr/share/cevo/cevo_version</filename></file-show></nc:rpc>]]>]]>
[host office session-id 16496] Received message from host
[host office session-id 16496] Requesting 'ExecuteRpc'
[host office session-id 16496] Sending:
<?xml version="1.0" encoding="UTF-8"?><nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:f87bf6bd-2539-4626-97d0-28faed8e1058"><get-interface-information><routing-instance>__juniper_private1__</routing-instance><terse/></get-interface-information></nc:rpc>]]>]]>
[host office session-id 16496] Received message from host
[host office session-id 16496] Requesting 'ExecuteRpc'
[host office session-id 16496] Sending:
<?xml version="1.0" encoding="UTF-8"?><nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:79da88d7-a9cc-4f3f-9636-1ce89d67dc9c"><file-show><filename>/etc/hosts.junos</filename></file-show></nc:rpc>]]>]]>
[host office session-id 16496] Received message from host
[host office session-id 16496] Requesting 'ExecuteRpc'
[host office session-id 16496] Sending:
<?xml version="1.0" encoding="UTF-8"?><nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:aa378e23-c143-4788-ba57-faca0efdf814"><get-route-engine-information/></nc:rpc>]]>]]>
[host office session-id 16496] Received message from host
[host office session-id 16496] Requesting 'ExecuteRpc'
[host office session-id 16496] Sending:
<?xml version="1.0" encoding="UTF-8"?><nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:6ce5293e-fd7a-43e8-9c24-f083f0e09a1e"><get-virtual-chassis-information/></nc:rpc>]]>]]>
[host office session-id 16496] Received message from host
Starting the software upgrade process: junos-arm-32-20.4R3.8.tgz
[host office session-id 16496] Requesting 'ExecuteRpc'
[host office session-id 16496] Sending:
<?xml version="1.0" encoding="UTF-8"?><nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:d0423a45-e144-4c52-88ca-29499440fab5"><request-package-checks-pending-install/></nc:rpc>]]>]]>
[host office session-id 16496] Received message from host
request-package-checks-pending-install rpc is not supported on given device
computing checksum on local package: junos-arm-32-20.4R3.8.tgz
cleaning filesystem ...
[host office session-id 16496] Requesting 'ExecuteRpc'
[host office session-id 16496] Sending:
<?xml version="1.0" encoding="UTF-8"?><nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:ea9d0384-810b-48b6-b161-e9ba976b5735"><request-system-storage-cleanup/></nc:rpc>]]>]]>
[host office session-id 16496] Received message from host
before copy, computing checksum on remote package: /var/tmp/junos-arm-32-20.4R3.8.tgz
[host office session-id 16496] Requesting 'ExecuteRpc'
[host office session-id 16496] Sending:
<?xml version="1.0" encoding="UTF-8"?><nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:03bd3d09-b06c-4682-916d-eb56f5581969"><get-checksum-information><path>/var/tmp/junos-arm-32-20.4R3.8.tgz</path></get-checksum-information></nc:rpc>]]>]]>
[host office session-id 16496] Received message from host
Connected (version 2.0, client OpenSSH_7.5)
Authentication (publickey) failed.
Authentication (password) successful!
b'junos-arm-32-20.4R3.8.tgz': 36388864 / 363733679 (10%)
b'junos-arm-32-20.4R3.8.tgz': 72761344 / 363733679 (20%)
b'junos-arm-32-20.4R3.8.tgz': 109133824 / 363733679 (30%)
b'junos-arm-32-20.4R3.8.tgz': 145506304 / 363733679 (40%)
b'junos-arm-32-20.4R3.8.tgz': 181878784 / 363733679 (50%)
b'junos-arm-32-20.4R3.8.tgz': 218251264 / 363733679 (60%)
b'junos-arm-32-20.4R3.8.tgz': 254623744 / 363733679 (70%)
b'junos-arm-32-20.4R3.8.tgz': 290996224 / 363733679 (80%)
b'junos-arm-32-20.4R3.8.tgz': 327368704 / 363733679 (90%)
b'junos-arm-32-20.4R3.8.tgz': 363733679 / 363733679 (100%)
after copy, computing checksum on remote package: /var/tmp/junos-arm-32-20.4R3.8.tgz
[host office session-id 16496] Requesting 'ExecuteRpc'
[host office session-id 16496] Sending:
<?xml version="1.0" encoding="UTF-8"?><nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:9fbefedc-3524-482e-8e6c-a90ab9045222"><get-checksum-information><path>/var/tmp/junos-arm-32-20.4R3.8.tgz</path></get-checksum-information></nc:rpc>]]>]]>
[host office session-id 16496] Received message from host
checksum check passed.
validating software against current config, please be patient ...
[host office session-id 16496] Requesting 'ExecuteRpc'
[host office session-id 16496] Sending:
<?xml version="1.0" encoding="UTF-8"?><nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:89b05585-3769-4da0-8a93-1e35402a9c95"><request-package-validate><package-name>/var/tmp/junos-arm-32-20.4R3.8.tgz</package-name></request-package-validate></nc:rpc>]]>]]>
[host office session-id 16496] Received message from host
installing software ... please be patient ...
[host office session-id 16496] Requesting 'ExecuteRpc'
[host office session-id 16496] Sending:
<?xml version="1.0" encoding="UTF-8"?><nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:fd26cbb9-d8a1-4297-8a37-a83218c239d3"><request-package-add><no-validate/><package-name>/var/tmp/junos-arm-32-20.4R3.8.tgz</package-name></request-package-add></nc:rpc>]]>]]>
[host office session-id 16496] Received message from host
software pkgadd package-result: 0
Output:
Removing /packages/sets/previous
Removing /var/log/wtmp.1.gz
Removing /var/log/wtmp.0.gz
Removing /var/log/escript.log.0.gz
Removing /var/log/interactive-commands.0.gz
Removing /var/log/messages.0.gz
Removing /var/log/op-script.log.0.gz
Removing /var/log/snapshot.0.gz
Removing /packages/sets/active/optional/jdocs-ex
Removing /packages/sets/active/jdocs-ex
setting unlink by default.
setting unlink by default.
Verified junos-arm-32-20.4R3.8 signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Verified fips-mode signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding fips-mode-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified jail-runtime signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding jail-runtime-arm-32-20210618.f43645e_builder_stable_11-204ab ...
Verified jdocs-ex signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding jdocs-ex-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified jpfe-EX34XX signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding jpfe-EX34XX-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified jphone-home signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding jphone-home-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified jsd-jet-1 signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding jsd-arm-32-20.4R3.8-jet-1 ...
Verified jsdn signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding jsdn-arm-32-20.4R3.8 ...
Verified junos-daemons signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-daemons-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified junos-dp-crypto-support-ex signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-dp-crypto-support-ex-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified junos-libs-ex signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-libs-ex-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified junos-libs signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-libs-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified junos-modules-ex signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-modules-ex-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified junos-modules signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-modules-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified junos-net-dcp-prd signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-net-dcp-prd-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified junos-net-prd signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-net-prd-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified junos-openconfig signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-openconfig-arm-32-20.4R3.8 ...
Verified junos-platform-ex signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-platform-ex-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified junos-probe signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-probe-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified junos-runtime-ex signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-runtime-ex-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified junos-runtime signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding junos-runtime-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified jweb-ex signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding jweb-ex-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified na-telemetry signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding na-telemetry-arm-32-20.4R3.8 ...
Verified oam-ve signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Verified os-boot-junos-ve signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Updating /boot junos-boot.tar ...
Updating /boot loader-ve-boot.tar ...
Adding os-boot-junos-ve-arm-32-20210618.f43645e_builder_stable_11-204ab ...
Verified os-crypto signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding os-crypto-arm-32-20210618.f43645e_builder_stable_11-204ab ...
Verified os-kernel-prd signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding os-kernel-prd-arm-32-20210618.f43645e_builder_stable_11-204ab ...
Verified os-libs signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding os-libs-11-arm-32-20210618.f43645e_builder_stable_11-204ab ...
Verified os-runtime signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding os-runtime-arm-32-20210618.f43645e_builder_stable_11-204ab ...
Verified os-zoneinfo signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding os-zoneinfo-20210618.f43645e_builder_stable_11-204ab ...
Verified py-base signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding py-base-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified py-base2 signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding py-base2-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified py-extensions signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding py-extensions-arm-32-20210907.154329_builder_junos_204_r3 ...
Verified py-extensions2 signed by PackageProductionECP256_2021 method ECDSA256+SHA256
Adding py-extensions2-arm-32-20210907.154329_builder_junos_204_r3 ...
NOTICE: 'pending' set will be activated at next reboot...

Software installation complete. Rebooting
[host office session-id 16496] Requesting 'ExecuteRpc'
[host office session-id 16496] Sending:
<?xml version="1.0" encoding="UTF-8"?><nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:79d76a75-7ed9-46b0-8b5e-594a411f0aaa"><request-reboot><in>0</in></request-reboot></nc:rpc>]]>]]>
[host office session-id 16496] Received message from host
Upgrade pending reboot cycle, please be patient.
Shutdown at Wed Jan 19 14:10:47 2022. [pid 24296]
```
