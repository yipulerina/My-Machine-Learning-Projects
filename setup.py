from setuptools import setup, find_packages

setup(name= "census_income", 
      version="0.0.1",
      author = "Yipu",
      author_email="lerinayipu@gmail.com",
      packages= find_packages(),
      install_requires = ["numpy", "pandas", "flask"]
      )
