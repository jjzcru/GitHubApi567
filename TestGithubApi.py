# -*- coding: utf-8 -*-
"""
@author: Jose J. Cruz
"""

import unittest

from GithubApi import get_commits, get_repositories


class TestTriangles(unittest.TestCase):
    # Test that it can get the repositories from a user
    def test_get_repositories(self):
        user = "jjzcru"
        repositories = get_repositories(user)
        self.assertGreater(len(repositories), 0)
        self.assertEqual(type(repositories), list)

    # Test that it can get the commits from a repo
    def test_get_commits(self):
        user = "jjzcru"
        repo = "elk"
        commits = get_commits(user, repo)
        print(commits)
        self.assertEqual(type(commits), list)
        self.assertEqual(len(commits), 30)
