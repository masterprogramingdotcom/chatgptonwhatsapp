from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='ChatGPTonWhatsApp',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'beautifulsoup4',
        'openai',
        'bs4'
    ],
    description="The following is a Python Package [ChatGPT on WhatsApp] that uses the Selenium and OpenAI libraries to create a chatbot for WhatsApp. The chatbot listens to incoming messages, processes them using OpenAI's GPT-3 language model, and replies with a generated response.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Danish Ali',
    author_email='help@masterprograming.com',
    license='MIT',
    url='https://github.com/masterprogramingdotcom/chatgptonwhatsapp',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
