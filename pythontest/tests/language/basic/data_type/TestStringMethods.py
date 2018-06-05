import unittest


class TestStringMethods (unittest.TestCase):
    string1 = 'foo'
    string2 = 'Foo'
    string3 = 'FOO'
    string4 = 'hello world'

    def test_upper(self):
        self.assertEqual(self.string1.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue(self.string3.isupper())
        self.assertFalse(self.string2.isupper())

    def test_islower(self):
        self.assertTrue(self.string1.islower())
        self.assertFalse(self.string2.islower())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
