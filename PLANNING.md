# Project Planning

## Problem Statement

### Primary User(s)

Input User: Property Management Firm ( Cushman & Wakefield, CBRE, etc.)              
Receiving User: Asset Management Firm (Brookfield, Blackstone, Heitman, etc.)

### Problem Overview

Both Property Management firms and Asset Management firms require timely and 
accurate data. When dealing with physical properties an assets operational 
data (leases) is key. When a new lease is agreed upon and signed, a lawyer typically
drafts up a 50+ page document, which is then sent to both the Property Management
firm as well as the Asset Management firm. Both firms then require an analyst to
spend hours digging through this massive PDF of legal jargon in order to pull out the key data
elements neccesary for input in their property management systems. This process is extrmeley time
consuming and inefficient.

### User Needs Statement

Property managers and Asset managers require timely and accurate leasing data in 
order to value assets and create reports for their investors. Getting this information
faster and more efficiently will allow these firms to spend more time on analysis 
and investor deliverables.

### As is Process Description
1. Tenant meets with property management firm to discuss lease terms
2. Agreed upon terms are then sent to legal to draft lease agreement (how this is sent is inconsistent)
3. Lawyers generate lease agreement which is sent to proeprty management firm and tenant to sign
4. Signed lease agreement is sent to both property management firm & asset management firm
5. Property Management analyst spends hours pulling out and inputting data elements into their system.
6. Asset Management analyst also spends hours pulling out and inputting data elements into their repsective system.

### To-be Process Description
1. Same step 1
2. At this stage when the terms are sent to legal they are input via a front end UI
(command line for the sake of this project)
3. Once input the user would click "Generate", the solution organizes the data into three different formats: 
    + Clean report output (command line output for this project)
    + .CSV File
    + Restful or JSON API
7. The lawyers can use one of the 3 outputs to still generate a lease agreement
8. Property management firms & Asset management firms can now utilize one of these
three formats to pull the key data elements as soon as they are generated and no one has to read a lease agreement
ever again.

## Information Requirements

### Information Inputs

1. All inputs come directly from the command prompt, inputted at the onset of lease agreement.

### Information Outputs

1. Report (Command-Line)
2. 'Abstract.csv' file containing key data elements of lease agreement
3. 'Restful API' or 'JSON API' key data elements will be stored in an API which firms could call into their respective systems.

## Technology Requirements

### APIs and Web Service Requirements

This solution will not need to call to any API's or web services to get data, however I would like to store the data input through
the command prompt to an API, which in theory could be called by someone else.

### Python Package Requirements

The application does not require any third-party packages except 'pytest' for testing purposes.

The application does however make extensive use of the 'os', 'csv' , 'json' , and 'datetime' modules.

### Hardware Requirements

The application will be running on a local machine. However I would like the results that get stored in the API to be available on a public server.

