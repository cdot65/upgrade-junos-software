from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

pkg = "junos-arm-32-21.4R1.12.tgz"

with Device(host="switch1", user="python", passwd="juniper123") as dev:
    sw = SW(dev)

    ok, msg = sw.install(package=pkg, validate=True, checksum_algorithm="sha256")
    print("Status: " + str(ok) + ", Message: " + msg)
    if ok:
        sw.reboot()
