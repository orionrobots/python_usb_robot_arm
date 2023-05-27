import usb_arm
import unittest
import time


def time_msec():
    return round(time.time() * 1000.0)


class StubUsb:
    def __init__(self):
        self.ctrl_commands = []

    def ctrl_transfer(self, reqType, req, value, idx, data=None, length=None):
        # print("ctl_transfer(%s, %s, %s, %s, %s, %s)" % (reqType, req, value, idx, data, length))
        assert reqType == 0x40
        assert req == 6
        assert value == 0x100
        self.ctrl_commands.append((data, time_msec()))

    def get_last_ctrl_command(self):
        return self.ctrl_commands[len(self.ctrl_commands)-1]

    def get_ctrl_commands(self):
        return self.ctrl_commands

    def reset(self):
        self.ctrl_commands = []


class TestableArm(usb_arm.Arm):
    def __init__(self):
        self.dev = StubUsb()

    def get_ctrl_cmd(self, idx):
        return self.dev.get_ctrl_commands()[idx]

    def get_ctrl_cmds(self):
        return self.dev.get_ctrl_commands()

    def get_ctrl_cmd_list(self):
        return list(map(lambda cmd: cmd[0], self.dev.get_ctrl_commands()))


class UsbArmTest(unittest.TestCase):

    def setUp(self):
        self.arm = TestableArm()

    def test_move_includes_correct_verb(self):
        self.arm.move(usb_arm.LedOn)
        cmd, time = self.arm.get_ctrl_cmd(0)
        self.assertEqual(usb_arm.LedOn, cmd)

    def test_move_adds_stop_verb(self):
        self.arm.move(usb_arm.ShoulderDown)
        self.assertEqual([usb_arm.ShoulderDown, usb_arm.Stop], self.arm.get_ctrl_cmd_list())

    def test_default_move_time_spaces_commands_as_expected(self):
        self.arm.move(usb_arm.ElbowUp)
        cmd0, time0 = self.arm.get_ctrl_cmd(0)
        cmd1, time1 = self.arm.get_ctrl_cmd(1)
        self.assertIn(time1 - time0, range(990, 1010))

    def test_specific_move_time_spaces_commands_as_expected(self):
        self.arm.move(usb_arm.ElbowUp, 2)
        cmd0, time0 = self.arm.get_ctrl_cmd(0)
        cmd1, time1 = self.arm.get_ctrl_cmd(1)
        self.assertIn(time1 - time0, range(1090, 2010))

    def test_untimed_seq_of_commands_orders_as_expected(self):
        cmds = [[usb_arm.ElbowUp], [usb_arm.ElbowDown], [usb_arm.ShoulderDown]]
        self.arm.doActions(cmds)
        expected_cmds = []
        for c in cmds:
            expected_cmds.append(c[0])
            expected_cmds.append(usb_arm.Stop)
        self.assertEqual(expected_cmds, self.arm.get_ctrl_cmd_list())

    def test_timed_seq_of_commands_orders_as_expected(self):
        cmds = [[usb_arm.ElbowUp, 1], [usb_arm.ElbowDown, 2], [usb_arm.ShoulderDown, 3]]
        self.arm.doActions(cmds)
        expected_cmds = []
        for c in cmds:
            expected_cmds.append(c[0])
            expected_cmds.append(usb_arm.Stop)
        self.assertEqual(expected_cmds, self.arm.get_ctrl_cmd_list())

    def test_timed_seq_of_commands_has_expected_times(self):
        cmds = [[usb_arm.BaseCtrClockWise, 2], [usb_arm.ElbowUp, 4]]
        self.arm.doActions(cmds)
        cmd0, time0 = self.arm.get_ctrl_cmd(0)
        cmd1, time1 = self.arm.get_ctrl_cmd(1)
        cmd2, time2 = self.arm.get_ctrl_cmd(2)
        cmd3, time3 = self.arm.get_ctrl_cmd(3)
        self.assertIn(time1 - time0, range(1090, 2010))
        self.assertIn(time2 - time1, range(0, 5))
        self.assertIn(time3 - time2, range(3090, 4010))

    def test_both_grips_action_names_exist(self):
        self.assertEqual(usb_arm.GripsOpen, usb_arm.OpenGrips)
        self.assertEqual(usb_arm.GripsClose, usb_arm.CloseGrips)


if __name__ == '__main__':
    unittest.main()
