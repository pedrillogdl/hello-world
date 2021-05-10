import unittest
import filecmp


class TestFilecmp(unittest.TestCase):
    def test_happyPath(self):
        # Right: Testing that the app is doing what it should do
        # comparing txt with txt, then a jpg with a jpg,
        # also a jpg with another jpg that is the same file
        # with a different name, then the negative test
        # comparing two different txt,
        # two different jpg  and two different binaries with the same name
        self.assertTrue(filecmp.cmp("mobydick.txt", "mobydickV1.txt"))
        self.assertTrue(filecmp.cmp("Puppy.jpg", "Puppy.jpg"))
        self.assertTrue(filecmp.cmp("Puppy.jpg", "anotherPuppy.jpg"))
        self.assertFalse(filecmp.cmp("mobydick.txt", "elprincipito.txt"))
        self.assertFalse(filecmp.cmp("Puppy.jpg", "notthesamepic.jpg"))
        self.assertFalse(filecmp.cmp("Puppy.jpg", "Puppy.png"))

    def test_boundary(self):
        # B: Testing boundaries, comparing a file with nothing,
        # entering a wrong argument comparing a file with a file
        # that doesn't exist, missing another argument
        # comparing with wrong arguments
        with self.assertRaises(Exception):
            filecmp.cmp("mobydick.txt", "")
        with self.assertRaises(Exception):
            filecmp.cmp("mobydick.txt", mobydick.txt)
        with self.assertRaises(Exception):
            filecmp.cmp("mobydick.txt", "thisfiledoesnexist.txt")
        with self.assertRaises(Exception):
            filecmp.cmp("", "thifiledoesnexist.txt")
        with self.assertRaises(Exception):
            filecmp.cmp(mobydick.txt, "thifiledoesnexist.txt")
        with self.assertRaises(Exception):
            filecmp.cmp("thisfiledoesnexist.txt", "mobydick.txt")

    def test_inverse(self):
        # I: Comparing the output of the method with itself,
        # first case is TRUE FALSE, then TRUE TRUE and the end FALSE FALSE
        self.assertNotEqual(filecmp.cmp("mobydick.txt", "mobydickV1.txt"), filecmp.cmp("mobydick.txt", "elprincipito.txt"))
        self.assertEqual(filecmp.cmp("mobydick.txt", "mobydickV1.txt"), filecmp.cmp("mobydick.txt", "mobydickV1.txt"))
        self.assertEqual(filecmp.cmp("mobydick.txt", "elprincipito.txt"), filecmp.cmp("mobydick.txt", "elprincipito.txt"))

   # def test_errors(self):
        # E: Testing a file that doesn't have permissions
        #with self.assertRaises(Exception):
            #filecmp.cmp("mobydick.txt", "mobydickV2.txt")


if __name__ == '__main__':
    unittest.main()
