import os, sys, logging
from jnpr.junos import Device
from jnpr.junos.utils.sw import SW
from jnpr.junos.exception import ConnectError

host = "192.168.104.168"
package = "junos-arm-32-21.4R1.12.tgz"
remote_path = "/var/tmp"
validate = True
logfile = "./install.log"


def update_progress(dev, report):
    # log the progress of the installing process
    logging.info(report)


def main():
    # initialize logging
    logging.basicConfig(
        filename=logfile, level=logging.INFO, format="%(asctime)s:%(name)s: %(message)s"
    )
    logging.getLogger().name = host
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.info("Information logged in {0}".format(logfile))

    # verify package exists
    if not (os.path.isfile(package)):
        msg = "Software package does not exist: {0}. ".format(package)
        logging.error(msg)
        sys.exit()

    # open a connection with the device and start a NETCONF session
    dev = Device(host=host, user="python", passwd="juniper123")
    try:
        dev.open()
    except ConnectError as err:
        logging.error("Cannot connect to device: {0}\n".format(err))
        return

    # Create an instance of SW
    sw = SW(dev)

    try:
        logging.info("Starting the software upgrade process: {0}".format(package))

        # Starting in Release 2.5.0, install() returns a tuple instead of a Boolean
        ok, msg = sw.install(
            package=package,
            cleanfs=True,
            remote_path=remote_path,
            progress=update_progress,
            validate=validate,
        )
    except Exception as err:
        msg = "Unable to install software, {0}".format(err)
        logging.error(msg)
        ok = False

    if ok is True:
        logging.info("Software installation complete. Rebooting")
        rsp = sw.reboot()
        logging.info("Upgrade pending reboot cycle, please be patient.")
        logging.info(rsp)
    else:
        msg = "Unable to install software, {0}".format(ok)
        logging.error(msg)


if __name__ == "__main__":
    main()
