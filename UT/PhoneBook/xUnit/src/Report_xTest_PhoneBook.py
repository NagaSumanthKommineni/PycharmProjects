from unittest import TestLoader, TestSuite

from HtmlTestRunner import HTMLTestRunner

from xUnit.src.xTest_PhoneBook import Test_PhoneBooth

phonebook_tests = TestLoader().loadTestsFromTestCase(Test_PhoneBooth)

suite = TestSuite([phonebook_tests])

runner = HTMLTestRunner(output='PhoneBooth Tests',
                        verbosity=0,
                        descriptions='Unit Test Result set for Phone booth class',
                        report_title='UnitTest Report for PhoneBooth.py')

runner.run(suite)