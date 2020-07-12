from setuptools import setup

with open('gabriel_udacity_distributions/README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='gabriel_udacity_distributions',
      version='0.92',
      description='Gaussian and Binomial distributions',
      packages=['gabriel_udacity_distributions'],
      author='Gabriel Francis',
      author_email='gncis8@gmail.com',
      long_description=long_description,
      long_description_content_type='text/markdown',
      zip_safe=False)

