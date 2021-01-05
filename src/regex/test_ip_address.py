import unittest
from ip_address import IpAddress

class IpAddressTest(unittest.TestCase):

    def test_should_create_valid_address(self):
        # given
        # when
        # then
        self.assertTrue( IpAddress(1,2,3,4).is_valid() )
        self.assertTrue( IpAddress(0,0,0,0).is_valid() )
        self.assertTrue( IpAddress(255,255,255,255).is_valid() )
        self.assertTrue( IpAddress(128,23,67,110).is_valid() )

    def test_should_reject_invalid_address(self):
        # given
        # when
        # then
        self.assertFalse( IpAddress().is_valid() )
        self.assertFalse( IpAddress(135).is_valid() )
        self.assertFalse( IpAddress(1,2,3,4,5).is_valid() )
        self.assertFalse( IpAddress(-1,2,-3,4).is_valid() )
        self.assertFalse( IpAddress(256,256,256,256).is_valid() )
        self.assertFalse( IpAddress(800,2455,2,480).is_valid() )

    def test_should_create_from_string(self):
        # given
        var = IpAddress(1,2,3,4)
        # when

        # then
        self.assertTrue( IpAddress.from_str("1.2.3.4").is_valid() )
        self.assertFalse( IpAddress.from_str("123.800.355.44").is_valid() )

    def test_should_access_octet_by_index(self):
        # given
        ip = IpAddress(1,2,3,4)

        # when

        # then
        self.assertEqual( ip[0], 1 )
        self.assertEqual( ip[1], 2 )
        self.assertEqual( ip[2], 3 )
        self.assertEqual( ip[3], 4 )

        with self.assertRaises(IndexError):
            ip[5]

        with self.assertRaises(IndexError):
            ip[-1]


if __name__ == "__main__":
    unittest.main()