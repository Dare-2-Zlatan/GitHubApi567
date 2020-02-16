import unittest

from github_ap import get_repo_info


class TestGetRepo(unittest.TestCase):
    def test_normal_response(self):
        expected = ['User: Dare-2-Zlatan',
                    'Repo: 567 Number of commits: 3',
                    'Repo: Assignment00_567 Number of commits: 2',
                    'Repo: Triangle567 Number of commits: 8']
        self.assertEqual(get_repo_info(), expected)

    def test_bad_user_name(self):
        self.assertEqual(get_repo_info('sfgbshb'), 'unable to fetch repos from user')
        self.assertEqual(get_repo_info(''), 'unable to fetch repos from user')


if __name__ == '__main__':
    unittest.main()