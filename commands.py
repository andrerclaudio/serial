INDEX_REPLY = 0
INDEX_COMMAND = 1
INDEX_DESCRIPTION = 2

INDEX_REPLY_FLAG = 0
INDEX_REPLY_BUFFER = 1

"""
"command_name" : [
                    (reply, [THE, REPLY]),
                    [STX, "PAYLOAD_SIZE", "AA", "BB", etc],
                    "command description,
                 ]

No worries about CRC to send. It will be calculated before being sent.
"""

cmd_action = {

    "init_test": [
        (True, ["02", "03", "01", "01", "01"]),
        ["02", "02", "01", "01"],
        "Make the board enter in Test Mode.",
    ],

    "turn_on_led": [
        (True, ["02", "03", "01", "02", "01"]),
        ["02", "02", "01", "02"],
        "Turn on all available leds on the board.",
    ],

    "turn_off_led": [
        (True, ["02", "03", "01", "03", "01"]),
        ["02", "02", "01", "03"],
        "Turn off all available leds on the board.",
    ],

    "open_relays": [
        (True, ["02", "03", "01", "04", "01"]),
        ["02", "02", "01", "04"],
        "Open all available relays on the board.",
    ],

    "close_relays": [
        (True, ["02", "03", "01", "08", "01"]),
        ["02", "02", "01", "08"],
        "Turn off all available leds on the board.",
    ],

    "start_test_pir": [
        (True, ["02", "03", "01", "05", "01"]),
        ["02", "02", "01", "05"],
        "Set the board to start PIR test.",
    ],

    "start_test_mw": [
        (True, ["02", "03", "01", "06", "01"]),
        ["02", "02", "01", "06"],
        "Set the board to start MW test.",
    ],

    "mask": [
        (True, ["02", "03", "01", "07", "01"]),
        ["02", "02", "01", "07"],
        "Set the board to start Mask test.",
    ],

    "tx_rf_event": [
        (True, ["02", "03", "01", "09", "01"]),
        ["02", "03", "01", "09"],  # Fill with the Qty. of packets to transmit
        "Transmit N packets to the air.",
    ],

    "current_start": [
        (True, ["02", "03", "01", "0A", "01"]),
        ["02", "02", "01", "0A"],
        "Turn off all available leds on the board.",
    ],

    "current_finish": [
        (True, ["02", "03", "01", "0B", "01"]),
        ["02", "02", "01", "0B"],
        "Turn off all available leds on the board.",
    ],

    "reset_device": [
        (True, ["02", "03", "01", "0C", "01"]),
        ["02", "02", "01", "0C"],
        "Turn off all available leds on the board.",
    ],

    "finish_test": [
        (True, ["02", "03", "01", "FE", "01"]),
        ["02", "02", "01", "FE"],
        "Turn off all available leds on the board.",
    ],

}

cmd_question = {

    "product_model": [
        (True, []),
        ["02", "02", "02", "09"],
        "Fetch the board model we are dealing with.",
    ],

    "version": [
        (True, []),
        ["02", "02", "02", "07"],
        "Fetch the software version.",
    ],

    "pyr_steady": [
        (True, []),
        ["02", "02", "02", "01"],
        "Ask whether the sensor is ready to work or not.",
    ],

    "trigger_pyr": [
        (True, []),
        ["02", "02", "02", "02"],
        "Pyr event happened.",
    ],

    "trigger_mw": [
        (True, []),
        ["02", "02", "02", "03"],
        "Microwave event happened.",
    ],

    "defaults": [
        (True, []),
        ["02", "02", "02", "04"],
        "Check if all the devices adjusts are in default.",
    ],

    "mask": [
        (True, []),
        ["02", "02", "02", "05"],
        "Check whether the mask sensor is working or not.",
    ],

    "light": [
        (True, []),
        ["02", "02", "02", "06"],
        "Check whether the light sensor is working or not.",
    ],

    "rf_id": [
        (True, []),
        ["02", "02", "02", "08"],
        "Fetch the RF ID.",
    ],

    "tamper": [
        (True, []),
        ["02", "02", "02", "0A"],
        "Check whether the button Tamper is open or close.",
    ],
}

cmd_information = {

    "temperature": [
        (True, []),
        ["02", "03", "03", "01"],  # Fill with the Temperature to transmit
        "Fetch the board model we are dealing with.",
    ],
}
