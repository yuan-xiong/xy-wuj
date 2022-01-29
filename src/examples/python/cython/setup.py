from distutils.core import setup, Extension
from Cython.Build import Cythonize

ext_modules=[Extension("add_wrapper", sources=["add_wrapper.pyx"], librarys=["add"], library_dirs=["."])]
setup(name='wrapper for libadd', ext_modules=Cythonize(ext_modules),)
#setup(name='wrapper for libadd', cmdclass={'build_ext': build_ext}, ext_modules=ext_modules)

#from distutils.extension import Extension
#from Cython.Distutils import build_ext
#
#ext_modules = [
#    Extension("esb_install", ["cic2.py"]),
#]
#setup(name="cic2", cmdclass={'build_ext': build_ext}, ext_modules=ext_modules)

