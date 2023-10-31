# build-in libraries
import time

# Project libraries
from commands import cmd_action, INDEX_COMMAND, INDEX_REPLY, INDEX_REPLY_FLAG, cmd_question, cmd_information
from tools import int_to_hex

ACK = '01'
NACK = '02'
QTY_PACKETS = '03'


def user_options(ser):
    """
    Show and wait for users selection.
    :param ser: Serial hardware object.
    :return:
    """

    opt = ''
    opt = opt + '\n\n'
    opt = opt + f'      1- Turn ON Leds        10- Is the Sensor steady?\n'
    opt = opt + f'      2- Turn OFF Leds       11- Was the PIR triggered?\n'
    opt = opt + f'      3- Open Relays         12- Was the MW triggered?\n'
    opt = opt + f'      4- Close Relays        13- All settings (switches and others) are default?\n'
    opt = opt + f'      5- Start PIR test      14- Is Masking Ok?\n'
    opt = opt + f'      6- Start MW test       15- Are the light sensors Ok?\n'
    opt = opt + f'      7- Start MASK test     16- Fetch RF ID numbers\n'
    opt = opt + f'      8- Send RF packet      17- Is tamper button closed?\n'
    opt = opt + f'      9- Finish test         18- Send the Temperature\n'
    opt = opt + '\n'
    opt = opt + f'      0- EXIT'
    opt = opt + '\n'
    opt = opt + f"      Enter with the option [number] above and press ENTER"
    ret = input(opt + f':  ')

    if ret in ['1', '2', '3', '4', '5', '6', '7',
               '8', '9', '10', '11', '12', '13',
               '14', '15', '16', '17', '18', '0']:

        if ret == '1':
            cmd = cmd_action['turn_on_led'][INDEX_COMMAND]
            ret = ser.send(cmd, reply=cmd_action['turn_on_led'][INDEX_REPLY][INDEX_REPLY_FLAG])
            if ret:
                ret = ret[:-1]
                ret = ret[-1:].pop()
                if str(ret) == ACK:
                    print('      --- Success on TURNING ON the Leds!')
                else:
                    print('      Something went wrong!')
            else:
                print('      Something went wrong!')

        elif ret == '2':
            cmd = cmd_action['turn_off_led'][INDEX_COMMAND]
            ret = ser.send(cmd, reply=cmd_action['turn_off_led'][INDEX_REPLY][INDEX_REPLY_FLAG])
            if ret:
                ret = ret[:-1]
                ret = ret[-1:].pop()
                if str(ret) == ACK:
                    print('      --- Success on TURNING OFF the Leds!')
                else:
                    print('      Something went wrong!')
            else:
                print('      Something went wrong!')

        elif ret == '3':
            cmd = cmd_action['open_relays'][INDEX_COMMAND]
            ret = ser.send(cmd, reply=cmd_action['open_relays'][INDEX_REPLY][INDEX_REPLY_FLAG])
            if ret:
                ret = ret[:-1]
                ret = ret[-1:].pop()
                if str(ret) == ACK:
                    print('      --- Success on OPENING the relays!')
                else:
                    print('      Something went wrong!')
            else:
                print('      Something went wrong!')

        elif ret == '4':
            cmd = cmd_action['close_relays'][INDEX_COMMAND]
            ret = ser.send(cmd, reply=cmd_action['close_relays'][INDEX_REPLY][INDEX_REPLY_FLAG])
            if ret:
                ret = ret[:-1]
                ret = ret[-1:].pop()
                if str(ret) == ACK:
                    print('      --- Success on CLOSING the relays!')
                else:
                    print('      Something went wrong!')
            else:
                print('      Something went wrong!')

        elif ret == '5':
            cmd = cmd_action['start_test_pir'][INDEX_COMMAND]
            ret = ser.send(cmd, reply=cmd_action['start_test_pir'][INDEX_REPLY][INDEX_REPLY_FLAG])
            if ret:
                ret = ret[:-1]
                ret = ret[-1:].pop()
                if str(ret) == ACK:
                    print('      --- PIR teste is awaited!')
                else:
                    print('      Something went wrong!')
            else:
                print('      Something went wrong!')

        elif ret == '6':
            cmd = cmd_action['start_test_mw'][INDEX_COMMAND]
            ret = ser.send(cmd, reply=cmd_action['start_test_mw'][INDEX_REPLY][INDEX_REPLY_FLAG])
            if ret:
                ret = ret[:-1]
                ret = ret[-1:].pop()
                if str(ret) == ACK:
                    print('      --- MW test is awaited!')
                else:
                    print('      Something went wrong!')
            else:
                print('      Something went wrong!')

        elif ret == '7':
            cmd = cmd_action['mask'][INDEX_COMMAND]
            ret = ser.send(cmd, reply=cmd_action['mask'][INDEX_REPLY][INDEX_REPLY_FLAG])
            if ret:
                ret = ret[:-1]
                ret = ret[-1:].pop()
                if str(ret) == ACK:
                    print('      --- Mask test is awaited!')
                else:
                    print('      Something went wrong!')
            else:
                print('      Something went wrong!')

        elif ret == '8':
            qty_packets = str(int_to_hex(int(QTY_PACKETS)))
            cmd = list(cmd_action['tx_rf_event'][INDEX_COMMAND])
            cmd.append(qty_packets)
            ret = ser.send(cmd, reply=cmd_action['tx_rf_event'][INDEX_REPLY][INDEX_REPLY_FLAG])
            if ret:
                ret = ret[:-1]
                ret = ret[-1:].pop()
                if str(ret) == ACK:
                    print(f'     --- Transmitted {QTY_PACKETS}!')
                else:
                    print('      Something went wrong!')
            else:
                print('      Something went wrong!')

        elif ret == '9':
            cmd = cmd_action['finish_test'][INDEX_COMMAND]
            ret = ser.send(cmd, reply=cmd_action['finish_test'][INDEX_REPLY][INDEX_REPLY_FLAG])
            if ret:
                ret = ret[:-1]
                ret = ret[-1:].pop()
                if str(ret) == ACK:
                    print('      --- The test was finished!')
                    print('      Closing the uart!')
                    time.sleep(2)
                    return False
                else:
                    print('      Something went wrong!')
            else:
                print('      Something went wrong!')

        elif ret == '10':

            opt = ''
            opt = opt + '\n\n'
            opt = opt + f'      It will loop 10 times or stop when the answer is ACK\n'
            print(opt)

            for attempts in range(0, 10):
                cmd = cmd_question['pyr_steady'][INDEX_COMMAND]
                ret = ser.send(cmd, reply=cmd_question['pyr_steady'][INDEX_REPLY][INDEX_REPLY_FLAG])
                if ret:
                    ret = ret[:-1]
                    ret = ret[-1:].pop()
                    if str(ret) == ACK:
                        print('\n      *** The PYR is ready to work! ***')
                        break
                    elif str(ret) == NACK:
                        time.sleep(1)
                        print('      --- The PYR is NOT ready yet!')
                    else:
                        print('      Something went wrong!')
                else:
                    print('      Something went wrong!')

        elif ret == '11':

            opt = ''
            opt = opt + '\n\n'
            opt = opt + f'      It will loop 10 times or stop when the answer is ACK\n'
            print(opt)

            for attempts in range(0, 10):
                cmd = cmd_question['trigger_pyr'][INDEX_COMMAND]
                ret = ser.send(cmd, reply=cmd_question['trigger_pyr'][INDEX_REPLY][INDEX_REPLY_FLAG])
                if ret:
                    ret = ret[:-1]
                    ret = ret[-1:].pop()
                    if str(ret) == ACK:
                        print('\n      *** A PYR event occurred! ***')
                        break
                    elif str(ret) == NACK:
                        time.sleep(1)
                        print('      --- NO PYR event happened!')
                    else:
                        print('      Something went wrong!')
                else:
                    print('      Something went wrong!')

        elif ret == '12':

            opt = ''
            opt = opt + '\n\n'
            opt = opt + f'      It will loop 10 times or stop when the answer is ACK\n'
            print(opt)

            for attempts in range(0, 10):
                cmd = cmd_question['trigger_mw'][INDEX_COMMAND]
                ret = ser.send(cmd, reply=cmd_question['trigger_mw'][INDEX_REPLY][INDEX_REPLY_FLAG])
                if ret:
                    ret = ret[:-1]
                    ret = ret[-1:].pop()
                    if str(ret) == ACK:
                        print('\n      *** A MW event occurred! ***')
                        break
                    elif str(ret) == NACK:
                        time.sleep(1)
                        print('      --- NO MW event happened!')
                    else:
                        print('      Something went wrong!')
                else:
                    print('      Something went wrong!')

        elif ret == '13':

            cmd = cmd_question['defaults'][INDEX_COMMAND]
            ret = ser.send(cmd, reply=cmd_question['defaults'][INDEX_REPLY][INDEX_REPLY_FLAG])
            if ret:
                ret = ret[:-1]
                ret = ret[-1:].pop()
                if str(ret) == ACK:
                    print('\n      *** All default adjusts are OK ***')
                elif str(ret) == NACK:
                    print('      --- The defaults are NOT ok!')
                else:
                    print('      Something went wrong!')
            else:
                print('      Something went wrong!')

        elif ret == '14':

            opt = ''
            opt = opt + '\n\n'
            opt = opt + f'      It will loop 10 times or stop when the answer is ACK\n'
            print(opt)

            for attempts in range(0, 10):
                cmd = cmd_question['mask'][INDEX_COMMAND]
                ret = ser.send(cmd, reply=cmd_question['mask'][INDEX_REPLY][INDEX_REPLY_FLAG])
                if ret:
                    ret = ret[:-1]
                    ret = ret[-1:].pop()
                    if str(ret) == ACK:
                        print('\n      *** The Mask sensor IS working! ***')
                        break
                    elif str(ret) == NACK:
                        time.sleep(1)
                        print('      --- NO Maks event happened!')
                    else:
                        print('      Something went wrong!')
                else:
                    print('      Something went wrong!')

        elif ret == '15':

            opt = ''
            opt = opt + '\n\n'
            opt = opt + f'      It will loop 10 times or stop when the answer is ACK\n'
            print(opt)

            for attempts in range(0, 10):
                cmd = cmd_question['light'][INDEX_COMMAND]
                ret = ser.send(cmd, reply=cmd_question['light'][INDEX_REPLY][INDEX_REPLY_FLAG])
                if ret:
                    ret = ret[:-1]
                    ret = ret[-1:].pop()
                    if str(ret) == ACK:
                        print('\n      *** The Light sensor IS working! ***')
                        break
                    elif str(ret) == NACK:
                        time.sleep(1)
                        print('      --- NO Light event happened!')
                    else:
                        print('      Something went wrong!')
                else:
                    print('      Something went wrong!')

        elif ret == '16':

            cmd = cmd_question['rf_id'][INDEX_COMMAND]
            ret = ser.send(cmd, reply=cmd_question['rf_id'][INDEX_REPLY][INDEX_REPLY_FLAG])
            if ret:
                ret = ret[:-1]
                ret = ret[-3:]
                rf_id = ' '.join(ret)
                print(f'\n      Bytes to TX: {rf_id}')
            else:
                print('      Something went wrong!')

        elif ret == '17':

            cmd = cmd_question['tamper'][INDEX_COMMAND]
            ret = ser.send(cmd, reply=cmd_question['tamper'][INDEX_REPLY][INDEX_REPLY_FLAG])
            if ret:
                ret = ret[:-1]
                ret = ret[-1:].pop()
                if str(ret) == ACK:
                    print('\n      --- Tamper is CLOSE!')
                elif str(ret) == NACK:
                    print('      --- Tamper is OPEN!')
                else:
                    print('      Something went wrong!')
            else:
                print('      Something went wrong!')

        elif ret == '18':

            opt = ''
            opt = opt + '\n\n'
            opt = opt + f'      Enter with the Temperature (°C) you want to send: '
            temp = input(opt)
            temp = str(int_to_hex(int(temp)))

            cmd = list(cmd_information['temperature'][INDEX_COMMAND])
            cmd.append(temp)
            ret = ser.send(cmd, reply=cmd_information['temperature'][INDEX_REPLY][INDEX_REPLY_FLAG])
            if ret:
                ret = ret[:-1]
                ret = ret[-1:].pop()
                if str(ret) == ACK:
                    print(f'     --- Temperature sent [{temp}°C]!')
                else:
                    print('      Something went wrong!')
            else:
                print('      Something went wrong!')

        elif ret == '0':
            print('      Closing the uart!')
            time.sleep(2)
            return False

        time.sleep(2)
        return True

    else:
        print('      Invalid option. Try again!')
        return True
