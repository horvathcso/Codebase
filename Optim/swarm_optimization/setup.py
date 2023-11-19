from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Swarm based optimization algortihms'
LONG_DESCRIPTION = 'Swarm based heuristic algorithms for optimization'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="swarm_algorithms", 
        version=VERSION,
        author="Csongor Horváth",
        author_email="<sifuto2013@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['optimization', 'swarm inteligence'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)