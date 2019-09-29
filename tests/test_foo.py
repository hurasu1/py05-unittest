import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        import sample.foo
        self.assertEqual(sample.foo.greeting(), "hello")


if __name__ == '__main__':
    unittest.main()
