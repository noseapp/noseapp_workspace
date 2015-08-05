# -*- coding: utf-8 -*-

import os
import subprocess


PYTHON_BIN = 'python'
BRANCH_FOR_BUILD = 'master'
COMMON_SUBPROCESS_OPTIONS = {
    'shell': True,
}


def sudo(command):
    if os.getlogin() != 'root':
        return 'sudo {}'.format(command)
    return command


def check_git_branch():
    output = subprocess.check_output(
        'git branch',
        **COMMON_SUBPROCESS_OPTIONS
    )
    assert '* {}'.format(BRANCH_FOR_BUILD) in output.split('\n'),\
        'Please check current git branch. Branch for build "{}"'.format(BRANCH_FOR_BUILD)


def to_delete_old_files():
    subprocess.call(
        sudo('rm -rf ./noseapp_workspace.egg-info ./dist/'),
        **COMMON_SUBPROCESS_OPTIONS
    )


def run_tests():
    exit_code = subprocess.call(
        sudo('{} setup.py test'.format(PYTHON_BIN)),
        **COMMON_SUBPROCESS_OPTIONS
    )
    assert exit_code == 0, 'Tests was worked with errors'


def upload_to_pip():
    exit_code = subprocess.call(
        sudo('{} setup.py register sdist upload'.format(PYTHON_BIN)),
        **COMMON_SUBPROCESS_OPTIONS
    )
    assert exit_code == 0, 'Upload to pip error'


def main():
    check_git_branch()
    to_delete_old_files()
    run_tests()
    upload_to_pip()


if __name__ == '__main__':
    main()
