import unittest
from main import summ, diff

class TestMain(unittest.TestCase):
  def Test_s1(self):
    self.assertEqual(summ(1, 3), 4)
  def Test_s2(self):
    self.assertEqual(summ(10, 100), 110)
  def Test_s3(self):
    self.assertEqual(summ(13, 7), 20)
  def Test_d1(self):
    self.assertEqual(diff(17, 1), 16)
  def Test_d2(self):
    self.assertEqual(diff(13, 4), 9)
  def Test_d3(self):
    self.assertEqual(diff(15, 5), 10)


if __name__ == '__main__':
  unittest.main()
