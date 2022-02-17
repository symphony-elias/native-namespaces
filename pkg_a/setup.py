from setuptools import setup

setup(
    name='eliasc_pkg_a',

    version='1.2.4',

    description='PKG A',
    long_description='',

    author='Elias Croze',

    license='Apache Software License',

    packages=['eliasc_pkg.a'],
    zip_safe=False,

    install_requires=["symphony-bdk-python"]
)
