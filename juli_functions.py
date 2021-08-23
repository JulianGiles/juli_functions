#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:36:22 2019

@author: julian.giles
"""

#%% --------- mult_hd multiplicadores para ajustar unidades -----------------
def unit_multipliers(): #para ajustar las unidades de los datasets a un común

    mult_hd = {'pre': {'RCA4':[24,0], 'RCA4CLIM':[24,0], 'LMDZ':[8,0], 'LMDZCLIM':[1,0], 'JRA-55':[8,0], 'ERA5':[24*1000,0], 'TRMM-3B42':[8,0], 'CMORPH':[8,0], 'CRU':[1/30,0], 'GLEAM+CMORPH+ERA5':[8,0]},
                'pre_nodrizzle': {'RCA4':[8,0], 'RCA4CLIM':[8,0], 'LMDZ':[8,0], 'LMDZCLIM':[1,0], 'JRA-55':[8,0], 'TRMM-3B42':[8,0], 'CMORPH':[8,0]},
             'lhf': {'RCA4':[-1,0], 'RCA4CLIM':[-1,0], 'LMDZ':[-1,0],'LMDZCLIM':[-1,0], 'JRA-55':[1,0], 'ERA5':[-1,0]},
             'shf': {'RCA4':[-1,0], 'RCA4CLIM':[-1,0], 'LMDZ':[-1,0],'LMDZCLIM':[-1,0], 'JRA-55':[1,0], 'ERA5':[-1,0]},
             'lwr': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[-1,0], 'ERA5':[1,0]},
             'swr': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[-1,0], 'ERA5':[1,0]},
             't2m': {'RCA4':[1,-273.15], 'RCA4CLIM':[1,-273.15], 'LMDZ':[1,-273.15], 'LMDZCLIM':[1,-273.15], 'JRA-55':[1,-273.15], 'ERA5':[1,-273.15]},
             'evapot': {'RCA4':[24,0], 'RCA4CLIM':[24,0], 'LMDZ':[86400,0], 'LMDZCLIM':[86400,0], 'JRA-55':[0.0352512,0], 'ERA5':[-60*60*24,0], 'GLEAM+CMORPH+ERA5':[1,0]},
             'slp': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             
             'u1000': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'u950': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'u900': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'u850': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'u800': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'u750': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'u700': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'u600': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'u500': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'u200': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},

             'v900': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'v850': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'v200': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},

             'q2m': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'qu900': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'qv900': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'quv900conv': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'q900': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0],'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'qu2d': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0],'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'qv2d': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0],'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'vimfc2d': {'RCA4':[86400,0], 'RCA4CLIM':[86400,0], 'LMDZ':[86400,0],'LMDZCLIM':[86400,0], 'JRA-55':[86400,0], 'ERA5':[-86400,0], 'GLEAM+CMORPH+ERA5':[-86400,0]},
             'uv900conv': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0],'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[-1,0]},
             'uv850conv': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0],'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[-1,0]},
             'u10m': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'v10m': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'uv10mconv': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'zi': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[0,0], 'ERA5':[1,0]},
             
             'w1000': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'w950': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'w900': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'w850': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'w800': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'w750': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'w700': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'w600': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'w500': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             
             't900': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             
             'gpot900': {'RCA4':[1/9.8,0], 'RCA4CLIM':[1/9.8,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'gpot200': {'RCA4':[1/9.8,0], 'RCA4CLIM':[1/9.8,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             
             'sm1': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0], 'GLEAM+CMORPH+ERA5':[1,0]},
             'swa': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'EF': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]}, #para pasar los datos a mm/day y correr la T a Celsius
             'EF_v2': {'RCA4':[1,0], 'RCA4CLIM':[1,0],'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'precwtr': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'cloudbot': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[1,0], 'ERA5':[1,0]},
             'totcc': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[0.01,0], 'ERA5':[1,0]},
             'lowcc': {'RCA4':[1,0], 'RCA4CLIM':[1,0], 'LMDZ':[1,0], 'LMDZCLIM':[1,0], 'JRA-55':[0.01,0], 'ERA5':[1,0]},
             'orog': {'RCA4':[1/9.8,0], 'RCA4CLIM':[1/9.8,0], 'LMDZ':[1/9.8,0], 'LMDZCLIM':[1/9.8,0], 'JRA-55':[1/9.8,0], 'ERA5':[1/9.8,0], 'GLEAM+CMORPH+ERA5':[1/9.8,0]}} 
    
    return mult_hd

def units_labels(): # diccionario con el nombre de las unidades a usar
    units_labels={'pre': '$\mathregular{mm⋅day^{-1}}$', #'mm/day',
                  'pre_nodrizzle': '$\mathregular{mm⋅day^{-1}}$', #'mm/day',
             'lhf': '$\mathregular{W⋅m^{-2}}$', #'W/m²',
             'shf': '$\mathregular{W⋅m^{-2}}$', #'W/m²',
             'lwr': '$\mathregular{W⋅m^{-2}}$', #'W/m²',
             'swr': '$\mathregular{W⋅m^{-2}}$', #'W/m²',
             't2m': '°C',
             'evapot': '$\mathregular{mm⋅day^{-1}}$', #'mm/day',
             'slp': 'Pa',
             'v900': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'uv900': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             
             'u1000': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'u950': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'u900': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'u850': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'u800': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'u750': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'u700': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'u600': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'u500': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'u200': '$\mathregular{m⋅s^{-1}}$', #'m/s',

             'v200': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'v850': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             
             'uv850': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'uv200': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             
             'q2m': 'kg/kg',
             'q900': 'kg/kg',
             'qu900': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'qv900': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'quv900conv': '$\mathregular{s^{-1}}$', #'1/s',
             'qu2d': '$\mathregular{kg⋅m^{-1}⋅s^{-1}}$', #'kg/m/s',
             'qv2d': '$\mathregular{kg⋅m^{-1}⋅s^{-1}}$', #'kg/m/s',
             'quv2d': '$\mathregular{kg⋅m^{-1}⋅s^{-1}}$', #'kg/m/s',
             'vimfc2d': '$\mathregular{mm⋅day^{-1}}$', #'mm/day',
             'uv900conv': '$\mathregular{s^{-1}}$', #'1/s',
             'uv850conv': '$\mathregular{s^{-1}}$', #'1/s',
             'u10m': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'v10m': '$\mathregular{m⋅s^{-1}}$', #'m/s',
             'uv10mconv': '$\mathregular{s^{-1}}$', #'1/s',
             'EF': '' ,
             'EF_v2': '' ,
             'swa': '' ,
             'zi': 'm',

             'w1000': '$\mathregular{Pa⋅s^{-1}}$', #'Pa/s',
             'w950': '$\mathregular{Pa⋅s^{-1}}$', #'Pa/s',
             'w900': '$\mathregular{Pa⋅s^{-1}}$', #'Pa/s',
             'w850': '$\mathregular{Pa⋅s^{-1}}$', #'Pa/s',
             'w800': '$\mathregular{Pa⋅s^{-1}}$', #'Pa/s',
             'w750': '$\mathregular{Pa⋅s^{-1}}$', #'Pa/s',
             'w700': '$\mathregular{Pa⋅s^{-1}}$', #'Pa/s',
             'w600': '$\mathregular{Pa⋅s^{-1}}$', #'Pa/s',
             'w500': '$\mathregular{Pa⋅s^{-1}}$', #'Pa/s',
             
             't900': 'K',
             
             'gpot900': 'gpm',
             'gpot200': 'gpm',
             
             'sm1': 'm',

             'precwtr': '$\mathregular{kg⋅m^{-2}}$', #kg/m2',
             'cloudbot': 'm',
             'lowcc': '', 
             'totcc': '',
             'orog': 'm'} 
    return units_labels

def units_labels_old(): # diccionario con el nombre de las unidades a usar
    units_labels={'pre': '$\mathregular{mm⋅day^{-1}}$', #'mm/day',
                  'pre_nodrizzle': '$\mathregular{mm⋅day^{-1}}$', #'mm/day',
             'lhf': 'W/m²',
             'shf': 'W/m²',
             'lwr': 'W/m²',
             'swr': 'W/m²',
             't2m': 'C',
             'evapot': '$\mathregular{mm⋅day^{-1}}$', #'mm/day',
             'slp': 'Pa',
             'v900': 'm/s',
             'uv900': 'm/s',
             
             'u1000': 'm/s',
             'u950': 'm/s',
             'u900': 'm/s',
             'u850': 'm/s',
             'u800': 'm/s',
             'u750': 'm/s',
             'u700': 'm/s',
             'u600': 'm/s',
             'u500': 'm/s',
             'u200': 'm/s',

             'v200': 'm/s',
             'v850': 'm/s',
             
             'uv850': 'm/s',
             'uv200': 'm/s',
             
             'q2m': 'kg/kg',
             'q900': 'kg/kg',
             'qu900': 'm/s',
             'qv900': 'm/s',
             'quv900conv': '1/s',
             'qu2d': 'kg/m/s',
             'qv2d': 'kg/m/s',
             'quv2d': 'kg/m/s',
             'vimfc2d': '$\mathregular{mm⋅day^{-1}}$', #'mm/day',
             'uv900conv': '1/s',
             'uv850conv': '1/s',
             'u10m': 'm/s',
             'v10m': 'm/s',
             'uv10mconv': '1/s',
             'EF': '' ,
             'EF_v2': '' ,
             'swa': '' ,
             'zi': 'm',

             'w1000': 'Pa/s',
             'w950': 'Pa/s',
             'w900': 'Pa/s',
             'w850': 'Pa/s',
             'w800': 'Pa/s',
             'w750': 'Pa/s',
             'w700': 'Pa/s',
             'w600': 'Pa/s',
             'w500': 'Pa/s',
             
             't900': 'K',
             
             'gpot900': 'gpm',
             'gpot200': 'gpm',
             
             'sm1': 'm',

             'precwtr': 'kg/m2',
             'cloudbot': 'm',
             'lowcc': '', 
             'totcc': '',
             'orog': 'm'} 
    return units_labels

def regions():
    regions = {'NEA':[-65,-57,-35,-25, "black"],
               'JEXIT': [-62,-58,-30,-25, 'Red'],
               'SALLJ':[-62,-54,-30,-20, "black"],
               'BH':[-50,-40,-20,-10, "black"],
               'SWA':[-70,-60,-12,-7, "black"]
               }
    return regions
#%% -------- VARIABLES FILES ------------
def files_dict():
    # diccionario con los nombres de los archivos:
    files =dict()
    files['RCA4'] = {'pre': 'CTL/Data/1980-2012/pre/pre_1982-2012.nc',
             'lhf': 'CTL/Data/1980-2012/lhf/lhf_198001_201212_sSA.nc',
             'shf': 'CTL/Data/1980-2012/shf/shf_198001_201212_sSA.nc',
             'lwr': 'CTL/Data/1980-2012/lwr/netlwr_198001_201212_sSA.nc',
             'swr': 'CTL/Data/1980-2012/swr/netswr_198001_201212_sSA.nc',
             't2m': 'CTL/Data/1980-2012/t2m/t2m_1982-2012.nc',
             'evapot': 'CTL/Data/1980-2012/evapot/evapot_1982-2012.nc',
             'slp': 'CTL/Data/1980-2012/slp/slp_198001_201212_sSA.nc',
             'u900': 'CTL/Data/1980-2012/u-v/u900_1983-2012.nc',
             'u200': 'CTL/Data/1980-2012/u-v/u200_1983-2012.nc',
             'v900': 'CTL/Data/1980-2012/u-v/v900_1983-2012.nc',
             'v200': 'CTL/Data/1980-2012/u-v/v200_1983-2012.nc',
             'uv900conv': 'CTL/Data/1980-2012/u-v/uv900_conv_1980-2012.nc',
             'u10m': 'CTL/Data/1980-2012/u-v_10m/u10m_198001_201212_sSA.nc',
             'v10m': 'CTL/Data/1980-2012/u-v_10m/v10m_198001_201212_sSA.nc',
             'uv10mconv': 'CTL/Data/1980-2012/u-v_10m/uv10m_conv_1980-2012.nc',
             'q2m': 'CTL/Data/1980-2012/q2m/q2m_198001_201212_sSA.nc',
             'q900': 'CTL/Data/1980-2012/q/q900_198001_201212_sSA.nc',
             'qu900': 'CTL/Data/1980-2012/qu-qv/qu900_1983-2012.nc',
             'qv900': 'CTL/Data/1980-2012/qu-qv/qv900_1983-2012.nc',
             'quv900conv': 'CTL/Data/1980-2012/qu-qv/quv900conv_1983-2012.nc',
             'qu2d': 'CTL/Data/1980-2012/qu2d-qv2d/qu2d_198001_201212_sSA.nc',
             'qv2d': 'CTL/Data/1980-2012/qu2d-qv2d/qv2d_198001_201212_sSA.nc',
             'vimfc2d': 'CTL/Data/1980-2012/vimfc2d/vimfc2d_198001_201212_sSA.nc',
             'swa': 'CTL/Data/1980-2012/swa/swa_198001_201212_sSA.nc',
             'zi': 'CTL/Data/1980-2012/zi/zi_198001_201212_sSA.nc',
             'w900': 'CTL/Data/1980-2012/w/w900_198001_201212_sSA.nc',
             'w500': 'CTL/Data/1980-2012/w/w500_1983-2012.nc',
             'cloudbot': 'CTL/Data/1980-2012/cloudbot/cloudbot_198001_201212_sSA.nc',
             'lowcc': 'CTL/Data/1980-2012/lowcc/lowcc_198001_201212_sSA.nc',
             'totcc': 'CTL/Data/1980-2012/totcc/totcc_198001_201212_sSA.nc',
             'precwtr': 'CTL/Data/1980-2012/precwtr/precwtr_198001_201212_sSA.nc',
             'sm1': 'CTL/Data/1980-2012/sm/sm1_1982-2012.nc',
             't900': 'CTL/Data/1980-2012/t/t900_198001_201212_sSA.nc',
             'gpot900': 'CTL/Data/1980-2012/gpot/gpot900_198001_201212_sSA.nc',
             'gpot200': 'CTL/Data/1980-2012/gpot/gpot200_198001_201212_sSA.nc',
             'orog': 'CTL/Data/1980-2012/land_data/gpot.nc',
             'lsmask': 'CTL/Data/1980-2012/land_data/frland.nc'}

    files['RCA4CLIM'] = {'pre': 'CLIM/Data/1980-2012/pre/pre_1982-2012.nc',
             'lhf': 'CLIM/Data/1980-2012/lhf/lhf_198001_201212_sSA.nc',
             'shf': 'CLIM/Data/1980-2012/shf/shf_198001_201212_sSA.nc',
             'lwr': 'CLIM/Data/1980-2012/lwr/netlwr_198001_201212_sSA.nc',
             'swr': 'CLIM/Data/1980-2012/swr/netswr_198001_201212_sSA.nc',
             't2m': 'CLIM/Data/1980-2012/t2m/t2m_1982-2012_3h.nc',
             'evapot': 'CLIM/Data/1980-2012/evap_c/evap_c_1982-2012.nc',
             'slp': 'CLIM/Data/1980-2012/slp/slp_198001_201212_sSA.nc',
             'u900': 'CLIM/Data/1980-2012/u-v/u900_1983-2012.nc',
             'u200': 'CLIM/Data/1980-2012/u-v/u200_1983-2012.nc',
             'v900': 'CLIM/Data/1980-2012/u-v/v900_1983-2012.nc',
             'v200': 'CLIM/Data/1980-2012/u-v/v200_1983-2012.nc',
             'uv900conv': 'CLIM/Data/1980-2012/u-v/uv900_conv_1980-2012.nc',
             'u10m': 'CLIM/Data/1980-2012/u-v_10m/u10m_198001_201212_sSA.nc',
             'v10m': 'CLIM/Data/1980-2012/u-v_10m/v10m_198001_201212_sSA.nc',
             'uv10mconv': 'CLIM/Data/1980-2012/u-v_10m/uv10m_conv_1980-2012.nc',
             'q2m': 'CLIM/Data/1980-2012/q2m/q2m_198001_201212_sSA.nc',
             'q900': 'CLIM/Data/1980-2012/q/q900_1983-2012.nc',
             'qu900': 'CLIM/Data/1980-2012/qu-qv/qu900_1983-2012.nc',
             'qv900': 'CLIM/Data/1980-2012/qu-qv/qv900_1983-2012.nc',
             'quv900conv': 'CLIM/Data/1980-2012/qu-qv/quv900conv_1983-2012.nc',
             'qu2d': 'CLIM/Data/1980-2012/qu2d-qv2d/qu2d_198001_201212_sSA.nc',
             'qv2d': 'CLIM/Data/1980-2012/qu2d-qv2d/qv2d_198001_201212_sSA.nc',
             'vimfc2d': 'CLIM/Data/1980-2012/vimfc2d/vimfc2d_198001_201212_sSA.nc',
             'swa': 'CLIM/Data/1980-2012/swa/swa_198001_201212_sSA.nc',
             'zi': 'CLIM/Data/1980-2012/zi/zi_198001_201212_sSA.nc',
             'w900': 'CLIM/Data/1980-2012/w/w900_198001_201212_sSA.nc',
             'w500': 'CLIM/Data/1980-2012/w/w500_1983-2012.nc',
             'cloudbot': 'CLIM/Data/1980-2012/cloudbot/cloudbot_198001_201212_sSA.nc',
             'lowcc': 'CLIM/Data/1980-2012/lowcc/lowcc_198001_201212_sSA.nc',
             'totcc': 'CLIM/Data/1980-2012/totcc/totcc_198001_201212_sSA.nc',
             'precwtr': 'CLIM/Data/1980-2012/precwtr/precwtr_198001_201212_sSA.nc',
             'sm1': 'CLIM/Data/1980-2012/sm/sm1_198001_201212_sSA_fixed.nc',
             't900': 'CLIM/Data/1980-2012/t/t900_198001_201212_sSA.nc',
             'gpot900': 'CLIM/Data/1980-2012/gpot/gpot900_198001_201212_sSA.nc',
             'gpot200': 'CLIM/Data/1980-2012/gpot/gpot200_198001_201212_sSA.nc',
             'orog': 'CTL/Data/1980-2012/land_data/gpot.nc',
             'lsmask': 'CTL/Data/1980-2012/land_data/frland.nc'}

    
    files['LMDZ'] = {'pre': 'LMDZ/CTL/rainsnow/LMDZ_3h_rainsnow_1979-2012_new.nc', #(LMDZ new esta en mm/3h)
             'lhf': 'LMDZ/CTL/latf/latf_1983-2012_mon.nc',
             'shf': 'LMDZ/CTL/senf/senf_1983-2012_mon.nc',
             'lwr': 'LMDZ/CTL/lwr/lwr_1983-2012_mon.nc',
             'swr': 'LMDZ/CTL/swr/swr_1983-2012_mon.nc',
             't2m': 'LMDZ/CTL/t2m/LMDZ_3h_t2m_1979-2012.nc',
             'evapot': 'LMDZ/CTL/evap/evap_c_1982-2012_day.nc',
             'u900': 'LMDZ/CTL/vitu/LMDZ_day_vitu_1979-2012_000900.nc',
             'v900': 'LMDZ/CTL/vitv/LMDZ_day_vitv_1979-2012_000900.nc',
             'uv900conv': 'LMDZ/CTL/uvconv/LMDZ_day_uv900_convergence_1979-2012.nc',
             'u850': 'LMDZ/CTL/vitu/LMDZ_day_vitu_1979-2012_000850.nc',
             'v850': 'LMDZ/CTL/vitv/LMDZ_day_vitv_1979-2012_000850.nc',
             'uv850conv': 'LMDZ/CTL/uvconv/LMDZ_day_uv850_convergence_1979-2012.nc',
             'qu2d': 'LMDZ/CTL/vimtu/LMDZ_3h_vimtu_1979-2012.nc',
             'qv2d': 'LMDZ/CTL/vimtv/LMDZ_3h_vimtv_1979-2012.nc',
             'vimfc2d': 'LMDZ/CTL/vimfc2d/LMDZ_3h_vimfc2d_1979-2012.nc',
             'w900': 'LMDZ/CTL/w/w_1983-2012000900.nc',
             'w500': 'LMDZ/CTL/w/w_1983-2012000500.nc'}

    files['LMDZCLIM'] = {'pre': 'LMDZ/CLIM/pre/pre_1982-2012_day_new.nc', 
             'lhf': 'LMDZ/CLIM/latf/latf_1983-2012_mon.nc',
             'shf': 'LMDZ/CLIM/senf/senf_1983-2012_mon.nc',
             'lwr': 'LMDZ/CLIM/lwr/lwr_1983-2012_mon.nc',
             'swr': 'LMDZ/CLIM/swr/swr_1983-2012_mon.nc',
             't2m': 'LMDZ/CLIM/t2m/t2m_1982-2012_day.nc',
             'evapot': 'LMDZ/CLIM/evap_c/evap_c_1982-2012_day.nc',
             'u900': 'LMDZ/CLIM/u-v/u_1983-2012000900.nc',
             'v900': 'LMDZ/CLIM/u-v/v_1983-2012000900.nc',
             'qu2d': 'LMDZ/CLIM/qu-qv/qu_1983-2012.nc',
             'qv2d': 'LMDZ/CLIM/qu-qv/qv_1983-2012.nc',
             'vimfc2d': 'LMDZ/CLIM/vimfc2d/',
             'w900': 'LMDZ/CLIM/w/w_1983-2012000900.nc',
             'w500': 'LMDZ/CLIM/w/w_1983-2012000500.nc'}

    
    files['JRA-55'] = {'pre': 'JRA-55/pre/pre_forecast3h_198210-201301_new.nc', # CUIDADO CON EL CORRIMIENTO DE TIEMPO. LOS PROMEDIOS TIENEN SU TIEMPO AL INICIO DEL INTERVALO, EL RESTO SON INSTANTANEOS.
             'lhf': 'JRA-55/lhf/lhf_1983-2012.nc',
             'shf': 'JRA-55/shf/shf_1983-2012.nc',
             'lwr': 'JRA-55/lwr/netlwr_1983-2012.nc',
             'swr': 'JRA-55/swr/netswr_1983-2012.nc',
             't2m': 'JRA-55/t2m/t2m_forecast3h_1980-2013.nc',
             'evapot': 'JRA-55/evapot/evapot_1982-2012.nc',
             'slp': 'JRA-55/sea_lvl_pressure/slp_diagnostic3h_1980-2012.nc',
             'u900': 'JRA-55/u-v/u900_1983-2012_new.nc',
             'v900': 'JRA-55/u-v/v900_1983-2012_new.nc',
             'uv900conv': 'JRA-55/u-v/uv900_convergence_1983-2012.nc',
             'u10m': 'JRA-55/u-v_10m/u10m_diagnostic3h_1980-2012.nc',
             'v10m': 'JRA-55/u-v_10m/v10m_diagnostic3h_1980-2012.nc',
             'uv10mconv': 'JRA-55/u-v_10m/uv10m_convergence_1980-2012.nc',
             'q2m': 'JRA-55/q2m/q2m_diagnostic3h_1980-2012.nc',
             'q900': 'JRA-55/q/q900_analysis6h_1980-2012.nc',
             'qu900': 'JRA-55/qu_qv/qu900_1983-2012.nc',
             'qv900': 'JRA-55/qu_qv/qv900_1983-2012.nc',
             'quv900conv': 'JRA-55/qu_qv/quv900conv_1983-2012.nc',
             'qu2d': 'JRA-55/qu2d_qv2d/qu2d_forecast3h_1980-2013.nc',
             'qv2d': 'JRA-55/qu2d_qv2d/qv2d_forecast3h_1980-2013.nc',
             'vimfc2d': 'JRA-55/vimfc2d/vimfc2d_forecast3h_1980-2013.nc',
             'zi': 'JRA-55/',
             'w900': 'JRA-55/w/vvel900_1983-2012.nc',
             'sm1': 'JRA-55/sm/sm_198210-201301.nc',
             'precwtr': 'JRA-55/precwtr/precwtr_1982-2012.nc',
             'lowcc': 'JRA-55/lowcc/lowcc_1982-2012.nc',
             'totcc': 'JRA-55/totcc/totcc_1982-2012.nc',
             'orog': 'JRA-55/land_data/gpot.nc',
             'lsmask': 'JRA-55/sm/sm_198210-201301.nc',
             }

    files['ERA5'] = {'pre': 'ERA5/single_level_vars/total_precipitation/total_precipitation_year_*.nc', 
             'lhf': 'ERA5/single_level_vars/mean_surface_latent_heat_flux/mean_surface_latent_heat_flux_year_*.nc',
             'shf': 'ERA5/single_level_vars/mean_surface_sensible_heat_flux/mean_surface_sensible_heat_flux_year_*.nc',
             'lwr': 'ERA5/single_level_vars/mean_surface_net_long_wave_radiation_flux/mean_surface_net_long_wave_radiation_flux_year_*.nc',
             'swr': 'ERA5/single_level_vars/mean_surface_net_short_wave_radiation_flux/mean_surface_net_short_wave_radiation_flux_year_*.nc',
             't2m': 'ERA5/single_level_vars/2m_temperature/2m_temperature_year_*.nc',
             'evapot': 'ERA5/single_level_vars/mean_evaporation_rate/mean_evaporation_rate_year_*.nc',
             'slp': 'ERA5/single_level_vars/mean_sea_level_pressure/mean_sea_level_pressure_year_*.nc',

             'u1000': 'ERA5/pressure_level_vars/u_component_of_wind/u_component_of_wind_1000_year_*.nc',
             'u950': 'ERA5/pressure_level_vars/u_component_of_wind/u_component_of_wind_950_year_*.nc',
             'u900': 'ERA5/pressure_level_vars/u_component_of_wind/u_component_of_wind_900_year_*.nc',
             'u850': 'ERA5/pressure_level_vars/u_component_of_wind/u_component_of_wind_850_year_*.nc',
             'u800': 'ERA5/pressure_level_vars/u_component_of_wind/u_component_of_wind_800_year_*.nc',
             'u750': 'ERA5/pressure_level_vars/u_component_of_wind/u_component_of_wind_750_year_*.nc',
             'u700': 'ERA5/pressure_level_vars/u_component_of_wind/u_component_of_wind_700_year_*.nc',
             'u600': 'ERA5/pressure_level_vars/u_component_of_wind/u_component_of_wind_600_year_*.nc',
             'u500': 'ERA5/pressure_level_vars/u_component_of_wind/u_component_of_wind_500_year_*.nc',

             'w1000': 'ERA5/pressure_level_vars/vertical_velocity/vertical_velocity_1000_year_*.nc',
             'w950': 'ERA5/pressure_level_vars/vertical_velocity/vertical_velocity_950_year_*.nc',
             'w900': 'ERA5/pressure_level_vars/vertical_velocity/vertical_velocity_900_year_*.nc',
             'w850': 'ERA5/pressure_level_vars/vertical_velocity/vertical_velocity_850_year_*.nc',
             'w800': 'ERA5/pressure_level_vars/vertical_velocity/vertical_velocity_800_year_*.nc',
             'w750': 'ERA5/pressure_level_vars/vertical_velocity/vertical_velocity_750_year_*.nc',
             'w700': 'ERA5/pressure_level_vars/vertical_velocity/vertical_velocity_700_year_*.nc',
             'w600': 'ERA5/pressure_level_vars/vertical_velocity/vertical_velocity_600_year_*.nc',
             'w500': 'ERA5/pressure_level_vars/vertical_velocity/vertical_velocity_500_year_*.nc',

             'v900': 'ERA5/pressure_level_vars/v_component_of_wind/v_component_of_wind_900_year_*.nc',
             'uv900conv': 'ERA5/pressure_level_vars/divergence/divergence_900_year_*.nc',
             'v850': 'ERA5/pressure_level_vars/v_component_of_wind/v_component_of_wind_850_year_*.nc',
             'uv850conv': 'ERA5/pressure_level_vars/divergence/divergence_850_year_*.nc',
             'u10m': 'ERA5/single_level_vars/10m_u_component_of_wind/10m_u_component_of_wind_year_*.nc',
             'v10m': 'ERA5/single_level_vars/10m_v_component_of_wind/10m_v_component_of_wind_year_*.nc',
             'uv10mconv': 'ERA5/single_level_vars/10m_uv_convergence/10m_uv_convergence_year_*.nc',
             'q900': 'ERA5/pressure_level_vars/specific_humidity/specific_humidity_900_year_*.nc',
             'qu900': 'ERA5/pressure_level_vars/qu_qv/qu_900_year_*.nc',
             'qv900': 'ERA5/pressure_level_vars/qu_qv/qv_900_year_*.nc',
             'qu2d': 'ERA5/single_level_vars/vertical_integral_of_eastward_water_vapour_flux/vertical_integral_of_eastward_water_vapour_flux_year_*.nc',
             'qv2d': 'ERA5/single_level_vars/vertical_integral_of_northward_water_vapour_flux/vertical_integral_of_northward_water_vapour_flux_year_*.nc',
             'vimfc2d': 'ERA5/single_level_vars/mean_vertically_integrated_moisture_divergence/mean_vertically_integrated_moisture_divergence_year_*.nc',
             'quv900conv': 'ERA5/pressure_level_vars/qu_qv/quv900conv_*.nc',
             'zi': 'ERA5/single_level_vars/boundary_layer_height/boundary_layer_height_year_*.nc',
             'sm1': 'ERA5/single_level_vars/volumetric_soil_water_layer_1/volumetric_soil_water_layer_1_year_*.nc',
             'precwtr': 'ERA5/single_level_vars/total_column_water_vapour/total_column_water_vapour_year_*.nc',
             'cloudbot': 'ERA5/single_level_vars/cloud_base_height/cloud_base_height_year_*.nc',
             'lowcc': 'ERA5/single_level_vars/low_cloud_cover/low_cloud_cover_year_*.nc',
             'totcc': 'ERA5/single_level_vars/total_cloud_cover/total_cloud_cover_year_*.nc',
             'orog': 'ERA5/single_level_vars/orography_geopotential_rotated.nc',
             'lsmask': 'ERA5/single_level_vars/land-sea_mask_rotated.nc'}
    
    files['TRMM-3B42'] = {'pre': 'TRMM_3B42/TRMM_3B42_3H_1998-2014_7_cut_fixed3h.nc'} #fixed3h es cambiado al formato del resto (acumulado en las 3h previas, in_mm3h es multiplicado por 3 el archivo original)
    
    files['CMORPH'] = {'pre': 'CMORPH/CMORPH_V1.0_CRT_0.25deg-3HLY_cut.nc'}

    files['CRU'] = {'pre': 'CRU/cru_ts3.23.1971.2014.pre.dat.nc'}
    
    files['GLEAM'] = {'sm1': 'GLEAM/v3.5a/daily/*/SMsurf_*_GLEAM_v3.5a.nc',
                      'evapot': 'GLEAM/v3.5a/daily/*/E_*_GLEAM_v3.5a.nc'}
    
    files['ESACCI'] = {'sm1': 'ESA_CCI_SM-v06.1/COMBINED/*/ESACCI-SOILMOISTURE-L3S-SSMV-COMBINED-*-fv06.1.nc'}

    files['GLEAM+CMORPH+ERA5'] = {'pre': 'CMORPH/CMORPH_V1.0_CRT_0.25deg-3HLY_cut.nc',
                             'sm1': 'GLEAM/v3.5a/daily/*/SMsurf_*_GLEAM_v3.5a.nc',
                             'vimfc2d': 'ERA5/single_level_vars/mean_vertically_integrated_moisture_divergence/mean_vertically_integrated_moisture_divergence_year_*.nc',
                             'orog': 'ERA5/single_level_vars/orography_geopotential_rotated.nc',
                             'lsmask': 'ERA5/single_level_vars/land-sea_mask_rotated.nc'}

    return files

#%% ------------ CARGA DE DATOS -------------------

def load_datasets (models, var_list, start_date, end_date, data_path, homepath, files, chunksize, seas_warm, seas_cold, latfix, lonfix, forward_timestep=False, interpolated='no', latlims=(-50.3, 13.5), triRCA=False):
    # forward_timestep=True si quiero que los timesteps indiquen el inicio del intervalo de datos que representa (False para que esté al final)
    # ---------- TOMA DE DATOS -----------
    import xarray as xr
    import numpy as np
    data_xr = dict()
    data = dict()
    lon = dict()
    lat = dict()
    lonproj = dict()
    latproj = dict()
    
    for model in models.keys():
        print("---------------------------- Cargando "+model)
        data_xr[model] = dict()
        data[model] = dict()
        for var in var_list:
            if var in ['EF']: 
                data[model][var] = dict()
                continue
        
            print("Cargando "+var)
            if model == 'JRA-55':
                try: 
                    if var == 'orog':
                        data_xr[model][var] = xr.open_mfdataset(data_path+files[model][var], combine='by_coords', chunks={'time':int(chunksize*10)})
                    else:
                        data_xr[model][var] = xr.open_mfdataset(data_path+files[model][var], combine='by_coords', chunks={'initial_time0_hours':int(chunksize*10)})
                except: 
                    print('               '+var+' not available for '+model+', ignoring')
                    continue
            elif model == 'ERA5' or model == 'GLEAM' or model == 'ESACCI':
                try: data_xr[model][var] = xr.open_mfdataset(data_path+files[model][var], combine='by_coords', chunks={'time':chunksize})
                except: 
                    print('               '+var+' not available for '+model+', ignoring')
                    continue

            elif model == 'CRU':
                try: data_xr[model][var] = xr.open_mfdataset(data_path+files[model][var], combine='by_coords', chunks={'time':chunksize})
                except: 
                    print('               '+var+' not available for '+model+', ignoring')
                    continue


            else:
                try: data_xr[model][var] = xr.open_mfdataset(homepath+files[model][var], combine='by_coords', chunks={'time':(chunksize*10)})
                except: 
                    print('               '+var+' not available for '+model+', ignoring')
                    continue

            var_temp = dict(data_xr[model][var].data_vars)
            
            # get coords names
            lon_name = [coord for coord in set(data_xr[model][var].coords.keys()) if "lon" in coord][0]
            lat_name = [coord for coord in set(data_xr[model][var].coords.keys()) if "lat" in coord][0]
            
            data[model][var] = dict()
            
            nn=1
            
            if var in ['orog','lsmask']:  #para estas hay un solo paso temporal , cambio temporalmente la variable para agarrarlo
                start_aux = start_date
                start_date = '1980-01-01'
            
            if model == 'RCA4' or model == 'RCA4CLIM':
                if triRCA and var in ['zi', 'lhf', 'shf', 'swr', 'lwr', 't2m'] : nn=3  # Para tomar variables horarias de forma trihoraria. Para mejorar: buscarle una forma mas elegante
                if forward_timestep and var not in ['orog', 'lsmask']:
                    if int(data_xr[model][var].coords['time'][2]-data_xr[model][var].coords['time'][1]) < 24*3600000000000 and int(data_xr[model][var].coords['time'][8]-data_xr[model][var].coords['time'][7]) < 24*3600000000000:
                        
                        tshift = data_xr[model][var].coords['time'][3]-data_xr[model][var].coords['time'][2] 
                        data_xr[model][var].coords['time'] = data_xr[model][var].coords['time'] - tshift
                    else:
                        print('!!!!!!!!!!!!! something is not right, unable to shift timesteps !!!!!!!!!!!!!!!!')
                
                if len(data_xr[model][var].coords) == 4:
                    data[model][var][''] = data_xr[model][var].sel(time=slice(start_date, end_date), lat=slice(latlims[0], latlims[1]))[[str(var_name) for var_name in set(var_temp.keys())][0]][::nn,0,:,:]
                else:
                    data[model][var][''] = data_xr[model][var].sel(time=slice(start_date, end_date), lat=slice(latlims[0], latlims[1]))[[str(var_name) for var_name in set(var_temp.keys())][0]][::nn,:,:]
                data[model][var][''].coords[lon_name] = data[model][var][''][lon_name] -360
    	
            if model == 'LMDZ' or model == 'LMDZCLIM':
                if len(data_xr[model][var].coords) == 4:
                    data[model][var][''] = data_xr[model][var].loc[{'time':slice(start_date, end_date), lat_name:slice(latlims[0], latlims[1], latfix[interpolated]), lon_name:slice(278+lonfix[interpolated][model], 326+lonfix[interpolated][model])}][[str(var_name) for var_name in set(var_temp.keys()) if var_name != 'time_bnds'][0]][:,0,:,:]
                if len(data_xr[model][var].coords) == 3:
                    data[model][var][''] = data_xr[model][var].loc[{'time':slice(start_date, end_date), lat_name:slice(latlims[0], latlims[1], latfix[interpolated]), lon_name:slice(278+lonfix[interpolated][model], 326+lonfix[interpolated][model])}][[str(var_name) for var_name in set(var_temp.keys()) if var_name != 'time_bnds'][0]][:,:,:]

                data[model][var][''].coords['time'] = data[model][var]['']['time'] + int(1.5*3600000000000) #sumo 1.5h (en LMDZ las cuentas trihorarias están ubicadas en el centro del intervalo)
                
                if interpolated=='True':
                    data[model][var][''].coords[lon_name] = data[model][var][''][lon_name] -360
                
            if model == 'JRA-55':
                if forward_timestep and var not in ['orog', 'lsmask']:
                    if int(data_xr[model][var].coords['initial_time0_hours'][2]-data_xr[model][var].coords['initial_time0_hours'][1]) < 24*3600000000000 and int(data_xr[model][var].coords['initial_time0_hours'][8]-data_xr[model][var].coords['initial_time0_hours'][7]) < 24*3600000000000:
                        
                        tshift = data_xr[model][var].coords['initial_time0_hours'][3]-data_xr[model][var].coords['initial_time0_hours'][2] 
                        data_xr[model][var].coords['initial_time0_hours'] = data_xr[model][var].coords['initial_time0_hours'] - tshift
                    else:
                        print('!!!!!!!!!!!!! something is not right, unable to shift timesteps !!!!!!!!!!!!!!!!')

                if var=='orog':
                    data[model][var][''] = data_xr[model][var].loc[{'time':slice(start_date, end_date), lat_name:slice(latlims[0], latlims[1]), lon_name:slice(278, 326)}][[str(var_name) for var_name in set(var_temp.keys()) if 'time' not in var_name][0]].rename({'time': 'initial_time0_hours'}).compute()
                elif var=='lsmask':
                    data[model][var][''] = (~np.isnan(data_xr[model][var].loc[{lat_name:slice(latlims[0], latlims[1]), lon_name:slice(278, 326)}][[str(var_name) for var_name in set(var_temp.keys()) if 'time' not in var_name][0]][10:12,0,:,:])).compute()
                elif len(data_xr[model][var].coords) == 4:
                    data[model][var][''] = data_xr[model][var].loc[{'initial_time0_hours':slice(start_date, end_date), lat_name:slice(latlims[0], latlims[1]), lon_name:slice(278, 326)}][[str(var_name) for var_name in set(var_temp.keys()) if 'time' not in var_name][0]][1:,0,:,:]
                else:
                    data[model][var][''] = data_xr[model][var].loc[{'initial_time0_hours':slice(start_date, end_date), lat_name:slice(latlims[0], latlims[1]), lon_name:slice(278, 326)}][[str(var_name) for var_name in set(var_temp.keys()) if 'time' not in var_name][0]][1:,:,:]
                
                data[model][var][''].coords[lon_name] = data[model][var][''][lon_name] -360
            
            if model == 'ERA5':
                if forward_timestep and var not in ['orog', 'lsmask']:
                    if int(data_xr[model][var].coords['time'][2]-data_xr[model][var].coords['time'][1]) < 24*3600000000000 and int(data_xr[model][var].coords['time'][8]-data_xr[model][var].coords['time'][7]) < 24*3600000000000:
                        
                        tshift = data_xr[model][var].coords['time'][3]-data_xr[model][var].coords['time'][2] 
                        data_xr[model][var].coords['time'] = data_xr[model][var].coords['time'] - tshift
                    else:
                        print('!!!!!!!!!!!!! something is not right, unable to shift timesteps !!!!!!!!!!!!!!!!')

                data[model][var][''] = data_xr[model][var].loc[{'time':slice(start_date, end_date), lat_name:slice(latlims[0], latlims[1],-1), lon_name:slice(278-360, 326-360)}][[str(var_name) for var_name in set(var_temp.keys())][0]][:,:,:]
    
            if model == 'TRMM-3B42':
                if forward_timestep and var not in ['orog', 'lsmask']:
                    if int(data_xr[model][var].coords['time'][2]-data_xr[model][var].coords['time'][1]) < 24*3600000000000 and int(data_xr[model][var].coords['time'][8]-data_xr[model][var].coords['time'][7]) < 24*3600000000000:
                        
                        tshift = data_xr[model][var].coords['time'][3]-data_xr[model][var].coords['time'][2] 
                        data_xr[model][var].coords['time'] = data_xr[model][var].coords['time'] - tshift
                    else:
                        print('!!!!!!!!!!!!! something is not right, unable to shift timesteps !!!!!!!!!!!!!!!!')

                data[model][var][''] = data_xr[model][var].loc[{'time':slice(start_date, end_date), lat_name:slice(latlims[0], latlims[1]), lon_name:slice(278+lonfix[interpolated][model], 326+lonfix[interpolated][model])}]['pcp'][1:,:,:]

                if interpolated=='True':
                    data[model][var][''].coords[lon_name] = data[model][var][''][lon_name] -360
                            
            if model == 'CMORPH':
                data[model][var][''] = data_xr[model][var].loc[{'time':slice(start_date, end_date), lat_name:slice(latlims[0], latlims[1]), lon_name:slice(278, 326)}][[str(var_name) for var_name in set(var_temp.keys())][0]][:-1,0,:,:]
                if not forward_timestep: data[model][var][''].coords['time'] = data[model][var]['']['time'] + int(3*3600000000000) #Muevo 3 horas para adelante, el timestep de CMORPH indica el inicio del intervalo de acumulación.
                data[model][var][''].coords[lon_name] = data[model][var][''][lon_name] -360
                                
            if model == 'CRU':
                data[model][var][''] = data_xr[model][var].loc[{'time':slice(start_date, end_date), lat_name:slice(latlims[0], latlims[1]), lon_name:slice(278-360, 326-360)}][[str(var_name) for var_name in set(var_temp.keys())][0]][:,:,:]
                
            if model == 'GLEAM':
                data[model][var][''] = data_xr[model][var].loc[{'time':slice(start_date, end_date), lat_name:slice(latlims[0], latlims[1],-1), lon_name:slice(278-360, 326-360)}][[str(var_name) for var_name in set(var_temp.keys())][0]][:,:,:]

            if model == 'ESACCI':
                data[model][var][''] = data_xr[model][var].loc[{'time':slice(start_date, end_date), lat_name:slice(latlims[0], latlims[1],-1), lon_name:slice(278-360, 326-360)}][[str(var_name) for var_name in set(var_temp.keys())][0]][:,:,:]


            if var in ['orog','lsmask']:  #vuelvo al start date original
                start_date = start_aux

            # extraigo lon y lats
            lon[model] = data[model][var][''][lon_name]
            lat[model] = data[model][var][''][lat_name]
            
            lonproj[model], latproj[model] = np.meshgrid(lon[model], lat[model])
            
            # separo semestres calido y frio 
            print("Separando semestres cálido y frío")
            def is_warm(month):
                return (month >= seas_warm[3]) | (month <= seas_warm[2])
            
            def is_cold(month):
                return (month >= seas_cold[0]) & (month <= seas_cold[5])
            
            def is_summer(month):
                return (month >= 12) | (month <= 2)
            
            def is_winter(month):
                return (month >= 6) & (month <= 8)
            
            def is_spring(month):
                return (month >= 9) & (month <= 11)

            def is_fall(month):
                return (month >= 3) & (month <= 5)

            if model == 'JRA-55':
                if var=='lsmask': continue
                data[model][var]['ONDJFM'] = data[model][var][''].sel(initial_time0_hours=is_warm(data[model][var]['']['initial_time0_hours.month']))
                data[model][var]['AMJJAS'] = data[model][var][''].sel(initial_time0_hours=is_cold(data[model][var]['']['initial_time0_hours.month']))
                data[model][var]['DJF'] = data[model][var][''].sel(initial_time0_hours=is_summer(data[model][var]['']['initial_time0_hours.month']))
                data[model][var]['JJA'] = data[model][var][''].sel(initial_time0_hours=is_winter(data[model][var]['']['initial_time0_hours.month']))
                data[model][var]['MAM'] = data[model][var][''].sel(initial_time0_hours=is_fall(data[model][var]['']['initial_time0_hours.month']))
                data[model][var]['SON'] = data[model][var][''].sel(initial_time0_hours=is_spring(data[model][var]['']['initial_time0_hours.month']))
                data[model][var]['OND'] = data[model][var][''].sel(initial_time0_hours=is_month(data[model][var]['']['initial_time0_hours.month'], [10,11,12]))
                data[model][var]['JFM'] = data[model][var][''].sel(initial_time0_hours=is_month(data[model][var]['']['initial_time0_hours.month'], [1,2,3]))
                
            else:
                data[model][var]['ONDJFM'] = data[model][var][''].sel(time=is_warm(data[model][var]['']['time.month']))
                data[model][var]['AMJJAS'] = data[model][var][''].sel(time=is_cold(data[model][var]['']['time.month']))
                data[model][var]['DJF'] = data[model][var][''].sel(time=is_summer(data[model][var]['']['time.month']))
                data[model][var]['JJA'] = data[model][var][''].sel(time=is_winter(data[model][var]['']['time.month']))
                data[model][var]['MAM'] = data[model][var][''].sel(time=is_fall(data[model][var]['']['time.month']))
                data[model][var]['SON'] = data[model][var][''].sel(time=is_spring(data[model][var]['']['time.month']))
                data[model][var]['OND'] = data[model][var][''].sel(time=is_month(data[model][var]['']['time.month'], [10,11,12]))
                data[model][var]['JFM'] = data[model][var][''].sel(time=is_month(data[model][var]['']['time.month'], [1,2,3]))
                
            
            
        if 'EF' in var_list:
            try:
                if model == 'JRA-55':
                    data[model]['EF'][''] = data[model]['lhf']['']/(data[model]['lhf']['']+data[model]['shf'][''])
                    data[model]['EF']['ONDJFM'] = data[model]['EF'][''].sel(initial_time0_hours=is_warm(data[model]['EF']['']['initial_time0_hours.month']))
                    data[model]['EF']['AMJJAS'] = data[model]['EF'][''].sel(initial_time0_hours=is_cold(data[model]['EF']['']['initial_time0_hours.month']))
                    data[model]['EF']['DJF'] = data[model]['EF'][''].sel(initial_time0_hours=is_summer(data[model]['EF']['']['initial_time0_hours.month']))
                    data[model]['EF']['JJA'] = data[model]['EF'][''].sel(initial_time0_hours=is_winter(data[model]['EF']['']['initial_time0_hours.month']))
                    data[model]['EF']['MAM'] = data[model]['EF'][''].sel(initial_time0_hours=is_fall(data[model]['EF']['']['initial_time0_hours.month']))
                    data[model]['EF']['SON'] = data[model]['EF'][''].sel(initial_time0_hours=is_spring(data[model]['EF']['']['initial_time0_hours.month']))
                    data[model]['EF']['OND'] = data[model]['EF'][''].sel(initial_time0_hours=is_month(data[model]['EF']['']['initial_time0_hours.month'], [10,11,12]))
                    data[model]['EF']['JFM'] = data[model]['EF'][''].sel(initial_time0_hours=is_month(data[model]['EF']['']['initial_time0_hours.month'], [1,2,3]))
        
                else:
                    data[model]['EF'][''] = data[model]['lhf']['']/(data[model]['lhf']['']+data[model]['shf'][''])
                    data[model]['EF']['ONDJFM'] = data[model]['EF'][''].sel(time=is_warm(data[model]['EF']['']['time.month']))
                    data[model]['EF']['AMJJAS'] = data[model]['EF'][''].sel(time=is_cold(data[model]['EF']['']['time.month']))
                    data[model]['EF']['DJF'] = data[model]['EF'][''].sel(time=is_summer(data[model]['EF']['']['time.month']))
                    data[model]['EF']['JJA'] = data[model]['EF'][''].sel(time=is_winter(data[model]['EF']['']['time.month']))    
                    data[model]['EF']['MAM'] = data[model]['EF'][''].sel(time=is_fall(data[model]['EF']['']['time.month']))    
                    data[model]['EF']['SON'] = data[model]['EF'][''].sel(time=is_spring(data[model]['EF']['']['time.month']))    
                    data[model]['EF']['OND'] = data[model]['EF'][''].sel(time=is_month(data[model]['EF']['']['time.month'], [10,11,12]))
                    data[model]['EF']['JFM'] = data[model]['EF'][''].sel(time=is_month(data[model]['EF']['']['time.month'], [1,2,3]))
            
            except KeyError:
                print('lhf or shf missing')
                del(data[model]['EF'])

    return data_xr, data, lon, lat, lonproj, latproj

#%%
# ------------- FUNCIONES PARA SEPARAR EN ESTACIONES ------
    
def is_warm(month, seas_warm = [1,2,3,10,11,12]):
    return (month >= seas_warm[3]) | (month <= seas_warm[2])

def is_cold(month, seas_cold = [4,5,6,7,8,9]):
    return (month >= seas_cold[0]) & (month <= seas_cold[5])

def is_summer(month):
    return (month >= 12) | (month <= 2)

def is_winter(month):
    return (month >= 6) & (month <= 8)

def is_spring(month):
    return (month >= 9) & (month <= 11)

def is_fall(month):
    return (month >= 3) & (month <= 5)

def is_month(time, month):
    # time = es el time.month
    # month = qué mes o meses quiero evaluar si es. Tiene que ser una lista de enteros o una sigla reconocible como DJF
    import numpy as np
    
    allmonths = 'JFMAMJJASONDJFMAMJJASOND'
    allmonthsn = [1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12]
    
    if isinstance(month, str):
        if month == '':
            month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
        else:
            month_list = allmonthsn[allmonths.find(month):allmonths.find(month)+len(month)]
    else:
        month_list = month.copy()
        
    cond = month_list.copy()
    for m,mm in enumerate(month_list):
        cond[m] = (time==mm)
    
    suma = cond[0]
    if len(month_list)>1:
        for m,mm in enumerate(month_list):
            if m >0:
                suma = suma+cond[m]
    return suma
    #return (np.sum(cond, axis=0)==1)
    

#%% ------ PLOT DE FIGURAS -------
def plot_3h_clims(model, seas, var, var_list, filename, clims3h, models, clevs, lon, lat, lonproj, latproj, proj,
                  images_path, units_labels, arrow_scale=4000, arrow_spacing=3): #figuras cada 3h
    # arrow_scale:  a smaller scale parameter makes the arrow longer
    import matplotlib
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import gridspec
    import matplotlib.colors as mcolors
    import cartopy
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
    import os
    from numpy import ma 
    
    fig1 = plt.figure( figsize=(8,5),dpi=300)  #fig size in inches (width, height)
    ax = fig1.add_axes([0.1,0.1,0.9,0.9])
    ax.set_visible(False)
    gs = gridspec.GridSpec(2,4, wspace=0.4, hspace=0.2)
    if 'anom' in filename:
        fig1.suptitle(models[model]+' '+seas+' '+var+' anomalies', fontsize=12)
    else: 
        fig1.suptitle(models[model]+' '+seas+' '+var, fontsize=12)

    if len(clims3h[model][var][seas].hour) >8:
        times = clims3h[model][var][seas].hour[::3]
    else:
        times = clims3h[model][var][seas].hour

                
    for m, time in enumerate(np.array(times)):
        barra = matplotlib.cm.get_cmap('RdYlBu_r') # premade colorbar
        norm = mcolors.BoundaryNorm(boundaries=clevs[var], ncolors=256)
        
        barra= barra_whitecenter(clevs[var] ,colormap=matplotlib.cm.get_cmap('RdYlBu_r'))
        
        ax1 = plt.subplot(gs[m], projection = proj)
        ax1.set_extent([lon[model][0], lon[model][-1], lat[model][0], lat[model][-1]], crs=proj)
        
        index = m #int(m*len(clims3h[model][var][seas].hour)/len(times))

        if len(clims3h[model][var][seas].hour) >8:
            CS1 = ax1.pcolormesh(lonproj[model], latproj[model], 
                                 clims3h[model][var][seas].roll(hour=-1, roll_coords=False).groupby_bins('hour', 8).mean(axis=0).roll(hour_bins=1, roll_coords=False)[m],
                                 norm=norm, transform=proj, cmap=barra) 
        else:
            CS1 = ax1.pcolormesh(lonproj[model], latproj[model], clims3h[model][var][seas][index], norm=norm, transform=proj, cmap=barra) 
        
        #color lower and upper colorbar triangles
        barra.set_over('Maroon')
        barra.set_under('Navy')
        
        ax1.coastlines(resolution='50m', linewidth=1)          # coast
        ax1.add_feature(cartopy.feature.BORDERS, linestyle='-', linewidth=1, alpha=0.7) #countries
        
        parallels = np.arange(-60,30,10.)
        meridians = np.arange(-90,-20,10.)
        lon_formatter = LongitudeFormatter(zero_direction_label=True)
        lat_formatter = LatitudeFormatter()
        ax1.xaxis.set_major_formatter(lon_formatter)
        ax1.yaxis.set_major_formatter(lat_formatter)
        ax1.set_xticks(meridians[1:-1:2], crs=proj)
        ax1.set_yticks(parallels[1:-1], crs=proj)
        ax1.gridlines(crs=proj, xlocs=meridians, ylocs=parallels, linewidth=1, linestyle='--')
        ax1.set_title(str(time)+' UTC', fontsize=12)
        
        if var== 'vimfc2d' and 'qu2d' and 'qv2d' in var_list or \
        var== 'quv900conv' and 'qu900' and 'qv900' in var_list or \
        var== 'uv900conv' and 'u900' and 'v900' in var_list or \
        var== 'uv850conv' and 'u850' and 'v850' in var_list or \
        var== 'uv10mconv' and 'u10m' and 'v10m' in var_list:
            if var=='vimfc2d': vect1= 'qu2d'; vect2= 'qv2d'
            if var=='quv900conv': vect1= 'qu900'; vect2= 'qv900'
            if var=='uv900conv': vect1= 'u900'; vect2= 'v900'
            if var=='uv850conv': vect1= 'u850'; vect2= 'v850'
            if var=='uv10mconv': vect1= 'u10m'; vect2= 'v10m'
            # Vectores
            u = np.ones(clims3h[model][vect1][seas][index].shape,dtype=bool)
            v = np.ones(clims3h[model][vect2][seas][index].shape,dtype=bool)
            
            u[0:np.shape(u)[0]:arrow_spacing,0:np.shape(u)[1]:arrow_spacing]=0
            v[0:np.shape(v)[0]:arrow_spacing,0:np.shape(v)[1]:arrow_spacing]=0
            
            uu = ma.array(clims3h[model][vect1][seas][index],mask = u)
            vv = ma.array(clims3h[model][vect2][seas][index],mask = v)
            
            Q = ax1.quiver(lonproj[model],latproj[model],uu,vv,width=3e-3,
                               headwidth=3,#headwidht (default3)
                               headlength=2.5, scale = arrow_scale[var],
                               transform=proj)  # (default5)
                     
            if m ==3:
                # busco para la quiverkey la magnitud del percentil 90 y redondeo al decimal significativo
                p90 = np.percentile(np.abs(clims3h[model][vect1][seas]), 90)
                deci = int(('%e' % p90).split('e')[1])
                p90round = round(p90, deci)
                
                qk = plt.quiverkey(Q, 1, 1.03, p90round, str(p90round)+' '+units_labels[vect1], labelpos='E')
        
    # add colorbar
    fig1.subplots_adjust(right=0.92)
    cbar_ax = fig1.add_axes([0.94, 0.3, 0.01, 0.4]) #[*left*, *bottom*, *width*,  *height*]
    cb =fig1.colorbar(CS1, cax=cbar_ax, extend='both')
    axis_labels = units_labels[var]
    cb.set_label(axis_labels, labelpad = -2)
    cb.formatter.set_powerlimits((0, 0))  # scientific notation
    
    if not os.path.exists(str(images_path)+'hourly_mean/'+model+'/'+seas):
        os.makedirs(str(images_path)+'hourly_mean/'+model+'/'+seas)
    fig1.savefig(str(images_path)+'hourly_mean/'+model+'/'+seas+'/'+str(filename),dpi=300,bbox_inches='tight',orientation='landscape',papertype='A4')
    plt.close(fig1)
    
def plot_3h_anim_frames(model, seas, var, var_list, filename, clims3h, models, clevs, lon, lat, lonproj, latproj, proj,
                  images_path, units_labels, arrow_scale=4000, arrow_spacing=3):
    import matplotlib
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    import cartopy
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
    import os
    from numpy import ma 

    if len(clims3h[model][var][seas].hour) >8:
        times = clims3h[model][var][seas].hour[::3]
    else:
        times = clims3h[model][var][seas].hour

    for m, time in enumerate(np.array(times)):
        fig1 = plt.figure( figsize=(7,5),dpi=300)  #fig size in inches (width, height)
        
        ax = fig1.add_axes([0.1,0.1,0.9,0.9], projection=proj)
#        fig1.set_title(models[model]+' '+seas+' '+var, fontsize=12)
                
        barra = barra_whitecenter(clevs[var] ,colormap=matplotlib.cm.get_cmap('RdYlBu_r'))
        norm = mcolors.BoundaryNorm(boundaries=clevs[var], ncolors=256)
        
        ax.set_extent([lon[model][0], lon[model][-1], lat[model][0], lat[model][-1]], crs=proj)

        index = m #int(m*len(clims3h[model][var][seas].hour)/len(times))
        
        if len(clims3h[model][var][seas].hour) >8:
            CS1 = ax.pcolormesh(lonproj[model], latproj[model], 
                                 clims3h[model][var][seas].roll(hour=-1, roll_coords=False).groupby_bins('hour', 8).mean(axis=0).roll(hour_bins=1, roll_coords=False)[m],
                                 norm=norm, transform=proj, cmap=barra) 
        else:
            CS1 = ax.pcolormesh(lonproj[model], latproj[model], clims3h[model][var][seas][index], norm=norm, transform=proj, cmap=barra) 
        
        #color lower and upper colorbar triangles
        barra.set_over('Maroon')
        barra.set_under('Navy')
        
        ax.coastlines(resolution='50m', linewidth=1)          # coast
        ax.add_feature(cartopy.feature.BORDERS, linestyle='-', linewidth=1, alpha=0.7) #countries
        
        parallels = np.arange(-60,30,10.)
        meridians = np.arange(-90,-20,10.)
        lon_formatter = LongitudeFormatter(zero_direction_label=True)
        lat_formatter = LatitudeFormatter()
        ax.xaxis.set_major_formatter(lon_formatter)
        ax.yaxis.set_major_formatter(lat_formatter)
        ax.set_xticks(meridians[1:-1:2], crs=proj)
        ax.set_yticks(parallels[1:-1], crs=proj)
        ax.gridlines(crs=proj, xlocs=meridians, ylocs=parallels, linewidth=1, linestyle='--')
        
        if 'anom' in filename:
            ax.set_title(models[model]+' '+seas+' '+var+' anomalies'+'\n'+str(time)+' UTC', fontsize=12)
        else:
            ax.set_title(models[model]+' '+seas+' '+var+'\n'+str(time)+' UTC', fontsize=12)
        
        if var== 'vimfc2d' and 'qu2d' and 'qv2d' in var_list or \
        var== 'quv900conv' and 'qu900' and 'qv900' in var_list or \
        var== 'uv900conv' and 'u900' and 'v900' in var_list or \
        var== 'uv850conv' and 'u850' and 'v850' in var_list or \
        var== 'uv10mconv' and 'u10m' and 'v10m' in var_list:
            if var=='vimfc2d': vect1= 'qu2d'; vect2= 'qv2d'
            if var=='quv900conv': vect1= 'qu900'; vect2= 'qv900'
            if var=='uv900conv': vect1= 'u900'; vect2= 'v900'
            if var=='uv850conv': vect1= 'u850'; vect2= 'v850'
            if var=='uv10mconv': vect1= 'u10m'; vect2= 'v10m'
            # Vectores
            u = np.ones(clims3h[model][vect1][seas][index].shape,dtype=bool)
            v = np.ones(clims3h[model][vect2][seas][index].shape,dtype=bool)
            
            u[0:np.shape(u)[0]:arrow_spacing,0:np.shape(u)[1]:arrow_spacing]=0
            v[0:np.shape(v)[0]:arrow_spacing,0:np.shape(v)[1]:arrow_spacing]=0
            
            uu = ma.array(clims3h[model][vect1][seas][index],mask = u)
            vv = ma.array(clims3h[model][vect2][seas][index],mask = v)
            
            Q = ax.quiver(lonproj[model],latproj[model],uu,vv,width=3e-3,
                               headwidth=3,#headwidht (default3)
                               headlength=2.5, scale = arrow_scale[var],
                               transform=proj)  # (default5)
            
            # busco para la quiverkey la magnitud del percentil 90 y redondeo al decimal significativo
            p90 = np.percentile(np.abs(clims3h[model][vect1][seas]), 90)
            deci = int(('%e' % p90).split('e')[1])
            p90round = round(p90, deci)
            
            qk = plt.quiverkey(Q, 1, 1.03, p90round, str(p90round)+' '+units_labels[vect1], labelpos='E')
        
        # add colorbar
        fig1.subplots_adjust(right=0.92)
        cbar_ax = fig1.add_axes([0.94, 0.3, 0.01, 0.4]) #[*left*, *bottom*, *width*,  *height*]
        cb =fig1.colorbar(CS1, cax=cbar_ax, extend='both')
        axis_labels = units_labels[var]
        cb.set_label(axis_labels, labelpad = -2)
        cb.formatter.set_powerlimits((0, 0))  # scientific notation
        
        if not os.path.exists(str(images_path)+'hourly_mean/'+model+'/'+seas+'/animation'):
            os.makedirs(str(images_path)+'hourly_mean/'+model+'/'+seas+'/animation')
        fig1.savefig(str(images_path)+'hourly_mean/'+model+'/'+seas+'/animation/'+str(filename)+str(time)+'.png',dpi=300,bbox_inches='tight',orientation='landscape',papertype='A4')
        plt.clf()
        plt.cla()
        plt.close(fig1)    
        
def plot_simple_SA_map(model, seas, var, var_list, filename, clims, models, clevs, lon, lat, lonproj, latproj, proj,
                  images_path, units_labels, arrow_scale=4000, arrow_spacing=3, extend='both'):
    import matplotlib
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    import cartopy
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
    import os
    from numpy import ma 

    fig1 = plt.figure( figsize=(6,5),dpi=300)  #fig size in inches (width, height)
    ax = fig1.add_axes([0.1,0.1,0.9,0.8], projection = proj)
    fig1.suptitle(models[model]+' '+seas+' '+var, fontsize=12)
    
    barra= barra_whitecenter(clevs[var] ,colormap=matplotlib.cm.get_cmap('RdYlBu_r'))
    #color lower and upper colorbar triangles
    barra.set_over('Maroon')
    barra.set_under('Navy')

    norm = mcolors.BoundaryNorm(boundaries=clevs[var], ncolors=barra.N)    

    if var[0:2] == 'uv' and var[-4:] != 'conv':
        CS1 = ax.pcolormesh(lonproj[model], latproj[model], np.sqrt(clims[model][var[0]+var[2:]][seas]**2 + clims[model][var[1:]][seas]**2), norm=norm, transform=proj, cmap=barra) 
    elif var[0:3] == 'quv' and var[-4:] != 'conv':
        CS1 = ax.pcolormesh(lonproj[model], latproj[model], np.sqrt(clims[model][var[0:2]+var[3:]][seas]**2 + clims[model][var[0]+var[2:]][seas]**2), norm=norm, transform=proj, cmap=barra) 
    else:        
        CS1 = ax.pcolormesh(lonproj[model], latproj[model], clims[model][var][seas], norm=norm, transform=proj, cmap=barra) 
    
    ax.coastlines(resolution='50m', linewidth=1)          # coast
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', linewidth=1, alpha=0.7) #countries
    ax.set_extent([lon[model][0], lon[model][-1], lat[model][0], lat[model][-1]], crs=proj)

    parallels = np.arange(-60,30,10.)
    meridians = np.arange(-90,-20,10.)
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    ax.set_xticks(meridians[1:-1:2], crs=proj)
    ax.set_yticks(parallels[1:-1], crs=proj)
    ax.gridlines(crs=proj, xlocs=meridians, ylocs=parallels, linewidth=1, linestyle='--')
    
    if var== 'vimfc2d' and 'qu2d' and 'qv2d' in var_list or \
    var== 'uv900conv' and 'u900' and 'v900' in var_list or \
    var== 'uv850conv' and 'u850' and 'v850' in var_list or \
    var== 'uv10mconv' and 'u10m' and 'v10m' in var_list or \
    var== 'uv900' and 'u900' and 'v900' in var_list or \
    var== 'uv200' and 'u200' and 'v200' in var_list or \
    var== 'quv900' and 'qu900' and 'qv900' in var_list or \
    var== 'quv2d' and 'qu2d' and 'qv2d' in var_list:
        if var=='vimfc2d': vect1= 'qu2d'; vect2= 'qv2d'
        if var=='uv900conv': vect1= 'u900'; vect2= 'v900'
        if var=='uv850conv': vect1= 'u850'; vect2= 'v850'
        if var=='uv10mconv': vect1= 'u10m'; vect2= 'v10m'
        if var=='uv900': vect1= 'u900'; vect2= 'v900'
        if var=='uv200': vect1= 'u200'; vect2= 'v200'
        if var=='quv900': vect1= 'qu900'; vect2= 'qv900'
        if var=='quv2d': vect1= 'qu2d'; vect2= 'qv2d'
        # Vectores
        u = np.ones(clims[model][vect1][seas].shape,dtype=bool)
        v = np.ones(clims[model][vect2][seas].shape,dtype=bool)
        
        u[0:np.shape(u)[0]:arrow_spacing,0:np.shape(u)[1]:arrow_spacing]=0
        v[0:np.shape(v)[0]:arrow_spacing,0:np.shape(v)[1]:arrow_spacing]=0
        
        uu = ma.array(clims[model][vect1][seas],mask = u)
        vv = ma.array(clims[model][vect2][seas],mask = v)
        
        Q = ax.quiver(lonproj[model],latproj[model],uu,vv,width=3e-3,
                           headwidth=3,#headwidht (default3)
                           headlength=2.5, scale = arrow_scale[var],
                           transform=proj)  # (default5)
        qk = plt.quiverkey(Q, 1, -0.03, 10, '10 '+units_labels[vect1], labelpos='E')
        
    # add colorbar
    cbar_ax = fig1.add_axes([0.92, 0.3, 0.01, 0.4]) #[*left*, *bottom*, *width*,  *height*]
    cb =fig1.colorbar(CS1, cax=cbar_ax, extend=extend)
    axis_labels = units_labels[var]
    cb.set_label(axis_labels, labelpad = -2)
    cb.formatter.set_powerlimits((0, 0))  # scientific notation
    
    if not os.path.exists(str(images_path)+'/'+model+'/'+seas):
        os.makedirs(str(images_path)+'/'+model+'/'+seas)
    fig1.savefig(str(images_path)+'/'+model+'/'+seas+'/'+str(filename),dpi=300,bbox_inches='tight',orientation='landscape',papertype='A4')
    plt.close(fig1)
    
def generic_SA(variable, folderpath, filename, clevs, barra, lon, lat, lonproj, latproj, proj, title,
                  unit_label, colorbar_ticks=None, extend='both'):
    import matplotlib
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    import cartopy
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
    import os
    from numpy import ma 

    fig1 = plt.figure( figsize=(7,5),dpi=300)  #fig size in inches (width, height)
    ax = fig1.add_axes([0.1,0.1,0.9,0.8], projection = proj)
    fig1.suptitle(title, fontsize=12)
    norm = mcolors.BoundaryNorm(boundaries=clevs, ncolors=256)    
    
    CS1 = ax.pcolormesh(lonproj, latproj, variable, norm=norm, transform=proj, cmap=barra) 
    
    #color lower and upper colorbar triangles
    barra.set_over('Maroon')
    barra.set_under('Navy')
    
    ax.coastlines(resolution='50m', linewidth=1)          # coast
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', linewidth=1, alpha=0.7) #countries
    ax.set_extent([lon[0], lon[-1], lat[0], lat[-1]], crs=proj)

    parallels = np.arange(-60,30,10.)
    meridians = np.arange(-90,-20,10.)
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    ax.set_xticks(meridians[1:-1:2], crs=proj)
    ax.set_yticks(parallels[1:-1], crs=proj)
    ax.gridlines(crs=proj, xlocs=meridians, ylocs=parallels, linewidth=1, linestyle='--')
        
    # add colorbar
    if colorbar_ticks is None: colorbar_ticks=clevs
    cbar_ax = fig1.add_axes([0.94, 0.3, 0.01, 0.4]) #[*left*, *bottom*, *width*,  *height*]
    cb =fig1.colorbar(CS1, cax=cbar_ax, extend=extend, ticks=colorbar_ticks)
    axis_labels = unit_label
    cb.set_label(axis_labels, labelpad = -2)
    cb.formatter.set_powerlimits((0, 0))  # scientific notation
    
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    fig1.savefig(folderpath+str(filename),dpi=300,bbox_inches='tight',orientation='landscape',papertype='A4')
    plt.close(fig1)
    
def plot_eofs(eofs, pcs, expvar, fixer, clevs, lon, lat, lonproj, latproj, proj, images_path, filename, title, units_labels):
    
    import matplotlib
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import gridspec
    import matplotlib.colors as mcolors
    import cartopy
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
    import os
    from numpy import ma 
    matplotlib.rcParams.update({'font.size':12}) #Change font size for all elements

    fig1 = plt.figure( figsize=(5*len(eofs)+5,5),dpi=300)  #fig size in inches (width, height)
    ax = fig1.add_axes([0.1,0.1,0.9,0.9])
    ax.set_visible(False)
    gs = gridspec.GridSpec(1,len(eofs)+1, wspace=0.4, hspace=0.2, width_ratios=[1 for i in range(len(eofs))]+[1.5])
    fig1.suptitle(title, fontsize=12)
                
    #plots eofs
    for m in range(len(eofs)):
        norm = mcolors.BoundaryNorm(boundaries=clevs, ncolors=256)
        
        barra= barra_whitecenter(clevs ,colormap=matplotlib.cm.get_cmap('RdYlBu_r'))
        
        ax1 = plt.subplot(gs[m], projection = proj)
        ax1.set_extent([lon[0], lon[-1], lat[0], lat[-1]], crs=proj)
                
        CS1 = ax1.pcolormesh(lonproj, latproj, eofs[m]*fixer[m], norm=norm, transform=proj, cmap=barra) 
        
        #color lower and upper colorbar triangles
        barra.set_over('Maroon')
        barra.set_under('Navy')
        
        ax1.coastlines(resolution='50m', linewidth=1)          # coast
        ax1.add_feature(cartopy.feature.BORDERS, linestyle='-', linewidth=1, alpha=0.7) #countries
        
        parallels = np.arange(-60,30,10.)
        meridians = np.arange(-90,-20,10.)
        lon_formatter = LongitudeFormatter(zero_direction_label=True)
        lat_formatter = LatitudeFormatter()
        ax1.xaxis.set_major_formatter(lon_formatter)
        ax1.yaxis.set_major_formatter(lat_formatter)
        ax1.set_xticks(meridians[1:-1:2], crs=proj)
        ax1.set_yticks(parallels[1:-1], crs=proj)
        ax1.gridlines(crs=proj, xlocs=meridians, ylocs=parallels, linewidth=1, linestyle='--')
        ax1.set_title('EOF'+str(m+1)+' ('+str(round(float(expvar[m]),1))+'%)', fontsize=12)
                
    #plots pcs
    ax2 = plt.subplot(gs[m+1])
    CS2 = plt.plot(pcs[:,0].time, pcs[:,0]*fixer[0], label='PC1') 
    for pcnumber in np.arange(1,len(eofs)):
        plt.plot(pcs[:,pcnumber].time, pcs[:,pcnumber]*fixer[pcnumber], label='PC'+str(pcnumber+1))
    plt.xticks(pcs[:,0].time, rotation=90)
    plt.xlabel('year')
    ax2.xaxis.set_label_coords(0.8, -0.1)
    plt.ylim(-2,2)
    plt.yticks(np.arange(-2,2.5,0.5))
    plt.grid()
    plt.legend()
    ax2.set_title('PCs')
    #sub2.set_ymargin(0.5)
    
    # add colorbar
    cbar_ax = fig1.add_axes([0.06, 0.3, 0.01, 0.4]) #[*left*, *bottom*, *width*,  *height*]
    cb =fig1.colorbar(CS1, cax=cbar_ax, extend='both')
    axis_labels = units_labels
    cb.set_label(axis_labels, labelpad = -2)
    cb.formatter.set_powerlimits((0, 0))  # scientific notation
    
    if not os.path.exists(images_path):
        os.makedirs(images_path)
    fig1.savefig(str(images_path)+str(filename),dpi=300,bbox_inches='tight',orientation='landscape',papertype='A4')
    plt.close(fig1)
    
def plot_hodographs(var_x, var_y, regions, title, units_labels, images_path, filename, model_name=None): #model_name desactivado
    # var_x and var_y are dict like with name of variable: dataarray
    import matplotlib
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import gridspec
    import matplotlib.colors as mcolors
    import cartopy
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
    import os
    from numpy import ma 
    
    matplotlib.rcParams.update({'font.size':12}) #Change font size for all elements

    # para las etiquetas de los subplots
    numbering = ['a)', 'b)', 'c)', 'd)', 'e)', 'f)', 'g)', 'h)', 'i)', 'j)', 'k)', 'l)', 'm)', 'o)', 'p)', 'q)', 'r)', 's)']
        
    # lista de marcadores:
    markers = ['^', 'o', 's', '.', '*']
    # lista de colores:
    colors = ['Crimson', 'SteelBlue', 'LimeGreen', 'Gold', 'HotPink', 'DimGray', 'DarkViolet', 'MediumSeaGreen', 'Orange']
    
    def make_patch_spines_invisible(ax):
        ax.set_frame_on(True)
        ax.patch.set_visible(False)
        for sp in ax.spines.values():
            sp.set_visible(False)
    
    m=0
    mm=0
    fig1 = plt.figure( figsize=(5,1+5*len(regions.keys())),dpi=300)  #fig size in inches
    fig1.suptitle(title, fontsize=20)
    ax = fig1.add_axes([0.1,0.1,0.9,0.9])
    ax.set_visible(False)
    gs = gridspec.GridSpec(len(regions.keys()),1, wspace=0.5, hspace=0.3)

    mm=mm+1
    
    #creo diccionarios contenedores
    dc_reg = dict()
    for var_x_name in var_x.keys():
        dc_reg[var_x_name] =  dict()
        break
    for var_y_name in var_y.keys():
        dc_reg[var_y_name] =  dict()

    #calculo medias por regiones y ploteo
    for reg in regions.keys():
        #saco nombres de las coordenadas    
        lon_name = [coord for coord in set(var_x[var_x_name].coords.keys()) if "lon" in coord][0]
        lat_name = [coord for coord in set(var_x[var_x_name].coords.keys()) if "lat" in coord][0]
        time_name = var_x[var_x_name].dims[0]

        dc_reg[var_x_name][reg] = var_x[var_x_name].loc[{lat_name:slice(regions[reg][2], regions[reg][3]), lon_name:slice(regions[reg][0], regions[reg][1])}].mean(axis=(1,2))
        
        par = dict()
        LL = dict()
        if mm == 1:
            fig1.text(0.05,0.96-1/(len(regions)+1.2)*(m+1),reg,transform=ax.transAxes, fontsize=12, horizontalalignment='center', verticalalignment='center',rotation='vertical', weight='bold')
        
        for yy,var_y_name in enumerate(var_y.keys()):
            #saco nombres de las coordenadas    
            lon_name = [coord for coord in set(var_y[var_y_name].coords.keys()) if "lon" in coord][0]
            lat_name = [coord for coord in set(var_y[var_y_name].coords.keys()) if "lat" in coord][0]
            
            dc_reg[var_y_name][reg] = var_y[var_y_name].loc[{lat_name:slice(regions[reg][2], regions[reg][3]), lon_name:slice(regions[reg][0], regions[reg][1])}].mean(axis=(1,2))          
            
            if yy == 0:
                host = plt.subplot(gs[m%len(regions),0])
            
            else:  par[var_y_name] = host.twinx()
            
            # Offset the right spine of par2.  The ticks and label have already been
            # placed on the right by twinx above.
            if yy>1: 
                par[var_y_name].spines["right"].set_position(("axes", 1+0.17*(yy-1)))
            # Having been created by twinx, par2 has its frame off, so the line of its
            # detached spine is invisible.  First, activate the frame but make the patch
            # and spines invisible.
                make_patch_spines_invisible(par[var_y_name])
            # Second, show the right spine.
                par[var_y_name].spines["right"].set_visible(True)
            
            length = len(dc_reg[var_x_name][reg])
            length_y = len(dc_reg[var_y_name][reg])
            
            if yy==0:
                LL[var_y_name], = host.plot(dc_reg[var_x_name][reg][::int(np.ceil(length/length_y))], 
                          dc_reg[var_y_name][reg][::int(np.ceil(length_y/length))], linestyle='', marker=markers[yy], color=colors[yy], label=var_y_name)
                
                for ii in np.arange(0,min(length, length_y)): #poner etiquetas de time a los puntos
                    host.text(dc_reg[var_x_name][reg][int(ii*length/min(length, length_y))], dc_reg[var_y_name][reg][int(ii*length_y/min(length, length_y))], str(int(dc_reg[var_x_name][reg][time_name][int(ii*length/min(length, length_y))])),
                              fontsize=5)
                    #host.annotate(str(int(dc_reg[model][var_x][seas][reg]['hour'][ii])), (dc_reg[model][var_x][seas][reg][ii], dc_reg[model][var][seas][reg][ii]), xycoords='axis data')
                
                #host.set_xticks(np.append(dc_reg['RCA4'][var][seas][reg]['hour'], 24))
                #host.set_xticklabels(['0','','','3','','','6','','','9','','','12','','','15','','','18','','','21','','','24'])
                host.set_xlabel(var_x_name+' ['+units_labels[var_x_name]+']')
                host.xaxis.set_label_coords(-0.15, -0.05)
                host.yaxis.label.set_color(LL[var_y_name].get_color())
                host.set_ylabel(units_labels[var_y_name])
                tkw = dict(size=4, width=1.5)
                host.tick_params(axis='y', colors=LL[var_y_name].get_color(), **tkw)
                host.tick_params(axis='x', **tkw)

            else:
                LL[var_y_name], = par[var_y_name].plot(dc_reg[var_x_name][reg][::int(np.ceil(length/length_y))], 
                          dc_reg[var_y_name][reg][::int(np.ceil(length_y/length))], linestyle='', marker=markers[yy], color=colors[yy], label=var_y_name)
                
                for ii in np.arange(0,min(length, length_y)): #poner etiquetas de time a los puntos
                    par[var_y_name].text(dc_reg[var_x_name][reg][int(ii*length/min(length, length_y))], dc_reg[var_y_name][reg][int(ii*length_y/min(length, length_y))], str(int(dc_reg[var_x_name][reg][time_name][int(ii*length/min(length, length_y))])),
                       fontsize=5)
                
                par[var_y_name].yaxis.label.set_color(LL[var_y_name].get_color())
                par[var_y_name].tick_params(axis='y', colors=LL[var_y_name].get_color(), **tkw)
                par[var_y_name].set_ylabel(units_labels[var_y_name])
                            
        lines = [LL[var] for var in var_y.keys()]
                    
        #if m==(len(models.keys())*len(regions.keys())-1): host.legend(lines, [l.get_label() for l in lines], fontsize='small', loc=(0.1,-0.6), ncol= 4)
        host.legend(lines, [l.get_label() for l in lines], fontsize='small', loc=(1,1.05), ncol= 4)
        
        #if m%len(regions)==0: host.set_title(model_name+"\n", weight='bold', fontsize=10)            
    
        host.text(-0.1,1.05, numbering[m], transform=host.transAxes)    
        
        ################# add correlations amount - freq|int
    #                host.text(-0.35,1.05, 'corr(a,f): '+str(round(scipy.stats.stats.pearsonr(meanamount[model][seas][reg].values, meanfreq[model][seas][reg].values)[0],2)), transform=host.transAxes, rotation=90)
    #                host.text(-0.25,1.05, 'corr(a,i): '+str(round(scipy.stats.stats.pearsonr(meanamount[model][seas][reg].values, meanintensity[model][seas][reg].values)[0],2)), transform=host.transAxes, rotation=90)
    
        host.grid(axis='x')
        m=m+1
        
    #fig1.subplots_adjust(right=0.9)
    #plt.legend(loc=(1.1,0))
    if not os.path.exists(str(images_path)+var_x_name+'_based'):
        os.makedirs(str(images_path)+var_x_name+'_based')
    fig1.savefig(str(images_path)+var_x_name+'_based'+'/'+filename,dpi=300,bbox_inches='tight',orientation='landscape',papertype='A4')
#    fig1.savefig(str(images_path)+var_x_name+'_based'+'/'+filename, format='pdf',dpi=600,bbox_inches='tight',orientation='landscape',papertype='A4')
    plt.close(fig1)
    
    
# ----------------- funcion de plot rectangulos
def plot_rectangle(ax, lonmin,lonmax,latmin,latmax, col, proj, zorder=None):
    import matplotlib.patches as mpatches
	
    ax.add_patch(mpatches.Rectangle(xy=[lonmin, latmin], width=lonmax-lonmin, height=latmax-latmin,
                                facecolor=col, fill = False,
                                alpha=1, linewidth=2, color=col,
                                transform=proj, zorder=zorder)
             )

    
# ---------------Ploteo los rectangulos en un mapa:
def plot_regions(regions, images_path, proj = False, lonmin = -82, lonmax = -34, latmin = -60, latmax = 13, shownames=True, namepos='top', skogul_home = '/home/julian.giles/datosskogul/'):
    import matplotlib
    import numpy as np
    import matplotlib.pyplot as plt
    import cartopy
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
    import cartopy.crs as ccrs	
    
    if proj == False: proj = ccrs.PlateCarree(central_longitude=0.0)  # Proyeccion cyl eq
    
    matplotlib.rcParams.update({'font.size':15}) #Change font size for all elements
    
    def plot_rectangle(ax, lonmin,lonmax,latmin,latmax, col, proj):
        import matplotlib.patches as mpatches
	
        ax.add_patch(mpatches.Rectangle(xy=[lonmin, latmin], width=lonmax-lonmin, height=latmax-latmin,
                                    facecolor=col, fill = False,
                                    alpha=1, linewidth=2, color=col,
                                    transform=proj)
                 )
    
    print('Plotting regions')    
        
    fig1 = plt.figure( figsize=(6,6),dpi=300)  #fig size in inches
    ax = fig1.add_axes([0.1,0.1,0.8,0.8], projection = proj)
    
    ax.imshow(plt.imread(skogul_home+'Natural_earth/NE2_50M_SR_W.tif'),origin='upper', extent=(-180,180,-90,90), transform=proj)
    
#    ax.stock_img();
#    ax.add_feature(cartopy.feature.LAND)
#    ax.add_feature(cartopy.feature.OCEAN)

    ax.coastlines(resolution='50m', linewidth=1)          # coast
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', linewidth=1, alpha=0.7) #countries
        
    parallels = np.arange(-60,30,10.)
    meridians = np.arange(-90,-20,10.)
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    ax.set_xticks(meridians[1:-1:2], crs=proj)
    ax.set_yticks(parallels[1:-1], crs=proj)
    ax.gridlines(crs=proj, xlocs=meridians, ylocs=parallels, linewidth=1, linestyle='--',zorder=1)

    for reg in regions.keys():
        plot_rectangle(ax, regions[reg][0],regions[reg][1],regions[reg][2],regions[reg][3], regions[reg][4], proj)
        #plot_rectangle(ax, regions[reg][0],regions[reg][1],regions[reg][2],regions[reg][3], regions[reg][4], proj)
        if shownames:
            if namepos == 'top': plt.text(regions[reg][0]+0.3, regions[reg][3]-0.5, reg, va='top')
            if namepos == 'bot': plt.text(regions[reg][0]+0.3, regions[reg][2]+0.5, reg, va='bottom')
    
    ax.set_extent([lonmin, lonmax, latmin, latmax], crs=proj)
    fig1.savefig(images_path+'boxes_location.png',dpi=300,bbox_inches='tight',orientation='landscape',papertype='A4')
    #fig1.savefig(images_path+'boxes_location.pdf', format='pdf', dpi=600,bbox_inches='tight',orientation='landscape',papertype='A4')
    plt.close(fig1)
    

# ------------------------------- Plot de múltiples mapas -------------------

def plot_multiple_maps(fig1, gridrows, gridcols, suptitle, data, timedim_name, clevs, barra, subtitles, extend,
                       filename, lon, lat, lonproj, latproj, proj,
                  images_path, units_labels, fontsize=12): 
    import matplotlib
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import gridspec
    import matplotlib.colors as mcolors
    import cartopy
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
    import os
    from numpy import ma 
    
    ax = fig1.add_axes([0.1,0.1,0.9,0.9])
    ax.set_visible(False)
    gs = gridspec.GridSpec(gridrows,gridcols, wspace=0.2, hspace=0.3)
    
    fig1.suptitle(suptitle, fontsize=fontsize)        
    
    for m in np.arange(0, len(data[timedim_name])):
        if m==gridrows*gridcols: break
        norm = mcolors.BoundaryNorm(boundaries=clevs, ncolors=256)
                
        ax1 = plt.subplot(gs[m], projection = proj)
        ax1.set_extent([lon[0], lon[-1], lat[0], lat[-1]], crs=proj)
                
        CS1 = ax1.pcolormesh(lonproj, latproj, data[m], norm=norm, transform=proj, cmap=barra) 
         
        ax1.coastlines(resolution='50m', linewidth=1)          # coast
        ax1.add_feature(cartopy.feature.BORDERS, linestyle='-', linewidth=1, alpha=0.7) #countries
        
        parallels = np.arange(-60,30,10.)
        meridians = np.arange(-90,-20,10.)
        lon_formatter = LongitudeFormatter(zero_direction_label=True)
        lat_formatter = LatitudeFormatter()
        ax1.xaxis.set_major_formatter(lon_formatter)
        ax1.yaxis.set_major_formatter(lat_formatter)
        
        if m >= len(data[timedim_name])-gridcols-1:
            ax1.set_xticks(meridians[1:-1:2], crs=proj)
            ax1.set_xticklabels(meridians[1:-1:2], fontsize=fontsize/2, position=(0.5,0.05))
        
        if m%gridcols==0:
            ax1.set_yticks(parallels[1:-1], crs=proj)
            ax1.set_yticklabels(parallels[1:-1], fontsize=fontsize/2)
        
        ax1.gridlines(crs=proj, xlocs=meridians, ylocs=parallels, linewidth=0.7, linestyle='--')
        
        ax1.set_title(subtitles[m], fontsize=fontsize/1.5, pad=2)
        
       
    # add colorbar
    fig1.subplots_adjust(right=0.92)
    cbar_ax = fig1.add_axes([0.94, 0.3, 0.01, 0.4]) #[*left*, *bottom*, *width*,  *height*]
    cb =fig1.colorbar(CS1, cax=cbar_ax, extend=extend)
    axis_labels = units_labels
    cb.set_label(axis_labels, labelpad = -2)
    cb.formatter.set_powerlimits((0, 0))  # scientific notation
    
    if not os.path.exists(str(images_path)):
        os.makedirs(str(images_path))
    fig1.savefig(str(images_path)+str(filename),dpi=300,bbox_inches='tight',orientation='landscape',papertype='A4')
    plt.close(fig1)


    
# ------------------------------- Plot ciclos varias variables diurnos cajas -------------------

def plot_dc_regions(models, regions, var_list, dc_reg, images_path, font_size=20):
    # var_list tiene que empezar con la variable de más resolucion temporal
    
    # lista de colores:
    colors = ['Crimson', 'SteelBlue', 'SeaGreen', 'Gold', 'HotPink', 'DimGray', 'DarkViolet', 'MediumSeaGreen', 'Orange', 'MediumBlue', 'MediumVioletRed']
    numbering = ['a)', 'b)', 'c)', 'd)', 'e)', 'f)', 'g)', 'h)', 'i)', 'j)', 'k)', 'l)', 'm)', 'o)', 'p)', 'q)', 'r)', 's)']
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import gridspec
    
    def make_patch_spines_invisible(ax):
        ax.set_frame_on(True)
        ax.patch.set_visible(False)
        for sp in ax.spines.values():
            sp.set_visible(False)
    
    for seas in dc_reg['RCA4'][var_list[0]].keys():
        m=0
        mm=0
        fig1 = plt.figure( figsize=(1+9*len(models.keys()),1+5*len(regions.keys())),dpi=300)  #fig size in inches
        fig1.suptitle('Precipitation mean DCP components in regions '+seas,  y=0.94)
        ax = fig1.add_axes([0.1,0.1,0.9,0.9])
        ax.set_visible(False)
        gs = gridspec.GridSpec(len(regions.keys()),len(models.keys()), wspace=1.3, hspace=0.3)
    
        for model in models.keys():
            mm=mm+1
            
            for reg in regions.keys():
                par = dict()
                LL = dict()
                if mm == 1:
                    fig1.text(0.08,0.96-1/(len(regions)+1.2)*(m+1),reg,transform=ax.transAxes, fontsize=font_size, horizontalalignment='center', verticalalignment='center',rotation='vertical', weight='bold')
                
                for var in var_list:
    
                    if var == var_list[0]:
                        host = plt.subplot(gs[m%len(regions),(mm-1)%len(models)])
                    
                    else:  par[var] = host.twinx()
                    
                    # Offset the right spine of par2.  The ticks and label have already been
                    # placed on the right by twinx above.
                    if var_list.index(var)>1: 
                        par[var].spines["right"].set_position(("axes", 1+0.15*(var_list.index(var)-1)))
                    # Having been created by twinx, par2 has its frame off, so the line of its
                    # detached spine is invisible.  First, activate the frame but make the patch
                    # and spines invisible.
                        make_patch_spines_invisible(par[var])
                    # Second, show the right spine.
                        par[var].spines["right"].set_visible(True)
                    
                    if var == var_list[0]:
                        LL[var], = host.plot(np.append(dc_reg[model][var][seas][reg]['hour'], 24), np.append(np.array(dc_reg[model][var][seas][reg]), np.array(dc_reg[model][var][seas][reg][0])), color=colors[var_list.index(var)], label=var)
                        host.set_xticks(np.arange(0,25))
                        host.set_xticklabels(['0','','','3','','','6','','','9','','','12','','','15','','','18','','','21','','','24'])
                        host.set_xlabel('Hour')
                        host.xaxis.set_label_coords(-0.15, -0.05)
                        host.yaxis.label.set_color(LL[var].get_color())
                        host.yaxis.label.set_fontsize(font_size/3)
                        tkw = dict(size=4, width=1.5)
                        host.tick_params(axis='y', colors=LL[var].get_color(), **tkw)
                        host.tick_params(axis='x', **tkw)
    
                    else:
                        LL[var], = par[var].plot(np.append(dc_reg[model][var][seas][reg]['hour'], 24), np.append(np.array(dc_reg[model][var][seas][reg]), np.array(dc_reg[model][var][seas][reg][0])), color=colors[var_list.index(var)], label=var)
                        par[var].yaxis.label.set_color(LL[var].get_color())
                        par[var].yaxis.label.set_fontsize(font_size/3)
                        par[var].tick_params(axis='y', colors=LL[var].get_color(), **tkw)

                        par[var].set_xticks(np.arange(0,25))
                        par[var].set_xticklabels(['0','','','3','','','6','','','9','','','12','','','15','','','18','','','21','','','24'])
                    
                    #host.set_ylabel('mm/day')
                    #par1.set_ylabel('%')
                    #par2.set_ylabel('mm/day')
                    
                lines = [LL[var] for var in var_list]
                           
                if mm==len(models.keys()) and m%len(regions)==0: host.legend(lines, [l.get_label() for l in lines], fontsize='small', loc=(1,1.05), ncol= 4)
                
                if m%len(regions)==0: host.set_title(model+"\n", weight='bold', fontsize=font_size)            
            
                host.text(-0.1,1.05, numbering[m], transform=host.transAxes)    
                
                ################# add correlations amount - freq|int
            #                host.text(-0.35,1.05, 'corr(a,f): '+str(round(scipy.stats.stats.pearsonr(meanamount[model][seas][reg].values, meanfreq[model][seas][reg].values)[0],2)), transform=host.transAxes, rotation=90)
            #                host.text(-0.25,1.05, 'corr(a,i): '+str(round(scipy.stats.stats.pearsonr(meanamount[model][seas][reg].values, meanintensity[model][seas][reg].values)[0],2)), transform=host.transAxes, rotation=90)
            
                host.grid(axis='x')
                m=m+1
            
        #fig1.subplots_adjust(right=0.9)
        #plt.legend(loc=(1.1,0))
        fig1.savefig(str(images_path)+'/dc_vars_boxes_mean_'+seas+'.jpg',dpi=300,bbox_inches='tight',orientation='landscape',papertype='A4')
        #fig1.savefig(str(images_path)+'/dc_vars_boxes_mean_'+seas+'.pdf', format='pdf',dpi=600,bbox_inches='tight',orientation='landscape',papertype='A4')
        plt.close(fig1)
        
#%%
# ------------- FUNCION PARA LA BARRA DE COLORES DOBLE CON CERO EN BLANCOS ------
def barra_whitecenter(clevs, colormap, no_extreme_colors=False):
    import numpy as np
    import matplotlib
    import matplotlib.colors as mcolors
    
    clevs[int(np.where(np.abs(clevs) < 1E-10)[0])] =0

    if no_extreme_colors:
        colormap = mcolors.ListedColormap(colormap(np.linspace(0.05, 0.95, 256)))
    
    if np.sign(clevs[0]) != np.sign(clevs[-1]) and clevs[0]!=0 and clevs[-1]!=0:
    
        ''' deprecated
        mincolor = colormap(0)
        maxcolor = colormap(250)
        medio1 = colormap(64)
        medio2 = colormap(155)
        mitadbarra = abs(min(clevs))/(max(clevs)+abs(min(clevs)))
        
        barra = mcolors.LinearSegmentedColormap.from_list('BWR', [(0, mincolor),	
                                                                      (mitadbarra/2, medio1),
                                                                      (mitadbarra-(1-mitadbarra)/(sum(clevs>0)+1), 'white'),
                                                                      (mitadbarra+(1-mitadbarra)/(sum(clevs>0)+1), 'white'),
                                                                      ((1+mitadbarra)/2, medio2),
                                                                      (1, maxcolor)])
        #v2
        clevs_range = clevs[-1]  - clevs[0]
        if np.any(clevs==0):
            barra = mcolors.ListedColormap([colormap(int(round(abs(x*colormap.N/2/clevs[0])))) for x in clevs[int(np.where(clevs==0)[0])-1:0:-1]] + 
                                           ['white', 'white'] +
                                           [colormap(int(round(x*colormap.N/2/clevs[-1]+colormap.N/2))) for x in clevs[int(np.where(clevs==0)[0])+1:]])
        else:
            barra = mcolors.ListedColormap([colormap(int(round(abs(x*colormap.N/2/clevs[0])))) for x in clevs[int(np.where(clevs==0)[0])-1:0:-1]] + 
                                           ['white'] +
                                           [colormap(int(round(x*colormap.N/2/clevs[-1]+colormap.N/2))) for x in clevs[int(np.where(clevs==0)[0])+1:]])
        '''            
        #v3
        norm = mcolors.TwoSlopeNorm(0, clevs[0], clevs[-1])
        if np.any(clevs==0):
            barra = mcolors.ListedColormap([colormap(int(x)) for x in norm(clevs[np.where(clevs<0)])[:-1]*colormap.N]+['white','white']+[colormap(int(x)) for x in norm(clevs[np.where(clevs>0)])*colormap.N])
        else:
            barra = mcolors.ListedColormap([colormap(int(x)) for x in norm(clevs[np.where(clevs<0)])*colormap.N]+['white']+[colormap(int(x)) for x in norm(clevs[np.where(clevs>0)])*colormap.N])
            
        
    else:
        barra= colormap
    
    return barra

#%%
# ------------- FUNCION PARA LA BARRA DE COLORES CENTRADA EN CERO ------
def barra_zerocenter(clevs, colormap, no_extreme_colors=False):
    import numpy as np
    import matplotlib
    import matplotlib.colors as mcolors
    
    clevs[int(np.where(np.abs(clevs) < 1E-10)[0])] =0
    
    if no_extreme_colors:
        colormap = mcolors.ListedColormap(colormap(np.linspace(0.1, 0.9, 256)))
    
    if np.sign(clevs[0]) != np.sign(clevs[-1]) and clevs[0]!=0 and clevs[-1]!=0:
        norm = mcolors.TwoSlopeNorm(0, clevs[0], clevs[-1])
        if np.any(clevs==0):
            barra = mcolors.ListedColormap([colormap(int(x)) for x in norm(clevs[np.where(clevs<0)])*colormap.N]+[colormap(int(x)) for x in norm(clevs[np.where(clevs>0)])*colormap.N])
        else:
            barra = mcolors.ListedColormap([colormap(int(x)) for x in norm(clevs[np.where(clevs<0)])*colormap.N]+[colormap(int(x)) for x in norm(clevs[np.where(clevs>0)])*colormap.N])

    else:
        barra= colormap
    
    return barra

#%% Compose figure in parts
"""Así sería el uso de estas funciones
# crear figura y axes
fig1, ax = juli_functions.make_figure(suptitle, figsize=(5,5), general_fontsize=12)

