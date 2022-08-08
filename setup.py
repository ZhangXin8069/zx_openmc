import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="zx_openmc",
  version="0.0.1",
  author="zhangxin",
  author_email="1514962740@qq.com",
  description="This is a solution to the OpenMC benchmark",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/zx2810/zx_openmc",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)