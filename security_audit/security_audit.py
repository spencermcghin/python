#!/usr/bin/python

""" Security mapping audit for OBIEE 12c. This code will generate a permissions report for all
catalog objects, for the server upon which it is run. It takes the domain home as an argument in
order to generate the report. This code will create data frames out of the two csv files generated
by the security_audit.py code and then show you those rows which only exist on the lower environment,
or whichever environment you'd like to validate against.
1. Run code once on lower environment application server.
2. Run code once again on target migration environment.
3. Move file 'C:\security_mappings.csv or /tmp/security_mappings.csv from target
   migration server to lower environment server and rename it 'security_mappings_02',
   placing it in the same directory as your other security_mappings.csv file.
4. Run security_compare.py and open audit_results.html to view test results."""


# Imports - please ensure these are installed on all servers
import os
import sys
import pandas as pd
import platform

# Set domain home as argument
domain_home = sys.argv[1]

# Makes sure DOMAIN_HOME is set and then cd to bitools dir
os.chdir(domain_home+'/bitools/bin')

# OBIEE runcat file drop locations
file_loc_win = 'C:\\permissions_report.csv'
file_loc_lin = '/tmp/permissions_report.csv'


""" Main functions for program."""


# Run runcat script to generate csv permissions report - note report output in C:\
def win_runcat():
    os.system('runcat.cmd -cmd report -offline C:/Oracle/Middleware' +
              '/Oracle_Home/user_projects/domains/bifoundation/bidata' +
              '/service_instances/ssi/metadata/content/catalog'
              ' -forceoutputFile C:\\permissions_report.csv'
              ' -type "All" -folder "/shared"'
              ' -fields "Owner:Name:Path:ACL:Group Members" -delimiter ","')


def lin_runcat():
    os.system('runcat.sh -cmd report -offline C:/Oracle/Middleware' +
              '/Oracle_Home/user_projects/domains/bifoundation/bidata' +
              '/service_instances/ssi/metadata/content/catalog'
              ' -forceoutputFile /tmp/permissions_report.csv'
              ' -type "All" -folder "/shared"'
              ' -fields "Owner:Name:Path:ACL:Group Members" -delimiter ","')


# Export cleaned up dataframes to server as csv
def exp_to_csv_win(exp_file):
    export = pd.DataFrame(exp_file)
    win_path = 'C:\\security_mappings.csv'
    export.to_csv(win_path, index=False)


def exp_to_csv_lin(exp_file):
    export = pd.DataFrame(exp_file)
    lin_path = '/tmp/security_mappings.csv'
    export.to_csv(lin_path, index=False)


# Create and clean up dataframes and then dump to csv
def df_to_cleancsv(csv):
    df = pd.DataFrame(pd.read_csv(csv))
    #  Clean up ACL column values
    df['ACL'] = df['ACL'].str.replace('^', ' ').str.replace(':', '').str.replace('=', ':')
    df = df.sort_values(['Owner'])
    return df

# Main Program


if __name__ == '__main__':
    if platform.system() == 'Windows':
        win_runcat()
        export_win = df_to_cleancsv(file_loc_win)
        os.remove(file_loc_win)  # Get rid of runcat csv output
        exp_to_csv_win(export_win)  # Export dataframe to csv using function above
    elif platform.system() == 'Linux':
        lin_runcat()
        export_lin = df_to_cleancsv(file_loc_lin)
        os.remove(file_loc_lin)
        exp_to_csv_lin(export_lin)