# Si son muchos plots
ax.set_visible(False)
gs = gridspec.GridSpec(nrows,ncols, wspace=0.4, hspace=0.2, width_ratios=[1,1,1]) #si quiero multiples subplos

# Poner en loop si son muchos plot
ax1 = plt.subplot(gs[m], projection = proj)

# barra de colores
barra= juli_functions.barra_whitecenter(clevs ,colormap=matplotlib.cm.get_cmap('RdYlBu_r'))
barra.set_over('Maroon')
barra.set_under('Navy')

# hago cada plot
CS1 = juli_functions.plot_pcolormesh(ax1, data, lon, lat, lonproj, latproj, proj, clevs, barra, title, titlesize = 12, coastwidth = 1, countrywidth = 1)

# agrego flechas
if var== 'vimfc2d' and 'qu2d' and 'qv2d' in var_list or \
var== 'uv900conv' and 'u900' and 'v900' in var_list or \
var== 'uv850conv' and 'u850' and 'v850' in var_list or \
var== 'uv10mconv' and 'u10m' and 'v10m' in var_list:
    juli_functions.plot_arrows(ax1, udata, vdata, lonproj, latproj, proj, units_labels, arrow_spacing = 3, arrow_scale = 4000)

# plot lineas
juli_functions.plot_line(ax1, data_x, data_y, xticks, yticks, ylims, xlabel, ylabel, xticksrot = 90)
plt.legend()

