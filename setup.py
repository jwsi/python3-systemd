from setuptools import setup, find_packages

# Set up your binary file name here.
# It will be added to $PATH
setup(
    name='package_name', # Name of package
    version='1.0.0', # Version of package
    description='Cool Python3 package', # Description of package
    url='https://github.com/jwsi', # Website for more info
    author='James Webb', # Author name (company or personal)
    author_email='example@example.com', # Author email
    packages=find_packages(), # This will find packages as long as directories have __init__.py
    package_data={'package_name': ['important.data']}, # Any data files you wish to bundle with the package
    include_package_data=True, # Use this to include package data above
    python_requires='>=3.7', # Not really relevant unless submitting to PyPi, so this is done in debian folder
    install_requires=['requests'], # Pip modules to depend on
    entry_points={
        'console_scripts': [
            'package_name=package_name.main:main', # Navigate to the function in your main file
        ],
    }
)