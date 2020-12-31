import unittest
from unittest.mock import MagicMock, Mock, patch

from calculator import Calculator

class CalculatorAddTest(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
        pass    

    # Simple calculation without any mocking of any dependency
    def test_add(self):
        self.assertEqual( self.calculator.add( 1, 1 ), 2 )

    # with decorator
    @patch( "calculator.log_stuff", spec=True )
    def test_add_no_log(self, mock_log_stuff: MagicMock):

        self.assertEqual( self.calculator.add( 1, 1 ), 2 )

        mock_log_stuff.assert_called_once()

    # with context
    def test_add_no_log_with_context_manager(self):
        with patch( "calculator.log_stuff", spec=True ) as mock_log_stuff:
            self.assertEqual( self.calculator.add( 1, 1 ), 2 )

            mock_log_stuff.assert_called_once()

    # applying mock inline
    def test_add_no_log_with_inline_mock(self):
        log_stuff_patcher = patch( "calculator.log_stuff", spec=True )
        mock_log_stuff = log_stuff_patcher.start()
        self.addCleanup( log_stuff_patcher.stop )


if __name__ == "__main__":
    unittest.main()