# add colorbar
fig1.subplots_adjust(right=, left=, top=, bottom=)
juli_functions.add_colorbar(fig1, CS1, extend, units_labels, cientific=(0,0), cbaxes= [0.06, 0.3, 0.01, 0.4]) #[*left*, *bottom*, *width*,  *height*]

# save 
juli_functions.savefig(fig1, savepath, filename)
"""


def make_figure(suptitle, figsize=(5,5), general_fontsize=12):
    import matplotlib
    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs	
    
    matplotlib.rcParams.update({'font.size':general_fontsize})
    fig1 = plt.figure( figsize=figsize,dpi=300)  #fig size in inches (width, height)
    ax = fig1.add_axes([0.05,0.05,0.95,0.85], projection= ccrs.PlateCarree(central_longitude=0.0) )
    fig1.suptitle(suptitle)
    return fig1, ax

def plot_pcolormesh(ax1, data, lon, lat, lonproj, latproj, proj, clevs, barra, title, titlesize = 12, titleloc='center', coastwidth = 1, countrywidth = 1, countryalpha=0.7, printlonslats = (True, True), gridline = True, **kwargs):
    import matplotlib.colors as mcolors
    import cartopy
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
    import numpy as np
    import xarray as xr

    norm = mcolors.BoundaryNorm(boundaries=clevs, ncolors=barra.N)
        
    ax1.set_extent([lon[0], lon[-1], lat[0], lat[-1]], crs=proj)
            
    CS1 = ax1.pcolormesh(lonproj, latproj, data, norm=norm, transform=proj, cmap=barra, **kwargs) 
        
    ax1.coastlines(resolution='50m', linewidth= coastwidth, alpha=countryalpha)          # coast
    ax1.add_feature(cartopy.feature.BORDERS, linestyle='-', linewidth=countrywidth, alpha=countryalpha) #countries
    
    parallels = np.arange((xr.ufuncs.trunc(lat/10)*10)[0]-10,(xr.ufuncs.ceil(lat/10)*10)[-1]+10,10.)
    meridians = np.arange((xr.ufuncs.trunc(lon/10)*10)[0]-10,(xr.ufuncs.trunc(lon/10)*10)[-1]+10,10.)
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax1.xaxis.set_major_formatter(lon_formatter)
    ax1.yaxis.set_major_formatter(lat_formatter)
    if printlonslats[0]: ax1.set_xticks(meridians[1:-1:1], crs=proj)
    if printlonslats[1]: ax1.set_yticks(parallels[1:-1], crs=proj)
    if gridline: ax1.gridlines(crs=proj, xlocs=meridians, ylocs=parallels, linewidth=countrywidth, linestyle='--', zorder=5)
    ax1.set_title(title, fontsize=titlesize, loc=titleloc)
    return CS1
    
def plot_arrows(ax1, udata, vdata, lonproj, latproj, proj, units_labels, arrow_spacing = 3, arrow_scale = 4000, arrow_length = 10, 
                plot_key = True, plot_key_pos = (1, -0.1), key_rect=[(-50,-50),14,5], width=3e-3, labelsep=0.1, **kwargs):
    import numpy as np
    from numpy import ma 
    import matplotlib.pyplot as plt
    import matplotlib
    
    # Vectores
    u = np.ones(udata.shape,dtype=bool)
    v = np.ones(vdata.shape,dtype=bool)
    
    u[::arrow_spacing,::arrow_spacing]=0
    v[::arrow_spacing,::arrow_spacing]=0
    
    uu = ma.array(udata,mask = u)
    vv = ma.array(vdata,mask = v)
    
    Q = ax1.quiver(lonproj,latproj,uu,vv,width=width,
                       headwidth=3,#headwidht (default3)
                       headlength=5, scale = arrow_scale, #Scale: Number of data units per arrow length unit, e.g., m/s per plot width; a smaller scale parameter makes the arrow longer. Default is None
                       transform=proj, **kwargs)  # (default5)
    
    rect = matplotlib.patches.Rectangle(key_rect[0], key_rect[1], key_rect[2], facecolor='white', edgecolor='black', transform=proj) #(x,y), width, height
    ax1.add_patch(rect)
    
    if plot_key: qk = plt.quiverkey(Q, plot_key_pos[0], plot_key_pos[1], arrow_length, str(arrow_length)+' '+units_labels, labelpos='S', coordinates='axes', labelsep=labelsep)
    #qk.text.set_backgroundcolor('w')

def plot_line(ax1, data_x, data_y, xticks, yticks, ylims, xlabel, ylabel, label='', title='', xticksrot = 90, color=None, ls=None, **kwargs):
    import matplotlib.pyplot as plt

    plt.plot(data_x, data_y, label=label, color=color, ls=ls, **kwargs) 
    plt.xticks(xticks, rotation=xticksrot)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    #ax1.xaxis.set_label_coords(0.8, -0.1)
    plt.ylim(ylims)
    plt.yticks(yticks)
    plt.grid()
    ax1.set_title(title)
    #sub2.set_ymargin(0.5)

def add_colorbar(fig1, CS1, extend, units_labels, cientific=(-3,3), cbaxes= [0.06, 0.3, 0.01, 0.4], orientation = 'vertical', ticks = None, labelpad=-2, **kwargs):
    cbar_ax = fig1.add_axes(cbaxes) #[*left*, *bottom*, *width*,  *height*]
    cb =fig1.colorbar(CS1, cax=cbar_ax, extend=extend, orientation=orientation, ticks=ticks, **kwargs)
    axis_labels = units_labels
    cb.set_label(axis_labels, labelpad = labelpad)
    cb.formatter.set_powerlimits(cientific)  # scientific notation
    cb.update_ticks()

def savefig(fig1, savepath, filename, bbox_inches='tight'):
    import matplotlib.pyplot as plt
    import os

    if not os.path.exists(savepath):
        os.makedirs(savepath)
    fig1.savefig(str(savepath)+str(filename),dpi=300,bbox_inches=bbox_inches,orientation='landscape')
    plt.close(fig1)    
 
def make_patch_spines_invisible(ax):# para ocultar ejes en plots combinados
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)


