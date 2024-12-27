from setuptools import setup, find_packages

setup(
    name="custom_gemini",
    version="2.0.0",
    author="Daniel Núñez Cano",
    author_email="danielnunezcano@gmail.com",
    description="Librería para generar respuestas limpias usando Google Gemini API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/danielnunezcano/gemini-custom",
    packages=find_packages(),
    install_requires=[
        "google-generativeai>=0.8.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
