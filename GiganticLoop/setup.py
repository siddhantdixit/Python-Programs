from setuptools import setup
setup(
    name='gigloop',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'gigloop=gigloop:run'
        ]
    }
)