from collections import OrderedDict

states = OrderedDict([
    ('AK', 'Alaska'),
    ('AL', 'Alabama'),
    ('AR', 'Arkansas'),
    ('AS', 'American Samoa'),
    ('AZ', 'Arizona'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DC', 'District of Columbia'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('GU', 'Guam'),
    ('HI', 'Hawaii'),
    ('IA', 'Iowa'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('MA', 'Massachusetts'),
    ('MD', 'Maryland'),
    ('ME', 'Maine'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MO', 'Missouri'),
    ('MP', 'Northern Mariana Islands'),
    ('MS', 'Mississippi'),
    ('MT', 'Montana'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('NE', 'Nebraska'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NV', 'Nevada'),
    ('NY', 'New York'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('PR', 'Puerto Rico'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VA', 'Virginia'),
    ('VI', 'Virgin Islands'),
    ('VT', 'Vermont'),
    ('WA', 'Washington'),
    ('WI', 'Wisconsin'),
    ('WV', 'West Virginia'),
    ('WY', 'Wyoming'),
])

parties = OrderedDict([
    ('DEM', 'Democratic Party'),
    ('REP', 'Republican Party'),
])
parties_extended = OrderedDict([
    ('AIC', 'American Independent Conservative'),
    ('AIP', 'American Independent Party'),
    ('AMP', 'American Party'),
    ('APF', "American People's Freedom Party"),
    ('CIT', "Citizens' Party"),
    ('CMP', 'Commonwealth Party of the U.S.'),
    ('COM', 'Communist Party'),
    ('CRV', 'Conservative Party'),
    ('CST', 'Constitutional'),
    ('D/C', 'Democratic/Conservative'),
    ('DFL', 'Democratic-Farm-Labor'),
    ('FLP', 'Freedom Labor Party'),
    ('GRE', 'Green Party'),
    ('GWP', 'George Wallace Party'),
    ('HRP', 'Human Rights Party'),
    ('IAP', 'Independent American Party'),
    ('ICD', 'Independent Conserv. Democratic'),
    ('IGD', 'Industrial Government Party'),
    ('IND', 'Independent'),
    ('LAB', 'U.S. Labor Party'),
    ('LBL', 'Liberal Party'),
    ('LBR', 'Labor Party'),
    ('LBU', 'Liberty Union Party'),
    ('LFT', 'Less Federal Taxes'),
    ('LIB', 'Libertarian'),
    ('LRU', 'La Raza Unida'),
    ('NAP', 'Prohibition Party'),
    ('NDP', 'National Democratic Party'),
    ('NLP', 'Natural Law Party'),
    ('PAF', 'Peace and Freedom'),
    ('PFD', 'Peace Freedom Party'),
    ('POP', 'People Over Politics'),
    ('PPD', 'Protest, Progress, Dignity'),
    ('PPY', "People's Party"),
    ('REF', 'Reform Party'),
    ('RTL', 'Right to Life'),
    ('SLP', 'Socialist Labor Party'),
    ('SUS', 'Socialist Party U.S.A.'),
    ('SWP', 'Socialist Workers Party'),
    ('THD', 'Theo-Dem'),
    ('TWR', 'Taxpayers Without Representation'),
    ('TX', 'Taxpayers'),
    ('USP', "U.S. People's Party"),
])

report_types = OrderedDict([
    ('M1', 'January Monthly'),
    ('M2', 'February Monthly'),
    ('M3', 'March Monthly'),
    ('M4', 'April Monthly'),
    ('M5', 'May Monthly'),
    ('M6', 'June Monthly'),
    ('M7', 'July Monthly'),
    ('M8', 'August Monthly'),
    ('M9', 'September Monthly'),
    ('M10', 'October Monthly'),
    ('M11', 'November Monthly'),
    ('M12', 'December Monthly'),
    ('MYE', 'Monthly Year-end'),
    ('Q1', 'April Quarterly'),
    ('Q2', 'July Quarterly'),
    ('Q3', 'October Quarterly'),
    ('MY', 'Mid-year Report'),
    ('YE', 'Year-end'),    
    ('12P', 'Pre-Primary'),
    ('12C', 'Pre-Convention'),
    ('12G', 'Pre-General'),
    ('12R', 'Pre-Runoff'),
    ('12S', 'Pre-Special'),
    ('30G', 'Post-General'),
    ('30R', 'Post-Runoff'),
    ('30S', 'Post-Special'),
    ('30P', 'Post-Primary'),
    ('60D', '60 Day Post Convention of a Presidential Host Committee'),
    ('TER', 'Termination Report'),
    ('24', '24-Hour Report'),
    ('48', '48-Hour Report'),
    ('90D', '90 Day Post Inaugural Report by an Inaugural Committee'),
    ('90S', 'Supplement to a 90D Inaugural Report'),
    ('CA', 'COMPREHENSIVE AMEND'),
    ('ADJ', 'COMP ADJUST AMEND'),
    ('M7S', 'July 20 (M7) Monthly report and Semi-Annual'),
    ('MSA', 'Semi-Annual only'),
    ('MSY', 'Semi-Annual only'),
    ('MYS', 'Jan 31 Year End (MYE) report and Semi-annual'),
    ('Q2S', 'July 15 (Q2) report and Semi-annual'),
    ('QSA', 'Semi-Annual only'),
    ('QYE', 'Semi-Annual only'),
    ('QYS', 'Jan 31 Year End (YE) report and Semi-Annual'),
    ('QMS', 'July 31 Mid-Year (MY) report and Semi-annual'),
    ('10D', 'PRE-ELECTION'),
    ('10G', 'PRE-GENERAL'),
    ('10P', 'PRE-PRIMARY'),
    ('10R', 'PRE-RUN-OFF'),
    ('10S', 'PRE-SPECIAL'),
    ('30D', 'POST-ELECTION'),
])

form_types = OrderedDict([
    ('F1', "Statement Of Organization"),
    ('F1M', "Notification Of Multicandidate Status"),
    ('F2', "Statement Of Candidacy"),
    ('F3', "Receipts And Disbursements - Authorized Committee"),
    ('F3P', "Receipts And Disbursements - Authorized Committee Presidential"),
    ('F3X', "Receipts And Disbursements - Non-Authorized Committee"),
    ('F3L', "Contributions Bundled By Lobbyist/Registrants And Lobbyist/Registrant PACs"),
    ('F4', "Receipts And Disbursements - Convention Committee"),
    ('F5', "Independent Expenditures Made And Contributions Received"),
    ('F24', "24/48 Hour Notice Of Independent Expenditures or Coordinated Expenditures"),
    ('F6', "48-Hour Notice Of Contributions/Loans Received"),
    ('F7', "Communication Costs - Corporations And Membership Orgs"),
    ('F8', "Debt Settlement Plan"),
    ('F9', "24-Hour Notice Of Disbursement/Obligations For Electioneering Communications"),
    ('F13', "Donations Accepted For Inaugural Committee"),
    ('F10', "24-Hour Notice Of Expenditure From Candidate's Personal Funds"),
    ('F99', "Miscellaneous Submission"),
    ('RFAI', "Request For Additional Information"),
])

amendment_indicators = OrderedDict([
    ('N', 'New'),
    ('A', 'Amended'),
])
amendment_indicators_extended = OrderedDict([
    ('T', 'Terminated'),
    ('C', 'Consolidated'),
    ('M', 'Multi-Candidate'),
    ('S', 'Secondary'),
])
