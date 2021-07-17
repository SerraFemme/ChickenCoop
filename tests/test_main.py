import unittest
from src.main import DoorManager


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.warden = DoorManager()

    def test_new(self):
        self.assertIsNotNone(self.warden)

    def test_is_the_system_on(self):
        self.assertTrue(self.warden.is_system_on())

    def test_turn_the_system_off(self):
        self.assertTrue(self.warden.is_system_on())
        self.warden.turn_system_off()
        self.assertFalse(self.warden.is_system_on())

    def test_turn_system_off_then_on(self):
        self.warden.turn_system_off()
        self.assertFalse(self.warden.is_system_on())
        self.warden.turn_system_on()
        self.assertTrue(self.warden.is_system_on())

    def test_check_door_is_closed(self):
        self.assertTrue(self.warden.is_door_closed())

    def test_open_door(self):
        self.warden.open_door()
        self.assertFalse(self.warden.is_door_closed())

    def test_door_can_open_then_close(self):
        self.warden.open_door()
        self.assertFalse(self.warden.is_door_closed())
        self.warden.close_door()
        self.assertTrue(self.warden.is_door_closed())

    def test_opening_door_when_door_disabled_is_on_throws_DoorOpenDisabled(self):
        self.warden.disable_door_open()
        self.assertRaises(self.warden.DoorOpenDisabled, self.warden.open_door)

    def test_door_closes_when_door_is_open_and_door_open_disabled_is_active(self):
        self.warden.open_door()
        self.assertFalse(self.warden.is_door_closed())
        self.warden.disable_door_open()
        self.warden.close_door()
        self.assertTrue(self.warden.is_door_closed())

    def test_warden_knows_the_time(self):
        test_time = self.warden.get_current_time()
        self.assertTrue(test_time)
        print("Current Time: " + test_time)

    def test_warden_opens_the_door_at_6_AM(self):
        self.warden.morning_operations()
        self.assertFalse(self.warden.is_door_closed())

    def test_warden_closes_the_door_at_9_PM(self):
        self.warden.evening_operations()
        self.assertTrue(self.warden.is_door_closed())

    def test_warden_operates_on_assigned_schedule(self):
        pass


if __name__ == '__main__':
    unittest.main()
