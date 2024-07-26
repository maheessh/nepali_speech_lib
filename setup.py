from setuptools import setup, find_packages

setup(
    name="NepaliSpeechLib",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "speechrecognition",
        "gtts",
        "pydub"
    ],
    author="Your Name",
    description="A library for Nepali speech recognition and text-to-speech.",
)
