from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mcs_custom_reports/__init__.py
from mcs_custom_reports import __version__ as version

setup(
	name="mcs_custom_reports",
	version=version,
	description="custom reports",
	author="DT Team",
	author_email="dev2@dipanetech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
