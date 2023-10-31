# build-in libraries
import logging
import time

from commands import cmd_action, INDEX_COMMAND, INDEX_REPLY, INDEX_REPLY_FLAG, cmd_question
# Project libraries
from ftdi import UartFTDI
from options import user_options
from products import devices

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def application():
    """
    The main idea is to send commands thought the Uart
    and ant them controls a board connected to it.

    :return: None
    """

    wait_device = ""
    wait_device = wait_device + "\n"
    wait_device = wait_device + "------------------------ Product Serial Communication ------------------------"
    wait_device = wait_device + "\n"
    wait_device = wait_device + "\n"

    print(wait_device)

    # Serial FTDI class init
    ftdi = UartFTDI()

    if ftdi.ser:

        app_running = True

        while app_running:

            cmd = cmd_action['init_test'][INDEX_COMMAND]
            ret = ftdi.send(cmd, reply=cmd_action['init_test'][INDEX_REPLY][INDEX_REPLY_FLAG])

            if ret:

                cmd = cmd_question['product_model'][INDEX_COMMAND]
                model = ftdi.send(cmd, reply=cmd_question['product_model'][INDEX_REPLY][INDEX_REPLY_FLAG])

                cmd = cmd_question['version'][INDEX_COMMAND]
                version = ftdi.send(cmd, reply=cmd_question['version'][INDEX_REPLY][INDEX_REPLY_FLAG])

                if model and version:

                    model_string = ''
                    for val in model[-3:-1]:
                        model_string = model_string + str(val).upper()

                    version_string = ''
                    for val in version[-4:-1]:
                        version_string = version_string + str(val).upper()

                    version_string = '.'.join(version_string[i:i + 2] for i in range(0, len(version_string), 2))
                    model_string = devices[model_string]
                    device = '\n\n\n\n'
                    device = device + '------------------------------------------------------------------------------\n'
                    device = device + f"            * Connected device:     {model_string}"
                    device = device + '\n'
                    device = device + f"            * Version:              {version_string}"
                    print(device)

                    while app_running:
                        if not user_options(ftdi):
                            app_running = False

                else:
                    print("     Something went wrong fetching model/version. Trying again!!")
                    time.sleep(1)

            else:
                print("     Waiting the device to connect!")
                time.sleep(1)


if __name__ == '__main__':
    # The application start from here.
    application()
