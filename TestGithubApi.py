# -*- coding: utf-8 -*-
"""
@author: Jose J. Cruz
"""

import unittest
from unittest.mock import Mock

from GithubApi import get_commits, get_repositories

get_repositories = Mock(return_value=[
  {
    "id": 5836951,
    "node_id": "MDEwOlJlcG9zaXRvcnk1ODM2OTUx",
    "name": "BinaryConverter",
    "full_name": "jjzcru/BinaryConverter",
    "private": False,
    "html_url": "https://github.com/jjzcru/BinaryConverter",
    "description": "Transform from decimal to binary",
    "default_branch": "master"
  }
])
get_commits = Mock(return_value=[{
    "sha": "3e5ec92bfecd83620a3a77a243f2f785305670c6"
}])

class TestTriangles(unittest.TestCase):
    # Test that it can get the repositories from a user
    def test_get_repositories(self):
        user = "jjzcru"
        repositories = get_repositories(user)
        self.assertEqual(len(repositories), 1)
        self.assertEqual(type(repositories), list)

    # Test that it can get the commits from a repo
    def test_get_commits(self):
        user = "jjzcru"
        repo = "elk"
        commits = get_commits(user, repo)
        self.assertEqual(type(commits), list)
        self.assertEqual(len(commits), 1)