# -*- coding: utf-8 -*-

import subprocess


COMMON_SUBPROCESS_OPTIONS = {
    'shell': True,
}


def check_git_branch():
    output = subprocess.check_output('git branch', **COMMON_SUBPROCESS_OPTIONS)
    assert '* master' in output.split('\n'), 'Please check current git branch'


def delete_old_files():
    subprocess.call('rm -rf ./noseapp_workspace.egg-info ./dist/', **COMMON_SUBPROCESS_OPTIONS)


def run_tests():
    exit_code = subprocess.call('python setup.py test', **COMMON_SUBPROCESS_OPTIONS)
    assert exit_code == 0, 'Tests was worked with errors'


def upload_to_pip():
    exit_code = subprocess.call('python setup.py register sdist upload', **COMMON_SUBPROCESS_OPTIONS)
    assert exit_code == 0, 'Upload to pip error'


if __name__ == '__main__':
    check_git_branch()
    delete_old_files()
    run_tests()
    upload_to_pip()
