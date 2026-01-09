import unittest
import contribute
import os
import shutil
import tempfile
import stat
from subprocess import check_output


class TestContribute(unittest.TestCase):

    def setUp(self):
        self.original_cwd = os.getcwd()
        self.test_dir = tempfile.mkdtemp()
        os.chdir(self.test_dir)

    def tearDown(self):
        os.chdir(self.original_cwd)

        def on_rm_error(func, path, exc_info):
            os.chmod(path, stat.S_IWRITE)
            func(path)
        shutil.rmtree(self.test_dir, onerror=on_rm_error)

    def test_arguments(self):
        args = contribute.arguments(['-nw'])
        self.assertTrue(args.no_weekends)
        self.assertEqual(args.max_commits, 10)

    def test_contributions_per_day(self):
        args = contribute.arguments(['-mc=20'])
        val = contribute.contributions_per_day(args)
        self.assertTrue(1 <= val <= 20)

    def test_commits(self):
        contribute.main(['-nw',
                         '--user_name=sampleusername',
                         '--user_email=your-username@users.noreply.github.com',
                         '-mc=12',
                         '-fr=100',
                         '-db=10',
                         '-da=5'])

        # Find the created repository directory
        dirs = [d for d in os.listdir('.')
                if os.path.isdir(d) and d.startswith('repository-')]
        self.assertTrue(len(dirs) > 0, "Repository directory was not created")

        repo_dir = os.path.join(os.getcwd(), dirs[0])
        commit_count = int(check_output(
            ['git', 'rev-list', '--count', 'HEAD'],
            cwd=repo_dir).decode('utf-8'))

        # 10 days before + 5 days after = 15 days total
        # Some might be weekends.
        self.assertTrue(commit_count > 0)
        self.assertTrue(commit_count <= 15 * 12)
