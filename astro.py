#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Download and display FITS images from the James Webb Space Telescope repository on the MAST Portal.

Usage:
    Run this file and write the name of the MAST Portal FITS file. Write the extension value after downloading the file and wait for the image to appear.

Author:
    Tiago Floriano - 2022-08-01

License:
    GNU GPL v3 License

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>5.
'''

import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits
from astropy.utils.data import download_file
import shutil
import os

print '############################'
arquivo = input('Nome do arquivo FITS: ')
print '############################'
narquivo = '{}.fits'.format(arquivo)

# verifica se o arquivo já foi baixado e faz o download caso necessário
if os.path.exists(narquivo) == False:
    tmp_path = \
        download_file('https://mast.stsci.edu/portal/Download/file?uri=mast:JWST/product/{}.fits'.format(arquivo),
                      cache=False)
    shutil.move(tmp_path, narquivo)

plt.style.use(astropy_mpl_style)

image_file = get_pkg_data_filename(narquivo)

fits.info(image_file)
print '############################'
extop = int(input('Ext: '))
print '############################'

image_data = fits.getdata(image_file, ext=extop)

print image_data.shape

plt.figure()
plt.imshow(image_data, cmap='gray')

plt.colorbar()

# plt.savefig('{nomearquivo}_{valorext}.png'.format(nomearquivo=arquivo,valorext=extop))

plt.show()
