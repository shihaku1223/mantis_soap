#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys
from mantis.Connector import Connector
from mantis.IssueViewer import IssueViewer
from mantis.Utils import changeIssueProject

from mantisconnect.project import Issue

import datetime
import zeep


if __name__ == '__main__':

    url = "http://osoft-de-c.olympus.co.jp/mantis/ipf3/app/api/soap/mantisconnect.php?wsdl"
    connector = Connector(url, "10079186", "123")
    connector.connect()

    #print("Mantis SOAP MC Version:" + connector.getVersion())
    issue = connector.getIssue(37957)
    print(issue)
    #viewer = IssueViewer(issue)
    #print(viewer.getLastUpdatedTime())
    #print(viewer.getProjectName())
    sys.exit(0)

    projectId = connector.getProjectId('機能UI')
    print("ProjectId: " + str(projectId))

    try:
        #issues = connector.getProjectIssues(projectId)
        issues = connector.getIssuesByFilter(projectId, 9348, 0, 0)

        print("Issues count:"+ str(len(issues)))
    except zeep.exceptions.TransportError as e:
        print(e.content)
    except zeep.exceptions.XMLSyntaxError as e:
        print(e)

    """
    for issue in issues:
        viewer = IssueViewer(issue)
        print(viewer.getId())
    """

    #issue = connector.getIssue(40507)
    #connector.updateIssueStatus(issue, 10)

    #users = connector.getProjectIssues(212)
    #print(len(users))
    #print(connector.test())

    #projectId = connector.getProjectId('sandbox_integ')
    #projectId = connector.getProjectId('TEST')
    #print(projectId)
    #changeIssueProject(connector, 30123, projectId)
