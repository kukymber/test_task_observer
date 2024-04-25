from setuptools import setup, find_packages

setup(
    name='test_service_flask',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
    ],
    entry_points={
        'console_scripts': [
            'test_service_flask-server=server.app:main'
        ]
    }
)
