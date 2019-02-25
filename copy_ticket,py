#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from optparse import OptionParser
from mantis.Connector import Connector
from mantis.IssueViewer import IssueViewer
from mantis.Utils import changeIssueProject

import sys
import functools
print_flush = functools.partial(print, flush=True)

MANTIS_URL = "http://osoft-de-c.olympus.co.jp/mantis/ipf3/app/api/soap/mantisconnect.php?wsdl"

def toIssueIdList(issueIds):
    splited_str = issueIds.split(',')
    return splited_str

def mainEntry():
    connector = Connector(MANTIS_URL, options.username, options.password)
    connector.connect()

    print_flush("Mantis SOAP MC Version:" + connector.getVersion())

    issueIds = toIssueIdList(options.issueId_list)

    projectId = connector.getProjectId(options.project)
    print_flush("{}, ProjectId: {}".format(options.project, str(projectId)))


    for issueIdStr in issueIds:
        issueId = int(issueIdStr) 
        print_flush("move {} issue to project {}".format(issueId, projectId))
        changeIssueProject(connector, issueId, projectId)

def printHelpMessageAndExit(option, parser):
    print_flush(option, 'option is required.')
    parser.print_help()
    sys.exit(1)

if __name__ == '__main__':

    parser = OptionParser()  

    parser.add_option("-l", "--issue-ids", default = None,
        action = "store", dest = "issueId_list",
        help = "Mantis Issue id list e.g.: 1,2,3,4")

    parser.add_option("-P", "--project", default = None,
        action = "store", dest = "project",
        help = "Destination Project name")

    parser.add_option("-u", "--username",
        action = "store", dest = "username",
        help = "Mantis username")

    parser.add_option("-p", "--password",
        action = "store", dest = "password",
        help = "Mantis password")

    (options, args) = parser.parse_args()

    for option, value in vars(options).items():
        if value is None:
            printHelpMessageAndExit(option, parser)

    mainEntry()
