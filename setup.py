from setuptools import find_packages,setup
#call setup method
setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Prtaiksha Patel',
    author_email='pratiksha@cloudyuga.guru',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2","beautifulsoup4"],
    packages=find_packages()
)
