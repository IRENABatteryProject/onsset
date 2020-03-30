import os
from runner import scenario

countries = ['ao', 'bf', 'bi', 'bj', 'bw', 'cd', 'cf', 'cg', 'ci', 'cm', 'dj', 'er', 'et', 'ga', 'gh', 'gm', 'gn', 'gq',
             'gw', 'ke', 'km', 'lr', 'ls', 'mg', 'ml', 'mr', 'mw', 'mz', 'na', 'ne', 'ng', 'rw', 'sd', 'sl', 'sn', 'so',
             'ss', 'st', 'sz', 'td', 'tg', 'tz', 'ug', 'za', 'zm', 'zw']

countries = ['ao', 'bf', 'bi', 'bj', 'bw', 'cd', 'cf', 'cg', 'ci', 'cm', 'dj', 'er', 'et', 'gh', 'gm', 'gq',
             'ke', 'km', 'lr', 'ls', 'mg', 'ml', 'mr', 'mw', 'mz', 'na', 'ng', 'rw', 'sd', 'sl', 'sn', 'so',
             'ss', 'st', 'sz', 'td', 'tg', 'tz', 'ug', 'za', 'zm', 'zw']

for country in countries:
    general_specs = 'C:/Users/asahl/Box Sync/Scenario_discovery/common-specs.xlsx'
    specs_path = os.path.join('C:/Users/asahl/Box Sync/Scenario_discovery/Specs_files', "{}-1-specs.xlsx".format(country))
    csv_path = os.path.join(
        'C:/Users/asahl/Box Sync/EGI Energy Systems/06 Projects/2017-11 WB Electrification Platform/Paper/Andreas Paper files/{}_inputs'.format(country),
        '{}-1-country-inputs.csv'.format(country))
    summary_folder = os.path.join('C:/Users/asahl/Box Sync/Scenario_discovery/Summaries', '{}'.format(country))
    results_folder = os.path.join('C:/Users/asahl/Box Sync/Scenario_discovery/Summaries', '{}'.format(country))
    scenario(specs_path, csv_path, results_folder, summary_folder, general_specs)
