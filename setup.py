# coding: utf-8
from setuptools import setup, find_packages

setup(
    name='uploadossfile',
    version='0.1.1',
    description='upload oss file',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    author='ivan',
    url='https://github.com',
    author_email='chongwuwy@163.com',
    license='MIT',
    packages=find_packages(),  # 需要处理哪里packages，当然也可以手动填，例如['pip_setup', 'pip_setup.ext']
    include_package_data=False,
    zip_safe=True,
)