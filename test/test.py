import unittest
import user_interface

class LearningMapTest(unittest.TestCase):





    def test_can_submit_skill_progress(self):
        aList = [1, 1, 1, 4, 6, 5, 6, 7, 8, 9, 10,
                 'one', 'two', 'three', 'four', 'five',
                 'six', 'seven', 'eight', 'nine', 'ten']
        writer(aList)
        self.assertEqual(aList, reader(1))


    def test_can_view_skils_progress(self):

    def test_can_save_skill_progress_text(self):





if __name__ == '__main__':
    unittest.main()
