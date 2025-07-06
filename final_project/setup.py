"""
Setup configuration for EmotionDetection package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="EmotionDetection",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for emotion detection using IBM Watson NLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/doronkatz/zzrjt-practice-project-emb-ai",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
    ],
    entry_points={
        "console_scripts": [
            "emotion-detector=EmotionDetection.emotion_detection:main",
        ],
    },
)
