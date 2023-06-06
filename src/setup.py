from setuptools import setup


setup(name='pyuqspice',
      version='0.0.1',
      description='Tools for uncertainty quantification and LTSpice',
      url='https://github.com/karylsienn/PyUQSpice',
      author='Karol Niewiadomski',
      author_email='niewiadomski.k@wp.pl',
      install_requires=['pandas', 'numpy', 'mmap'],
      packages=['ltspicer', 'pystatemc'],
      zip_safe=False)
