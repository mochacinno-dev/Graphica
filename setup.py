from setuptools import setup, find_packages

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="graphica",
    version="1.0.0",
    author="Camila 'Mocha' Rose",
    author_email="rblossom.dev@gmail.com",
    description="The simplest Python GUI library - create beautiful desktop applications with minimal code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mochacinno-dev/Graphica",
    project_urls={
        "Bug Tracker": "https://github.com/mochacinno-dev/Graphica/issues",
        "Documentation": "https://mochacinno-dev.github.io/Graphica",
        "Source Code": "https://github.com/mochacinno-dev/Graphica",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: User Interfaces",
    ],
    python_requires=">=3.6",
    install_requires=[
        # Graphica has no external dependencies!
        # tkinter comes with Python
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=4.0",
        ],
    },
    keywords="gui tkinter desktop ui interface simple easy",
    license="MIT",
)