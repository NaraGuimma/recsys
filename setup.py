from setuptools import setup, Extension

try:
    import numpy as np
except ImportError:
    exit('Please install numpy first.\nUse pip install numpy.')

try:
    from Cython.Build import cythonize
    from Cython.Distutils import build_ext
except ImportError:
    exit('You need Cython too :(.\n Use pip install cython.\nNo more requirements, promise!')

extensions = [
    Extension(
        'recsys.recommender.funksvd',
        ['recsys/recommender/funksvd.pyx'],
        include_dirs=[np.get_include()]
    ),
    Extension(
        'recsys.recommender.fm',
        ['recsys/recommender/fm.pyx'],
        include_dirs=[np.get_include()]
    )
]
ext_modules = cythonize(extensions)

setup(name='recsys',
      version='0.1.1',
      description='a simple recommender systems library in python',
      url='http://github.com/mayukh18/reco',
      author='Shenghui Li',
      author_email='lishenghui.uu@gmail.com',
      license='MIT',
      download_url = 'https://github.com/mayukh18/reco/tarball/0.2.1',
      include_package_data = True,
      keywords=['recommendation'],
      packages=['recsys',
                'recsys.recommender',
                'recsys.datasets',
                'recsys.metrics',
                'recsys.cross_validation'],
      ext_modules = ext_modules,
      cmdclass= {'build_ext': build_ext},
      install_requires=['numpy',
                        'pandas',
                        ],
      zip_safe=False
      )