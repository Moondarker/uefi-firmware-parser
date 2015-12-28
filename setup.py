#!/usr/bin/env python

from setuptools import setup, find_packages, Extension, Command
import os


class LintCommand(Command):
    """Run pylint on implementation and test code"""

    description = "Run pylint on implementation and test code"
    user_options = []

    _pylint_options = [
        "--max-line-length 80",
        "--ignore-imports yes"
    ]

    _lint_paths = [
        "uefi_firmware/*.py",
        "uefi_firmware/*/*.py",
        "tests/*.py",
        "scripts/*.py",
        "scripts/contrib/*.py",
    ]

    def initialize_options(self):
        """Set default values for options."""
        pass

    def finalize_options(self):
        """Post-process options."""
        pass

    def run(self):
        """Run the command"""
        os.system("pylint %s %s" % (
            " ".join(self._pylint_options),
            " ".join(self._lint_paths),
        ))

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='UEFI Firmware Parser',
    version='0.2',
    description='Various data structures and parsing tools for UEFI firmware.',
    long_description=readme,
    author='Teddy Reed',
    author_email='teddy@prosauce.org',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite="tests",
    cmdclass={
        "lint": LintCommand,
    },

    ext_modules=[
        Extension(
            'uefi_firmware.efi_compressor',
            sources=[
                os.path.join(
                    "uefi_firmware", "compression", "Tiano", "EfiCompress.c"),
                os.path.join(
                    "uefi_firmware", "compression", "Tiano", "TianoCompress.c"),
                os.path.join(
                    "uefi_firmware", "compression", "Tiano", "Decompress.c"),

                os.path.join(
                    "uefi_firmware", "compression", "LZMA", "SDK", "C", "Bra86.c"),
                os.path.join(
                    "uefi_firmware", "compression", "LZMA", "SDK", "C", "LzFind.c"),
                os.path.join(
                    "uefi_firmware", "compression", "LZMA", "SDK", "C", "LzmaDec.c"),
                os.path.join(
                    "uefi_firmware", "compression", "LZMA", "SDK", "C", "LzmaEnc.c"),
                os.path.join(
                    "uefi_firmware", "compression", "LZMA", "LzmaCompress.c"),
                os.path.join(
                    "uefi_firmware", "compression", "LZMA", "LzmaDecompress.c"),

                os.path.join("uefi_firmware", "compression", "EfiCompressor.c")
            ],
            include_dirs=[
                os.path.join("uefi_firmware", 'compression', 'Include')
            ],
        )
    ],

    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Topic :: Security',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords="security uefi firmware parsing bios",
)
