 #   Copyright (C) 2017-2022  Gavin W
 #   This program is free software: you can redistribute it and/or modify
 #   it under the terms of the GNU General Public License as published by
 #   the Free Software Foundation, either version 3 of the License, or
 #   (at your option) any later version.

 #   This program is distributed in the hope that it will be useful,
 #   but WITHOUT ANY WARRANTY; without even the implied warranty of
 #   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #   GNU General Public License for more details.

 #   You should have received a copy of the GNU General Public License
 #   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
from setuptools import setup, find_packages
from glob import glob
from KvFront.constants import *
import os,stat


# prefix = os.path.join( os.sys.prefix, "share" )
prefix = "KvFront"
server_cfg = os.path.join(prefix,'kvfront','config','server.conf')

with open("README.md", "r") as fh:
    description = fh.read()
with open("CHANGES.md", "r") as fh2:
    changelog= fh2.read()
long_description = description + "\n\n" + changelog


setup(
    name="KvFront",
    version="2.5.1",
    keywords=["memcached", "memcache", "memcached GUI", "memcached front","redis","redis GUI"],
    description="KvFront is a gui tool for memcached & redis developed by GTK+3",
    long_description=long_description,
    license="GPLv3",
    author="Gavin W",
    author_email="qmongofront@live.com",
    url="https://github.com/wgalaxy/KvFront",
    packages=find_packages(),
    include_package_data=True,
    # zip_safe= True,
    platforms="any",
    python_requires='>=3.6',
    install_requires=['python-memcached>=1.58', 'configparser>=3.5.0','redis>=4.1.0','sshtunnel>0.3.0'],
    
    # data_files=[(os.path.join(prefix,'kvfront','config'), glob('./config/*.conf')),
    # 	(os.path.join(prefix, 'applications'), ['./data/kvfront.desktop']),
    # 	(os.path.join(prefix, 'kvfront','icons'), glob('./icons/*.png')),
    # 	(os.path.join(prefix, 'kvfront','ui'), glob('./ui/*.ui'))],

    data_files=[(os.path.join(prefix,'config'), glob('./config/*.conf')),
    	(os.path.join('share','icons'), glob('./icons/*.*')),
        (os.path.join('share', 'applications'), ['./data/kvfront.desktop']),
    	(os.path.join(prefix,'ui'), glob('./ui/*.ui'))],

	entry_points = {
    'console_scripts':[
        'KvFront = KvFront.kvfront:main'
    	]
	}
 )  
# os.chmod(server_cfg, stat.S_IRWXO|stat.S_IRWXG|stat.S_IRWXU)

