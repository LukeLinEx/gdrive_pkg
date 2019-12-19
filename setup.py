from setuptools import setup

setup(
    name='gdrive_pkg',
    packages=['gdrive_pkg'],
    include_package_data=True,
    install_requires=[
        "google_auth_oauthlib",
        "google-api-python-client"
    ]
)
