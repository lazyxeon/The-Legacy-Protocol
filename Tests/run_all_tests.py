import unittest

if name == 'main': loader = unittest.TestLoader() suite = loader.discover('.', pattern='test_*.py')

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

if not result.wasSuccessful():
    exit(1)

