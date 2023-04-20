from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in crematic/__init__.py
from crematic import __version__ as version

setup(
	name="crematic",
	version=version,
	description="Commercial Real Estate Management and Interaction Tool",
	author="JMG",
	author_email="grijalva10@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
